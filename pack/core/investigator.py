from __future__ import annotations
from re import L

# from typing import TYPE_CHECKING

from ability import *
from action.action import DiscoverClue
from asset import AssetCard
from card import *
from enemy import Enemy
from event.event import AlreadyDealDamageHorrorEvent
from event.select_target import SelectTargetEvent
from investigator import InvestigatorCard


class RolandBanks(InvestigatorCard, EventListener):
    use: int

    def __init__(self, player: Player):
        super().__init__("Roland Banks", 9, 5, [3, 3, 4, 2], player)
        self.traits = ["Agency", "Detective"]

        self.use = 1

    @Triggered()
    @Handle(EventType.AlreadyDealDamageHorror)
    def onEnemyDefeated(self, event: AlreadyDealDamageHorrorEvent):
        if self.use == 0:
            return
        if event.by == self and isinstance(event.target, Enemy) and event.isFatal:
            DiscoverClue(self.owner.investigator, 1, self.owner.investigator.location)

    @Handle(EventType.RoundEnd)
    def upkeep(self):
        self.use = 1


class Roland_s_38Special(AssetCard, EventListener):
    def __init__(self):
        AssetCard.__init__(
            self,
            "Roland's .38 Special",
            3,
            [Slot.Hand],
            [Icon.Combat, Icon.Agility, Icon.Wild],
        )
        self.traits = ["Item", "Weapon", "Firearm"]

    @Triggered()
    def fight(self):
        # selectTarget = SelectTargetEvent(f"fight with {self.name}", )
        
        
        return



