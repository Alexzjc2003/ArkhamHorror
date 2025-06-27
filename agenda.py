from __future__ import annotations

from typing import TYPE_CHECKING, Self

from encounter import EncounterDeck
from player import Player

if TYPE_CHECKING:
    from encounter import EncounterDeck

from card import Card
from deck import Deck, DiscardPile


class AgendaCard(Card):
    owner: EncounterDeck
    doomThreshold: int

    def __init__(self, name: str, threshold: int):
        super().__init__(name)
        self.doomThreshold = threshold

    def flip(self): ...
    def setOwner(self, owner: EncounterDeck) -> Self:
        return super().setOwner(owner)


class Agenda:
    deck: Deck[AgendaCard]

    @property
    def currentAgenda(self) -> AgendaCard:
        return self.deck.getTop()

    def __init__(self):
        self.deck = Deck[AgendaCard](DiscardPile[AgendaCard]())
        ...

    def advance(self):
        # remove each token on card
        self.deck.getTop().token.clear()
        # flip current agenda
        self.deck.getTop().flip()

        # remove the current agenda
        self.deck.drawFromTop()
