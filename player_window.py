from __future__ import annotations

from event.event import PlayerWindowEvent
from game import Game

from typing import TYPE_CHECKING
if TYPE_CHECKING:
  from phase import Phase, Turn

class PlayerWindow:
  phase: Phase
  turn: Turn | None

  def __init__(self, phase:Phase, turn:Turn | None=None):

    self.phase = phase
    self.turn  = turn

    Game.triggerEvent((PlayerWindowEvent("player window", self)))
    
    ...