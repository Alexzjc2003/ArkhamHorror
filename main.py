from game import Game
from listener.card_listener import CardListener
from listener.dumb_listener import DumbListener
from investigator import Investigator
from phase.round import Round
from player import Player
from pack.core.encounter import *
from pack.core.investigator import RolandBanks

from agenda import Agenda, AgendaCard


class AgendaCard1(AgendaCard):

    def __init__(self):
        super().__init__("AgendaCard1", 3)

    def flip(self):
        print("Agenda1 flipped")


class AgendaCard2(AgendaCard):
    def __init__(self):
        super().__init__("AgendaCard2", 4)

    def flip(self):
        print("Agenda2 flipped")


class AgendaCard3(AgendaCard):
    def __init__(self):
        super().__init__("AgendaCard3", 5)

    def flip(self):
        print("Agenda3 flipped")


class SimpleAgenda(Agenda):
    def __init__(self):
        super().__init__()
        self.deck.putOnBottom(AgendaCard1().setOwner(Game._encounter_deck))
        self.deck.putOnBottom(AgendaCard2().setOwner(Game._encounter_deck))
        self.deck.putOnBottom(AgendaCard3().setOwner(Game._encounter_deck))


if __name__ == "__main__":
    Game.registerListener(DumbListener())
    Game.registerListener(CardListener())

    p1 = Player()

    p1.investigator = Investigator("Roland Banks", RolandBanks(p1))
    p1.investigator.card.setOwner(p1)

    Game.addInvestigator(p1.investigator)

    Game.useAgenda(SimpleAgenda())

    Game._encounter_deck.add(AncientEvils().setOwner(Game._encounter_deck))

    # take 3 rounds
    for i in range(0, 3):
        Round(i + 1)
        # take_round(i + 1)
        ...
