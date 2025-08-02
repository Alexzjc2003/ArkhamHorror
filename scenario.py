from __future__ import annotations
from typing import TYPE_CHECKING, Callable


if TYPE_CHECKING:
    from skill_test import SkillTest
    from chaos.chaos_token import ChaosTokenType


class ScenarioRef:
    modifier: dict[ChaosTokenType, Callable[[SkillTest], int]]
    effect: dict[ChaosTokenType, Callable[[SkillTest], None]]

    def __init__(
        self,
        modifier: dict[ChaosTokenType, Callable[[SkillTest], int]],
        effect: dict[ChaosTokenType, Callable[[SkillTest], None]],
    ):
        self.modifier = modifier
        self.effect = effect
        pass


class Scenario:
    reference: ScenarioRef

    def __init__(self, reference: ScenarioRef):
        self.reference = reference
