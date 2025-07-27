from __future__ import annotations
from action.action import PlaceDoom
from action.player_action import DrawAction
from event.event import (
    MythosPhaseEndEvent,
    MythosPhaseStartEvent,
    PlayerWindowEvent,
)
from game import Game

from player_window import PlayerWindow
from .phase import Phase

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .round import Round


class MythosPhase(Phase):
    def __init__(self, round: Round):
        super().__init__(round)

    def __call__(self):
        # 1.1 Mythos phase start
        Game.triggerEvent(MythosPhaseStartEvent("myt phase start", self))

        # 1.2 Place doom on agenda
        PlaceDoom(Game.currentAgenda())

        # 1.3 Check doom threshold

        # check if the agenda should advance
        if Game.getDoomCount() >= Game.currentAgenda().doomThreshold:
            Game.getAgenda().advance()

        # 1.4 Each player draw encounter
        for investigator in Game.getInvestigators():
            DrawAction(
                investigator,
                Game._encounter_deck,
            )

        # Player window
        Game.triggerEvent(PlayerWindowEvent("1.4 - 1.5", PlayerWindow(phase=self)))

        # 1.5 Mythos phase end
        Game.triggerEvent(MythosPhaseEndEvent("myt phase end", self))
