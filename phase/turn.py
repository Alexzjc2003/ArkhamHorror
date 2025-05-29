from event.event import InvestigatorTurnEndEvent, InvestigatorTurnStartEvent
from game import Game
from investigator import Investigator

class Turn():
  investigator:Investigator

  shouldEnd:bool

  
  def __init__(self, investigator: Investigator):
    self.investigator = investigator
    self.shouldEnd = False

    # 2.2 turn start
    Game.triggerEvent(InvestigatorTurnStartEvent("inv turn start", self))

    while not self.shouldEnd:
      # TODO: Player Window
      ...
      # 2.2.1 take possible actions
      investigator.hello()
      self.shouldEnd = True 
      pass
    
    # 2.2.2 turn end
    Game.triggerEvent(InvestigatorTurnEndEvent("inv turn end", self))