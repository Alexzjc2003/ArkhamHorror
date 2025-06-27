from __future__ import annotations
from abc import ABC, abstractmethod
from enum import Enum

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from card import Card


from event.event_type import EventType
from listener.event_listener import EventListener, Handle


class AbilityType(Enum):
    Constant = "Constant"
    Forced = "Forced"
    Relevation = "Relevation"
    Triggered = "Triggered"


def Ability(type: AbilityType):
    def decorator(func):
        func._ability_type = type
        return func

    return decorator


def Relevation(func):
    return Ability(AbilityType.Relevation)(func)


def Triggered():
    def decorator(func):
        return Ability(AbilityType.Triggered)(func)

    return decorator
