from __future__ import annotations

from typing import TYPE_CHECKING, cast

from element import Entity
from enemy import Enemy
from investigator import Investigator


class EntityManager:
    entity: dict[str, Entity]

    def __init__(self) -> None:
        self.entity = {}
        pass

    def set(self, entity: Entity, name: str):
        self.entity[name] = entity

    def get(self, name: str) -> Entity:
        # ett = self.entity[name]

        # if ett.type == "Investigator":
        #     return cast(Investigator, ett)
        # if ett.type == "Enemy":
        #     return cast(Enemy, ett)
        return self.entity[name]
    
    # def filter(self, )
