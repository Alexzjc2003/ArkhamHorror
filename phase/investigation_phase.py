from __future__ import annotations

from event.event import (
    InvestigationPhaseEndEvent,
    InvestigationPhaseStartEvent,
    PlayerWindowEvent,
)
from game import Game
import investigator
from .phase import Phase
from .turn import Turn
from player_window import PlayerWindow
from investigator import Investigator

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .round import Round


class InvestigationPhase(Phase):
    investigators: list[Investigator]
    turn: Turn

    def __init__(self, round: Round, investigators: list[Investigator]):
        super().__init__(round)
        self.investigators = investigators

    def __call__(self):
        # 2.1 phase start
        Game.triggerEvent(InvestigationPhaseStartEvent("inv phase start", self))

        # TODO: Player Window
        Game.triggerEvent(PlayerWindowEvent("2.1 - 2.2", PlayerWindow(phase=self)))

        # 2.2 turns of invs
        for inv in self.investigators:
            self.turn = Turn(self, inv)
            self.turn()
        pass

        # 2.3 phase end
        Game.triggerEvent(InvestigationPhaseEndEvent("inv phase end", self))
