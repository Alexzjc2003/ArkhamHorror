from __future__ import annotations

import inspect
from card import AbilityType
from event.event_type import EventType
from .event_listener import EventListener, Handle

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from event.event import PlayerAlreadyDrawEvent


class CardListener(EventListener):
    @Handle(EventType.PlayerAlreadyDraw)
    def onCardDrawn(self, event: PlayerAlreadyDrawEvent):
        card = event.card

        for c in card:
            for name, method in inspect.getmembers(c, inspect.ismethod):
                if (
                    hasattr(method, "_ability_type")
                    and getattr(method, "_ability_type") == AbilityType.Relevation
                ):
                    method()
