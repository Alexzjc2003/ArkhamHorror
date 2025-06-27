from __future__ import annotations
from collections import defaultdict
import inspect

from event.event import Event
from event.event_type import EventType
from listener.event_listener import EventListener


class EventBus:
    _handlers: dict[EventType, list] = defaultdict(list)

    def __init__(self):
        pass

    def register(self, listener: EventListener):
        for name, method in inspect.getmembers(listener, inspect.ismethod):
            if hasattr(method, "_event_type"):
                self._handlers[getattr(method, "_event_type")].append(method)

    def unregister(self, listener: EventListener):
        for name, method in inspect.getmembers(listener, inspect.ismethod):
            if hasattr(method, "_event_type"):
                self._handlers[getattr(method, "_event_type")].remove(method)

    def trigger(self, event: Event):
        for func in self._handlers[event.type]:
            func(event)
