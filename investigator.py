from __future__ import annotations

from typing import TYPE_CHECKING

from card import Card, CardType, Icon
from element import Damageable, Entity
from skill_test import SkillTest

if TYPE_CHECKING:
    from location import Location
    from player import Player


class InvestigatorCard(Card):
    owner: Player
    health: int
    sanity: int
    skill: list[int]

    def __init__(
        self, name: str, health: int, sanity: int, skill: list[int], owner: Player
    ):
        super().__init__(name, owner)
        self.health = health
        self.sanity = sanity
        self.type = CardType.Investigator
        self.skill = skill


class Investigator(Damageable, Entity):
    card: InvestigatorCard
    name: str
    location: Location

    def __init__(self, name: str, card: InvestigatorCard):
        Damageable.__init__(self, card.token, card.health, card.sanity)
        self.name = name
        self.card = card

    def hello(self):
        st = SkillTest(self, Icon.Combat, 3)
        st(lambda: print(f"{st.isSuccess}"))

        print(f"Hello, I am {self.name}.")
