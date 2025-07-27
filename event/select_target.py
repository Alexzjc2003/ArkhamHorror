from __future__ import annotations

from .event_type import EventType
from typing import Generic, TypeVar

from .event import Event

TResult = TypeVar("TResult")


class SelectTargetEvent(Event, Generic[TResult]):
    options: dict[TResult, str | None]
    amount: int
    prompt: str | None

    target: TResult | list[TResult]

    def __init__(
        self,
        name: str,
        options: dict[TResult, str | None],
        amount: int = 1,
        prompt: str | None = None,
    ):
        super().__init__(name, EventType.SelectTarget)

        self.options = options
        self.amount = amount
