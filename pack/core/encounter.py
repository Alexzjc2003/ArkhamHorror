from action.action import PlaceDoom
from card import *
from event.event import WouldPlaceDoomEvent
from game import Game


class CardAncientEvils(Card):
    def __init__(self):
        super().__init__("Ancient Evils")

    @Ability(AbilityType.Relevation)
    def putDoomOnAgenda(self):
        # Game.triggerEvent(WouldPlaceDoomEvent("ancient evils", Game.getAgenda()))

        PlaceDoom(Game.getAgenda())

        # check if the agenda should advance
        if Game.getDoomCount() >= Game.currentAgenda().doomThreshold:
            Game.getAgenda().advance()

        if not self.deck is None:
            self.deck.discard(self)
