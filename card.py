from __future__ import annotations

from enum import Enum
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from deck import Deck


class AbilityType(Enum):
    Constant = "Constant"
    Forced = "Forced"
    Relevation = "Relevation"
    Triggered = "Triggered"


class Token:
    resource: int
    doom: int
    clue: int
    damage: int
    horror: int

    def __init__(
        self,
        resource: int = 0,
        doom: int = 0,
        clue: int = 0,
        damage: int = 0,
        horror: int = 0,
    ):
        self.resource = resource
        self.doom = doom
        self.clue = clue
        self.damage = damage
        self.horror = horror

    def clear(self):
        self.resource = 0
        self.doom = 0
        self.clue = 0
        self.damage = 0
        self.horror = 0


class Card:
    name: str
    token: Token
    deck: Deck | None

    def __init__(
        self, name: str = "", token: Token = Token(), deck: Deck | None = None
    ):
        self.name = name
        self.token = token
        self.deck = deck


def Ability(type: AbilityType):
    def decorator(func):
        func._ability_type = type
        return func

    return decorator
