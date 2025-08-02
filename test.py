from __future__ import annotations
from agenda import Agenda, AgendaCard
from chaos.chaos_bag import ChaosBag
from chaos.chaos_token import ChaosTokenNum, ChaosTokenSym, ChaosTokenType
from event.select_target import SelectTargetEvent
from game import Game
from investigator import Investigator
from listener.card_listener import CardListener
from listener.dumb_listener import DumbListener
from listener.target_selector import TargetSelector
from pack.core.encounter import AncientEvils
from pack.core.investigator import RolandBanks
from phase.round import Round
from player import Player
from scenario import Scenario, ScenarioRef


class AgendaCard1(AgendaCard):

    def __init__(self):
        super().__init__("AgendaCard1", 3)

    def flip(self) -> AgendaCard:
        ev = SelectTargetEvent(
            "Agenda1 select",
            {"option1": "info1", "option2": None, "option3": "info3"},
            amount=1,
            prompt="Agenda1 flipped",
        )
        Game.triggerEvent(ev)

        print(ev.target)
        return AgendaCard1()


class SimpleAgenda(Agenda):
    def __init__(self):
        super().__init__()
        self.deck.putOnBottom(AgendaCard1().setOwner(Game._encounter_deck))


if __name__ == "__main__":

    # pre-game setup
    Game.registerListener(TargetSelector())
    Game.registerListener(CardListener())
    Game.registerListener(DumbListener())

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
    Game._chaos_bag = ChaosBag()

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
    # Game._chaos_bag.add(ChaosTokenSym(ChaosTokenType.ElderSign))
    # Game._chaos_bag.add(ChaosTokenSym(ChaosTokenType.AutoFail))

    # 7. Collect starting resources
    p1.investigator.token.resource = 5

    # 8. Draw opening hands

    # 9 & 10. Scenario introduction & setup

    Game._scenario = Scenario(ScenarioRef({}, {}))

    # 11. Set agenda deck
    Game.useAgenda(SimpleAgenda())
    Game._encounter_deck.add(AncientEvils().setOwner(Game._encounter_deck))

    # 12. Set act deck

    # 13. Scenario reference


    # .reference take 3 rounds
    for i in range(0, 5):
        Game._round = Round(i + 1)
        Game._round()
        ...

    pass
