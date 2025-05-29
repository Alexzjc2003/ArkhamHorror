from event.event import InvestigationPhaseEndEvent, InvestigationPhaseStartEvent
from game import Game
from phase import Turn
from .phase import Phase
from investigator import Investigator

class InvestigationPhase(Phase):

  def __init__(self, investigators:list[Investigator]):

    # 2.1 phase start
    Game.triggerEvent(InvestigationPhaseStartEvent("inv phase start", self))

    # TODO: Player Window

    # 2.2 turns of invs
    for inv in investigators:
      turn = Turn(inv)  
    pass

    # 2.3 phase end
    Game.triggerEvent(InvestigationPhaseEndEvent("inv phase end", self))

  

