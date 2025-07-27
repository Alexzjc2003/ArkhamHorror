from __future__ import annotations

from event.event import PlayerWindowEvent
from game import Game

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from phase import Phase
    from phase.investigation_phase import InvestigationPhase


class PlayerWindow:
    phase: Phase
    # turn: Turn | None

    def __init__(self, phase: Phase):

        self.phase = phase

        Game.triggerEvent((PlayerWindowEvent("player window", self)))

        ...
