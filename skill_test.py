from __future__ import annotations

from typing import TYPE_CHECKING, Callable

from event.event import CalcModifierEvent
from game import Game
from player_window import PlayerWindow

if TYPE_CHECKING:
    from card import Icon
    from player import Player


class SkillTest:
    player: Player
    skill: Icon
    difficulty: int
    modifier: int
    isSuccess: bool

    def __init__(self, player: Player, skill: Icon, difficulty: int):
        self.player = player
        self.skill = skill
        self.difficulty = difficulty
        self.modifier = 0
        self.isSuccess = False

        pass

    def __call__(self, result: Callable):
        # ST.1 determine skill of test

        # player window
        PlayerWindow(Game._round.phase)

        # ST.2 commit cards to test

        # player window
        PlayerWindow(Game._round.phase)

        # ST.3 reveal chaos token
        tokens = Game._chaos_bag.reveal(1)

        # ST.4 apply chaos symbol effect(s)
        while len(tokens) > 0:
            t = tokens.pop(0)
            self.modifier += t.modifier
            t.resolve(
                tokens
            )  # that is, the list does not contain the token being resolved

        # ST.5 determine modified skill value (all modifiers: tokens,
        # card effects in play, cards committed...)

        baseValue = self.player.investigator.card.skill[self.skill.value]
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

        # ST.8 end
