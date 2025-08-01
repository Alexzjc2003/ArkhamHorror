from chaos.chaos_token import ChaosTokenNum, ChaosTokenSym, ChaosTokenType
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

    # pre-game setup
    Game.registerListener(DumbListener())
    Game.registerListener(CardListener())

    # game setup
    p1 = Player()

    # 1. Choose investigators

    p1.investigator = Investigator("Roland Banks", RolandBanks(p1))
    p1.investigator.card.setOwner(p1)
    Game.addInvestigator(p1.investigator)

    # 2. Take trauma damage/horror
    # 3. Choose lead investigator

    # 4. Assemble and shuffle investigator decks

    # 5. Assemble token pool
    # 6. Assemble the chaos bag
    #    +1, 0, -1, -1, -2, -2, -3, -4,
    #    sku, cul, elt, tab, els, auf
    Game._chaos_bag.add(ChaosTokenNum(+1))
    Game._chaos_bag.add(ChaosTokenNum(0))
    Game._chaos_bag.add(ChaosTokenNum(-1))
    Game._chaos_bag.add(ChaosTokenNum(-1))
    Game._chaos_bag.add(ChaosTokenNum(-2))
    Game._chaos_bag.add(ChaosTokenNum(-2))
    Game._chaos_bag.add(ChaosTokenNum(-3))
    Game._chaos_bag.add(ChaosTokenNum(-4))

    Game._chaos_bag.add(ChaosTokenSym(ChaosTokenType.Skull))
    Game._chaos_bag.add(ChaosTokenSym(ChaosTokenType.Cultist))
    Game._chaos_bag.add(ChaosTokenSym(ChaosTokenType.ElderThing))
    Game._chaos_bag.add(ChaosTokenSym(ChaosTokenType.Tablet))
    Game._chaos_bag.add(ChaosTokenSym(ChaosTokenType.ElderSign))
    Game._chaos_bag.add(ChaosTokenSym(ChaosTokenType.AutoFail))

    # 7. Collect starting resources
    p1.investigator.token.resource = 5

    # 8. Draw opening hands

    # 9 & 10. Scenario introduction & setup

    # 11. Set agenda deck
    Game.useAgenda(SimpleAgenda())
    Game._encounter_deck.add(AncientEvils().setOwner(Game._encounter_deck))

    # 12. Set act deck

    # 13. Scenario reference

    # take 3 rounds
    for i in range(0, 3):
        Game._round = Round(i + 1)
        Game._round()
        ...
