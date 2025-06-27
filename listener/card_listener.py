from __future__ import annotations

import inspect
from ability import AbilityType
from event.event import AlreadyGetOutOfPlayEvent
from event.event_type import EventType
from game import Game
from .event_listener import EventListener, Handle

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from event.event import PlayerAlreadyDrawEvent
    from event.event import AlreadyGetInPlayEvent


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

    @Handle(EventType.AlreadyGetInPlay)
    def onCardGetInPlay(self, event: AlreadyGetInPlayEvent):
        card = event.card
        for name, method in inspect.getmembers(card, inspect.ismethod):
            if (
                hasattr(method, "_ability_type")
                and getattr(method, "_ablility_type") == AbilityType.Triggered
            ):
                if isinstance(card, EventListener):
                    Game.registerListener(
                        card
                    )  # A card with triggered ability is supposed to be an EventListener

    @Handle(EventType.AlreadyGetOutOfPlay)
    def onCardGetOutOfPlay(self, event: AlreadyGetOutOfPlayEvent):
        card = event.card
        for name, method in inspect.getmembers(card, inspect.ismethod):
            if (
                hasattr(method, "_ablility_type")
                and getattr(method, "_ability_type") == AbilityType.Triggered
            ):
                if isinstance(card, EventListener):
                    Game.unregisterListener(
                        card
                    )  # A card with triggered ability is supposed to be an EventListener
