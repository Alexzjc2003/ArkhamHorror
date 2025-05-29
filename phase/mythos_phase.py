from __future__ import annotations
from event.event import DoomPlacedOnAgendaEvent, MythosPhaseEndEvent, MythosPhaseStartEvent, PlayerWindowEvent
from game import Game

from player_window import PlayerWindow
from .phase import Phase

from typing import TYPE_CHECKING
if TYPE_CHECKING:
  from .round import Round

class MythosPhase(Phase):
  def __init__(self, round:Round):
    
    # 1.1 Mythos phase start
    Game.triggerEvent(MythosPhaseStartEvent("myt phase start", self))
    
    # 1.2 Place doom on agenda
    # Game.triggerEvent(DoomPlacedOnAgendaEvent(...))

    # 1.3 Check doom threshold

    # 1.4 Each player draw encounter

    # Player window
    Game.triggerEvent(PlayerWindowEvent("1.4 - 1.5", PlayerWindow(phase=self)))

    # 1.5 Mythos phase end
    Game.triggerEvent(MythosPhaseEndEvent("myt phase end", self))

