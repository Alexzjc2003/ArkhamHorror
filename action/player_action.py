from __future__ import annotations
from enum import Enum
from typing import TYPE_CHECKING

from action.action import GameAction
from event.event import PlayerAlreadyDrawEvent, PlayerWouldDrawEvent
from game import Game

if TYPE_CHECKING:
    from card import Card
    from deck import Deck
    from investigator import Investigator


class ActionType(Enum):
    Draw = "Draw"


class ActionCost:
    resource: int | None
    action: int | None

    charge: int | None
    secret: int | None
    ammo: int | None

    def __init__(
        self,
        resource: int | None = None,
        action: int | None = None,
        charge: int | None = None,
        secret: int | None = None,
        ammo: int | None = None,
    ):

        self.resource = resource
        self.action = action
        self.charge = charge
        self.secret = secret
        self.ammo = ammo

        ...


class PlayerAction(GameAction):
    type: ActionType
    cost: ActionCost

    def __init__(self, type: ActionType, cost: ActionCost = ActionCost()):
        super().__init__(f"player_action: {type.value}")

        self.type = type
        self.cost = cost


class DrawAction(PlayerAction):
    investigator: Investigator
    deck: Deck
    card: list[Card] | None
    count: int

    def __init__(
        self,
        investigator: Investigator,
        deck: Deck,
        cost: ActionCost = ActionCost(),
        count: int = 1,
    ):
        super().__init__(type=ActionType.Draw, cost=cost)

        self.investigator = investigator
        self.deck = deck
        self.card = None
        self.count = count

        wouldDraw = PlayerWouldDrawEvent(
            "would draw", self.investigator, self.deck, self.count
        )
        Game.triggerEvent(wouldDraw)

        if wouldDraw.cancelled:
            return

        # draw card
        self.investigator = wouldDraw.investigator
        self.deck = wouldDraw.deck
        self.count = wouldDraw.count

        self.card = [self.deck.drawFromTop() for _ in range(self.count)]

        Game.triggerEvent(
            PlayerAlreadyDrawEvent(
                "already draw", self.investigator, self.deck, self.card
            )
        )
