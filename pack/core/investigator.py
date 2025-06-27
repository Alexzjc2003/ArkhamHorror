from __future__ import annotations

# from typing import TYPE_CHECKING

from action.action import DiscoverClue
from enemy import Enemy
from event.event import AlreadyDealDamageHorrorEvent
from investigator import InvestigatorCard
from card import *
from ability import *


class RolandBanks(InvestigatorCard, EventListener):
    use: int

    def __init__(self, player: Player):
        super().__init__("Roland Banks", 9, 5, player)
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
