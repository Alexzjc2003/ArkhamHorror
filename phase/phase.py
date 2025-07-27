from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .round import Round


class Phase(ABC):
    round: Round

    def __init__(self, round: Round):
        self.round = round
        pass

    @abstractmethod
    def __call__(self): ...
