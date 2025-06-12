from agenda import Agenda
from card import Card
from event.event import AlreadyPlaceDoomEvent, WouldPlaceDoomEvent
from game import Game


class GameAction:
    name: str

    def __init__(self, name: str):
        self.name = name


class PlaceDoom(GameAction):
    target: Card
    count: int

    def __init__(self, target: Card | Agenda, count: int = 1):
        if isinstance(target, Card):
            self.target = target
        elif isinstance(target, Agenda):
            self.target = target.currentAgenda
        else:
            raise TypeError("Invalid target to place doom")
        self.count = count

        wouldPlaceDoom = WouldPlaceDoomEvent(
            "would place doom", self.target, self.count
        )
        Game.triggerEvent(wouldPlaceDoom)

        if wouldPlaceDoom.isCancelled:
            return

        self.target = wouldPlaceDoom.target
        self.count = wouldPlaceDoom.count

        self.target.token.doom += self.count

        Game.triggerEvent(AlreadyPlaceDoomEvent("doom placed", self.target))
