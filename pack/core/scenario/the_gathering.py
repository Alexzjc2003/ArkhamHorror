from __future__ import annotations

from typing import TYPE_CHECKING, Callable
from chaos.chaos_token import ChaosToken, ChaosTokenType
from scenario import Scenario, ScenarioRef

if TYPE_CHECKING:
    from investigator import Investigator


class TheGathering(Scenario):
    def __init__(self, reference: ScenarioRef):
        super().__init__(reference)


class TheGatheringRefES(ScenarioRef):
    def __init__(self):
        super().__init__({}, {})

        def _calc_ghoul_count_(investigator: Investigator) -> int:
            location = investigator.location
            
            return 0

        self.modifier[ChaosTokenType.Skull] = lambda skillTest: _calc_ghoul_count_(
            skillTest.investigator
        )
