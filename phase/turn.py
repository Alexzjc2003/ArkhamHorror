from __future__ import annotations

from event.event import (
    InvestigatorTurnEndEvent,
    InvestigatorTurnStartEvent,
    PlayerWindowEvent,
)
from game import Game
from investigator import Investigator
from player_window import PlayerWindow

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .investigation_phase import InvestigationPhase


class Turn:
    phase: InvestigationPhase
    investigator: Investigator

    shouldEnd: bool

    def __init__(self, phase: InvestigationPhase, investigator: Investigator):
        self.phase = phase
        self.investigator = investigator

        self.shouldEnd = False

    def __call__(self):
        # 2.2 turn start
        Game.triggerEvent(InvestigatorTurnStartEvent("inv turn start", self))

        while not self.shouldEnd:
            # TODO: Player Window

            Game.triggerEvent(
                PlayerWindowEvent("2.2 - 2.2.1", PlayerWindow(phase=self.phase))
            )
            ...
            # 2.2.1 take possible actions
            self.investigator.hello()
            self.shouldEnd = True
            pass

        # 2.2.2 turn end
        Game.triggerEvent(InvestigatorTurnEndEvent("inv turn end", self))
