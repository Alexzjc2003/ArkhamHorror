from __future__ import annotations

from enum import Enum
from typing import TYPE_CHECKING, Self
from abc import ABC, abstractmethod

from event.event_type import EventType
from listener.event_listener import EventListener, Handle


if TYPE_CHECKING:
    from encounter import EncounterDeck
    from investigator import Investigator
    from player import Player


class Token:
    resource: int
    doom: int
    clue: int
    damage: int
    horror: int

    def __init__(
        self,
        resource: int = 0,
        doom: int = 0,
        clue: int = 0,
        damage: int = 0,
        horror: int = 0,
    ):
        self.resource = resource
        self.doom = doom
        self.clue = clue
        self.damage = damage
        self.horror = horror

    def clear(self):
        self.resource = 0
        self.doom = 0
        self.clue = 0
        self.damage = 0
        self.horror = 0


class CardType(Enum):
    Investigator = "Investigator"
    Enemy = "Enemy"
    Agenda = "Agenda"
    Treachery = "Treachery"


class Card:
    name: str
    owner: Player | EncounterDeck | None
    type: CardType
    token: Token

    def __init__(
        self,
        name: str,
        owner: Player | EncounterDeck | None = None,
        token: Token = Token(),
    ):
        self.name = name
        self.owner = owner
        self.token = token

    def setOwner(self, owner: Player | EncounterDeck) -> Self:
        self.owner = owner
        return self
