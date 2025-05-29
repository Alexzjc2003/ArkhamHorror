from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
  from .round import Round

class Phase: 
  round:Round

  def __init__(self, round: Round):
    self.round = round
    pass