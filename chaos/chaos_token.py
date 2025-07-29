from __future__ import annotations
from typing import TYPE_CHECKING

from abc import ABC, abstractmethod
from enum import Enum

from game import Game

if TYPE_CHECKING:
    from scenario import ScenarioRef


class ChaosTokenType(Enum):
    Number = 0
    Skull = 1
    Cultist = 2
    ElderThing = 3
    Tablet = 4
    AutoFail = 10
    ElderSign = 11


class ChaosToken(ABC):
    type: ChaosTokenType

    def __init__(self, type: ChaosTokenType):
        self.type = type

    @property
    @abstractmethod
    def modifier(self) -> int: ...

    @abstractmethod
    def resolve(self, tokens: list[ChaosToken]): ...

    @abstractmethod
    def __eq__(self, value: object) -> bool: ...

    @abstractmethod
    def __repr__(self) -> str: ...


class ChaosTokenNum(ChaosToken):
    _value: int

    def __init__(self, value: int):
        super().__init__(ChaosTokenType.Number)
        self._value = value

    @property
    def modifier(self) -> int:
        return self._value

    def resolve(self, tokens: list[ChaosToken]): ...

    def __eq__(self, value: object) -> bool:
        return (
            isinstance(value, ChaosTokenNum)
            and value._value == self._value
            or isinstance(value, int)
            and value == self._value
        )

    def __repr__(self) -> str:
        s = f"{self.modifier}" if self.modifier < 0 else f"+{self.modifier}"
        return f"ChaosTokenNum({s})"

    def __str__(self) -> str:
        return self.__repr__()


class ChaosTokenSym(ChaosToken):
    def __init__(self, type: ChaosTokenType):
        super().__init__(type)

    @property
    def modifier(self) -> int:
        m = Game._scenario.reference.modifier[self.type]
        return m if isinstance(m, int) else m()

    def resolve(self, tokens: list[ChaosToken]):
        if 1 <= self.type.value <= 4:
            return Game._scenario.reference.effect[self.type](tokens)
        else:
            raise NotImplementedError()

    def __eq__(self, value: object) -> bool:
        return (
            isinstance(value, ChaosTokenSym)
            and value.type == self.type
            or isinstance(value, ChaosTokenType)
            and value == self.type
        )

    def __repr__(self) -> str:
        s = f"{self.modifier}" if self.modifier < 0 else f"+{self.modifier}"
        return f"ChaosTokenSym[{self.type.name}]({s})"

    def __str__(self) -> str:
        return self.__repr__()