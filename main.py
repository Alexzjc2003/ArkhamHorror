from game import Game
from listener.dumb_listener import DumbListener
from phase import InvestigationPhase
from investigator import Investigator

def take_round(num: int):
    print(f"Round {num}:")
    investigationPhase = InvestigationPhase(invs)


if __name__ == "__main__":
    inv1 = Investigator("1")
    inv2 = Investigator("2")
    inv3 = Investigator("3")
    invs = [inv1, inv2, inv3]

    Game.registerListener(DumbListener())
    
    # take 3 rounds
    for i in range(0, 3):
        take_round(i+1)    
    
    
    