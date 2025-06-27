from ability import Relevation
from action.action import PlaceDoom
from card import *
from game import Game
from encounter import EncounterDeck


class AncientEvils(Card):
    def __init__(self):
        super().__init__("Ancient Evils")

    @Relevation
    def putDoomOnAgenda(self):
        PlaceDoom(Game.getAgenda())

        # check if the agenda should advance
        if Game.getDoomCount() >= Game.currentAgenda().doomThreshold:
            Game.getAgenda().advance()

        if isinstance(self.owner, EncounterDeck):
            self.owner.discard(self)
