from __future__ import annotations

from typing import Generic, Self, TypeVar


import random
from card import Card


class EmptyDeckException(Exception):
    def __init__(self, deck: Deck):
        super().__init__()


TCard = TypeVar("TCard", bound=Card)


class Deck(Generic[TCard]):
    cards: list[TCard]
    discardPile: DiscardPile[TCard]

    def __init__(self):
        self.cards = []
        self.discardPile = DiscardPile[TCard]()

    def putOnTop(self, card: TCard) -> Self:
        self.cards.insert(0, card)
        return self

    def putOnBottom(self, card: TCard) -> Self:
        self.cards.append(card)
        return self

    def shuffle(self) -> Self:
        random.shuffle(self.cards)
        return self

    def drawFromTop(self) -> TCard:
        if len(self.cards) == 0:
            raise EmptyDeckException(self)

        return self.cards.pop(0)

    def drawFromBottom(self) -> TCard:
        if len(self.cards) == 0:
            raise EmptyDeckException(self)

        return self.cards.pop(-1)

    def reset(self) -> Self:
        while len(self.discardPile.cards) != 0:
            self.cards.append(self.discardPile.cards.pop())
        return self.shuffle()

    def add(self, card: TCard) -> Self:
        return self.putOnBottom(card)

    def getTop(self) -> TCard:
        if len(self.cards) == 0:
            raise EmptyDeckException(self)
        return self.cards[0]

    def getBottom(self) -> TCard:
        if len(self.cards) == 0:
            raise EmptyDeckException(self)
        return self.cards[-1]

    def discard(self, card: TCard) -> TCard:
        self.discardPile.cards.append(card)
        return card


class DiscardPile(Generic[TCard]):
    cards: list[TCard]

    def __init__(self):
        self.cards = []


class EncounterDeck(Deck):

    def __init__(self):
        super().__init__()

    def drawFromTop(self) -> Card:
        if len(self.cards) == 0:
            self.reset()
        return super().drawFromTop()

    def drawFromBottom(self) -> Card:
        if len(self.cards) == 0:
            self.reset()
        return super().drawFromBottom()
