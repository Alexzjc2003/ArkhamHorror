from __future__ import annotations
from enum import Enum
from typing import TYPE_CHECKING

from action.action import GameAction
from event.event import PlayerAlreadyDrawEvent, PlayerWouldDrawEvent
from game import Game
import investigator

if TYPE_CHECKING:
    from card import Card
    from deck import Deck
    from enemy import Enemy
    from investigator import Investigator


class ActionType(Enum):
    Draw = "Draw"
    Fight = "Fight"


class PlayerAction(GameAction):
    type: ActionType

    def __init__(self, type: ActionType):
        super().__init__(f"player_action: {type.value}")

        self.type = type


class DrawAction(PlayerAction):
    investigator: Investigator
    deck: Deck
    card: list[Card] | None
    amount: int

    def __init__(
        self,
        investigator: Investigator,
        deck: Deck,
        amount: int = 1,
    ):
        super().__init__(type=ActionType.Draw)

        self.investigator = investigator
        self.deck = deck
        self.card = None
        self.amount = amount

        wouldDraw = PlayerWouldDrawEvent(
            "would draw", self.investigator, self.deck, self.amount
        )
        Game.triggerEvent(wouldDraw)

        if wouldDraw.cancelled:
            return

        # draw card
        self.investigator = wouldDraw.investigator
        self.deck = wouldDraw.deck
        self.amount = wouldDraw.amount

        self.card = [self.deck.drawFromTop() for _ in range(self.amount)]

        Game.triggerEvent(
            PlayerAlreadyDrawEvent(
                "already draw", self.investigator, self.deck, self.card
            )
        )


class FightAction(PlayerAction):
    investigator: Investigator
    target: Enemy

    def __init__(self, investigator: Investigator, target: Enemy):
        super().__init__(ActionType.Fight)
