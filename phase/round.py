from event.event import RoundStartEvent
from game import Game
from phase.phase import Phase
from .investigation_phase import InvestigationPhase
from .mythos_phase import MythosPhase


class Round:
    num: int
    phase: Phase

    def __init__(self, num: int):
        self.num = num

    def __call__(self):

        Game.triggerEvent(RoundStartEvent("round start", self))

        if self.num != 1:
            self.phase = MythosPhase(self)
            self.phase()

        self.phase = InvestigationPhase(self, Game.getInvestigators())
        self.phase()
        ...
