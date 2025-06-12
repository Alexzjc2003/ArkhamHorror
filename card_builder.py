from __future__ import annotations

from typing import TypeVar, TYPE_CHECKING

from card import Card
from deck import Deck

# if TYPE_CHECKING:


class CardBuilder:

    TCard = TypeVar("TCard", bound=Card)

    def __init__(self): ...

    def build(self, tCard: type[TCard], deck: Deck, *args, **kwargs):
        card = tCard(*args, **kwargs)
        card.deck = deck
        return card
