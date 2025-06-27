from __future__ import annotations
from typing import TYPE_CHECKING, Tuple


from card import Card, CardType
from element import Damageable

if TYPE_CHECKING:
    from encounter import EncounterDeck
    from investigator import Investigator


class EnemyCard(Card):
    fight: int
    evade: int
    health: int
    attack: Tuple[int, int]

    def __init__(
        self,
        name,
        owner: Investigator | EncounterDeck,
        fight: int = 0,
        evade: int = 0,
        health: int = 1,
        attack: Tuple[int, int] = (0, 0),
    ):
        super().__init__(name, owner)
        self.type = CardType.Enemy

        self.fight = fight
        self.evade = evade
        self.health = health
        self.attack = attack


class Enemy(Damageable):
    card: EnemyCard

    fight: int
    evade: int
    attack: Tuple[int, int]

    def __init__(self, card: EnemyCard) -> None:
        super().__init__(token=card.token, health=card.health, sanity=None)
        self.card = card
        self.fight = card.fight
        self.evade = card.evade
        self.attack = card.attack

    @property
    def health(self) -> int:
        return self.card.health - self.card.token.damage
