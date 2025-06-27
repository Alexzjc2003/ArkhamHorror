from __future__ import annotations
from typing import Literal

from card import Token


class InvalidDamageException(Exception):
    def __init__(self, damageable: Damageable):
        super().__init__(f"{damageable}")


class Damageable:
    _health: int | None
    _sanity: int | None

    token: Token

    def __init__(self, token: Token, health: int | None = 0, sanity: int | None = 0):
        self.token = token
        self.health = health
        self.sanity = sanity

    def canTakeDamage(self) -> int | None:
        if self.health is None:
            return None
        else:
            return self.health - self.token.damage

    def canTakeHorror(self) -> int | None:
        if self.sanity is None:
            return None
        else:
            return self.sanity - self.token.horror

    def takeDamage(self, amount: int) -> int:
        can = self.canTakeDamage()
        if can is None:
            raise InvalidDamageException(self)
        else:
            actual = amount if can >= amount else can
            self.token.damage += actual
            return actual

    def takeHorror(self, amount: int) -> int:
        can = self.canTakeHorror()
        if can is None:
            raise InvalidDamageException(self)
        else:
            actual = amount if can >= amount else can
            self.token.horror += actual
            return actual


class Entity:
    type: Literal["Investigator", "Enemy"]

    def __init__(self, type: Literal["Investigator", "Enemy"]):
        self.type = type
