from game import Game
from .investigation_phase import InvestigationPhase
from .mythos_phase import MythosPhase


class Round:
  num:int

  def __init__(self, num:int):
    self.num = num

    if num != 1:
      MythosPhase(self)

    InvestigationPhase(self, Game.getInvestigators())
    ...