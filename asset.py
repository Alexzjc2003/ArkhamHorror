from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from area import AreaInPlay


from card import Card, CardType, Icon, Slot


class AssetCard(Card):
    cost: int | None
    slot: list[Slot]
    icon: list[Icon]

    def __init__(
        self,
        name: str,
        cost: int | None = None,
        slot: list[Slot] = [],
        icon: list[Icon] = [],
    ):
        super().__init__(name)
        self.type = CardType.Asset
        self.cost = cost
        self.slot = slot
        self.icon = icon


class Asset:
    card: AssetCard
    area: AreaInPlay

    def __init__(self, card: AssetCard, area: AreaInPlay):
        self.card = card
        self.area = area
