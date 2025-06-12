from card_builder import CardBuilder
from game import Game
from listener.card_listener import CardListener
from listener.dumb_listener import DumbListener
from investigator import Investigator
from phase.round import Round
from pack.core.encounter import *

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
        builder = CardBuilder()
        self.deck.putOnBottom(builder.build(AgendaCard1, self.deck))
        self.deck.putOnBottom(builder.build(AgendaCard2, self.deck))
        self.deck.putOnBottom(builder.build(AgendaCard3, self.deck))


if __name__ == "__main__":
    Game.registerListener(DumbListener())
    Game.registerListener(CardListener())
    builder = CardBuilder()

    inv1 = Investigator("1")
    inv2 = Investigator("2")
    inv3 = Investigator("3")

    Game.addInvestigator(inv1)
    Game.addInvestigator(inv2)
    Game.addInvestigator(inv3)

    Game.useAgenda(SimpleAgenda())

    Game._encounter_deck.add(builder.build(CardAncientEvils, deck=Game._encounter_deck))

    # take 3 rounds
    for i in range(0, 3):
        Round(i + 1)
        # take_round(i + 1)
        ...
