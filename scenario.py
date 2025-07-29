from __future__ import annotations
from typing import TYPE_CHECKING, Callable


if TYPE_CHECKING:
    from chaos.chaos_token import ChaosToken, ChaosTokenType


class ScenarioRef:
    modifier: dict[ChaosTokenType, int | Callable[..., int]]
    effect: dict[ChaosTokenType, Callable[[list[ChaosToken]], None]]

    def __init__(
        self,
        modifier: dict[ChaosTokenType, int | Callable[..., int]],
        effect: dict[ChaosTokenType, Callable[[list[ChaosToken]], None]],
    ):
        self.modifier = modifier
        self.effect = effect
        pass


class Scenario:
    reference: ScenarioRef

    def __init__(self, reference: ScenarioRef):
        self.reference = reference
