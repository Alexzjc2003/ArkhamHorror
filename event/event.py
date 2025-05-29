from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
  from investigator import Investigator
  from phase.mythos_phase import MythosPhase
  from phase.round import Round
  from player_window import PlayerWindow
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

class PlayerWindowEvent(Event):
  window: PlayerWindow
  def __init__(self, name:str, window:PlayerWindow):
    super().__init__(name, EventType.PlayerWindow)
    self.window = window


class RoundStartEvent(Event):
  round:Round
  def __init__(self, name:str, round:Round):
    super().__init__(name, EventType.RoundStart)
    self.round = round


class MythosPhaseStartEvent(Event):
  phase: MythosPhase
  def __init__(self, name:str, phase:MythosPhase):
    super().__init__(name, EventType.MythosPhaseStart)
    self.phase = phase


class MythosPhaseEndEvent(Event):
  phase:MythosPhase
  def __init__(self, name:str, phase:MythosPhase):
    super().__init__(name, EventType.MythosPhaseEnd)
    self.phase = phase

  
class PlayerWouldDrawEvent(Event):
  # TODO
  ...

class DoomPlacedOnAgendaEvent(Event):
  # TODO
  ...