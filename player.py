from __future__ import annotations

from typing import TYPE_CHECKING

from deck import Deck, DiscardPile

if TYPE_CHECKING:
    from investigator import Investigator


class Player:
    investigator: Investigator
    deck: Deck
    discardPile: DiscardPile

    def __init__(self):
        self.deck = Deck(DiscardPile())
        self.discardPile = self.deck.discardPile
        pass
