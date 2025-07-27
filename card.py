from __future__ import annotations

from enum import Enum
from typing import TYPE_CHECKING, Self


if TYPE_CHECKING:
    from encounter import EncounterDeck
    from player import Player


class Slot(Enum):
    Accessory = 0
    Body = 1
    Ally = 2
    Hand = 3
    Arcane = 4
    Tarrot = 5


class Icon(Enum):
    Willpower = 0
    Intellect = 1
    Combat = 2
    Agility = 3
    Wild = 4


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


class CardType(Enum):
    Agenda = "Agenda"
    Asset = "Asset"
    Enemy = "Enemy"
    Investigator = "Investigator"
    Treachery = "Treachery"


class Card:
    name: str
    owner: Player | EncounterDeck | None
    type: CardType
    token: Token
    traits: list[str]

    def __init__(
        self,
        name: str,
        owner: Player | EncounterDeck | None = None,
        token: Token = Token(),
    ):
        self.name = name
        self.owner = owner
        self.token = token
        self.traits = []

    def setOwner(self, owner: Player | EncounterDeck) -> Self:
        self.owner = owner
        return self
