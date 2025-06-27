from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from card import Card


class Area:
    cards: list[Card]

    isInPlay: bool

    def __init__(self, isInPlay: bool):
        self.cards = []
        self.isInPlay = isInPlay


class AreaInPlay(Area):
    def __init__(self):
        Area.__init__(self, True)


class AreaOutOfPlay(Area):
    def __init__(self):
        Area.__init__(self, False)


class AreaManager:
    cardArea: dict[Card, Area]

    def __init__(self):
        self.cardArea = {}

    def set(self, card: Card, area: Area):
        self.cardArea[card] = area

    def get(self, card: Card) -> Area | None:
        return self.cardArea.get(card, None)

    def move(self, card: Card, src: Area, dst: Area):
        src.cards.remove(card)
        dst.cards.append(card)

        self.set(card, dst)

    def put(self, card: Card, dst: Area):
        assert self.get(card) is None
        dst.cards.append(card)

        self.set(card, dst)
