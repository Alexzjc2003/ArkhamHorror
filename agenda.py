from __future__ import annotations

from card import Card
from deck import Deck


class AgendaCard(Card):
    doomThreshold: int

    def __init__(self, name: str, threshold: int):
        super().__init__(name)
        self.doomThreshold = threshold

    def flip(self): ...


class Agenda:
    deck: Deck[AgendaCard]

    @property
    def currentAgenda(self) -> AgendaCard:
        return self.deck.getTop()

    def __init__(self):
        self.deck = Deck[AgendaCard]()

        ...

    def advance(self):
        # remove each token on card
        self.deck.getTop().token.clear()
        # flip current agenda
        self.deck.getTop().flip()

        # remove the current agenda
        self.deck.drawFromTop()
