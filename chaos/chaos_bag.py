from __future__ import annotations

import random
from typing import TYPE_CHECKING, Self

from event.event import (
    AlreadyRevealChaosTokenEvent,
    WouldRevealChaosTokenEvent,
)
from game import Game

from .chaos_token import ChaosToken, ChaosTokenType


class ChaosBag:
    token: list[ChaosToken]

    def __init__(self):
        self.token = []

    def add(self, token: ChaosToken) -> Self:
        self.token.append(token)
        return self

    def remove(self, token: int | ChaosTokenType):
        self.token.remove(token)  # type: ignore

    def reveal(self, amount: int) -> list[ChaosToken]:
        wouldRevealChaosToken = WouldRevealChaosTokenEvent(
            "would reveal chaos token", amount
        )
        Game.triggerEvent(wouldRevealChaosToken)

        if wouldRevealChaosToken.isCancelled or wouldRevealChaosToken.amount == 0:
            return []

        amount = (
            wouldRevealChaosToken.amount
            if wouldRevealChaosToken.amount < len(self.token)
            else len(self.token)
        )

        token = random.sample(self.token, amount)

        Game.triggerEvent(
            AlreadyRevealChaosTokenEvent("already reveal chaos token", token)
        )

        return token
