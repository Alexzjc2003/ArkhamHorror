from __future__ import annotations

from typing import TYPE_CHECKING, Callable

from event.event import CalcModifierEvent
from game import Game
from player_window import PlayerWindow

if TYPE_CHECKING:
    from card import Icon
    from investigator import Investigator


class SkillTest:
    investigator: Investigator
    skill: Icon
    difficulty: int
    modifier: int
    isSuccess: bool

    def __init__(self, investigator: Investigator, skill: Icon, difficulty: int):
        self.investigator = investigator
        self.skill = skill
        self.difficulty = difficulty
        self.modifier = 0
        self.isSuccess = False

        pass

    def __call__(self, result: Callable, *args):
        # ST.1 determine skill of test

        # player window
        PlayerWindow(Game._round.phase)

        # ST.2 commit cards to test

        # player window
        PlayerWindow(Game._round.phase)

        # ST.3 reveal chaos token
        tokens = Game._chaos_bag.reveal(self.investigator, 1)

        # ST.4 apply chaos symbol effect(s)
        while len(tokens) > 0:
            t = tokens.pop(0)
            self.modifier += t.modifier(self)
            t.resolve(self)
        # ST.5 determine modified skill value (all modifiers: tokens,
        # card effects in play, cards committed...)

        baseValue = self.investigator.card.skill[self.skill.value]
        calcModifier = CalcModifierEvent(
            "st.5 determine modified skill value", self.skill, True
        )
        Game.triggerEvent(calcModifier)
        self.modifier += baseValue + calcModifier.modifier
        if self.modifier < 0:
            self.modifier = 0

        # ST.6 determine success/failure
        self.isSuccess = self.modifier >= self.difficulty

        # ST.7 apply skill test result
        result(*args)

        # ST.8 end
