from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
  from investigator import Investigator
  from phase import InvestigationPhase, Turn

from .event_type import EventType

class Event:
  name:str
  type:EventType

  def __init__(self, name:str, type:EventType):
    self.name = name
    self.type = type


class InvestigationPhaseStartEvent(Event):
  phase:InvestigationPhase
  def __init__(self, name:str, phase:InvestigationPhase):
    super().__init__(name, EventType.InvestigationPhaseStart)
    self.phase = phase


class InvestigationPhaseEndEvent(Event):
  phase:InvestigationPhase
  def __init__(self, name:str, phase:InvestigationPhase):
    super().__init__(name, EventType.InvestigationPhaseEnd)
    self.phase = phase


class InvestigatorTurnStartEvent(Event):
  turn:Turn
  investigator:Investigator
  def __init__(self, name:str, turn:Turn):
    super().__init__(name, EventType.InvestigatorTurnStart)
    self.turn = turn
    self.investigator = turn.investigator


class InvestigatorTurnEndEvent(Event):
  turn:Turn
  investigator:Investigator
  def __init__(self, name:str, turn:Turn):
    super().__init__(name, EventType.InvestigatorTurnEnd)
    self.turn = turn
    self.investigator = turn.investigator