from game import Game
from listener.dumb_listener import DumbListener
from phase import InvestigationPhase
from investigator import Investigator
from phase.round import Round

def take_round(num:int):
    Round(num)


if __name__ == "__main__":
    Game.registerListener(DumbListener())
    
    inv1 = Investigator("1")
    inv2 = Investigator("2")
    inv3 = Investigator("3")

    Game.addInvestigator(inv1)
    Game.addInvestigator(inv2)
    Game.addInvestigator(inv3)

    
    # take 3 rounds
    for i in range(0, 3):
        take_round(i+1)    
    
    
    