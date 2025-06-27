from __future__ import annotations


from inspect import isclass
from operator import inv
from typing import Tuple

from agenda import Agenda
from card import Card
from element import Damageable
from event.event import (
    AlreadyDealDamageHorrorEvent,
    AlreadyDiscoverClueEvent,
    AlreadyPlaceDoomEvent,
    WouldDealDamageHorrorEvent,
    WouldDiscoverClueEvent,
    WouldPlaceDoomEvent,
)
from game import Game
from investigator import Investigator
from location import Location


class GameAction:
    name: str

    def __init__(self, name: str):
        self.name = name


class PlaceDoom(GameAction):
    target: Card
    amount: int

    def __init__(self, target: Card | Agenda, amount: int = 1):
        if isinstance(target, Card):
            self.target = target
        elif isinstance(target, Agenda):
            self.target = target.currentAgenda
        else:
            raise TypeError("Invalid target to place doom")
        self.amount = amount

        wouldPlaceDoom = WouldPlaceDoomEvent(
            "would place doom", self.target, self.amount
        )
        Game.triggerEvent(wouldPlaceDoom)

        if wouldPlaceDoom.isCancelled:
            return

        self.target = wouldPlaceDoom.target
        self.amount = wouldPlaceDoom.amount

        self.target.token.doom += self.amount

        Game.triggerEvent(AlreadyPlaceDoomEvent("doom placed", self.target))


class DealDamageHorror(GameAction):
    target: Damageable | Investigator
    by: Card | None
    amount: Tuple[int, int]

    def __init__(
        self,
        target: Damageable,
        by: Card | None,
        amount: Tuple[int, int],
    ):
        self.target = target
        self.by = by
        self.amount = amount

        wouldDealDamageHorror = WouldDealDamageHorrorEvent(
            "would deal damage/horror", self.target, self.by, self.amount
        )
        Game.triggerEvent(wouldDealDamageHorror)

        self.target = wouldDealDamageHorror.target
        self.by = wouldDealDamageHorror.by
        self.amount = wouldDealDamageHorror.amount

        # apply damage/horror

        self.target.takeDamage(self.amount[0])
        self.target.takeHorror(self.amount[1])

        fatal = self.target.canTakeDamage() == 0 or self.target.canTakeHorror() == 0

        alreadyDealDamageHorror = AlreadyDealDamageHorrorEvent(
            "already deal damage/horror", self.target, self.by, self.amount, fatal
        )
        Game.triggerEvent(alreadyDealDamageHorror)


class DiscoverClue(GameAction):
    investigator: Investigator
    amount: int
    location: Location

    def __init__(self, investigator: Investigator, amount: int, location: Location):
        self.investigator = investigator
        self.amount = amount
        self.location = location

        if self.location.clue == 0:
            return
        elif self.location.clue < self.amount:
            self.amount = self.location.clue

        wouldDiscoverClue = WouldDiscoverClueEvent(
            "would discover clue", self.investigator, self.amount, self.location
        )
        Game.triggerEvent(wouldDiscoverClue)
        if wouldDiscoverClue.isCancelled:
            return

        self.investigator = wouldDiscoverClue.investigator
        self.amount = wouldDiscoverClue.amount
        self.location = wouldDiscoverClue.location

        if self.amount == 0 or self.location.clue == 0:
            return
        elif self.location.clue < self.amount:
            self.amount = self.location.clue

        location.card.token.clue -= self.amount
        self.investigator.card.token.clue += self.amount

        Game.triggerEvent(
            AlreadyDiscoverClueEvent(
                "already discover clue", investigator, amount, location
            )
        )
