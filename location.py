from __future__ import annotations

from card import Card


class Location:
    card: LocationCard

    @property
    def clue(self) -> int:
        return self.card.token.clue

    def __init__(self, card: LocationCard):
        self.card = card


class LocationCard(Card):
    def __init__(self, name):
        super().__init__(name)
