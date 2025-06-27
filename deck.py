from __future__ import annotations

from typing import Self, Generic, TypeVar


import random
from area import AreaOutOfPlay
from card import Card


class EmptyDeckException(Exception):
    def __init__(self, deck: Deck):
        super().__init__(f"{deck}")


TCard = TypeVar("TCard", bound=Card)


class Deck(Generic[TCard], AreaOutOfPlay):
    cards: list[TCard]
    discardPile: DiscardPile

    def __init__(self, discardPile: DiscardPile):
        AreaOutOfPlay.__init__(self)
        self.discardPile = discardPile

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


class DiscardPile(Generic[TCard], AreaOutOfPlay):
    cards: list[TCard]

    def __init__(self):
        AreaOutOfPlay.__init__(self)
