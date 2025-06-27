from collections import defaultdict
import inspect

from agenda import Agenda, AgendaCard
from encounter import EncounterDeck
from event import Event, EventType
from event.event_bus import EventBus
from investigator import Investigator
from listener import EventListener


class Game:

    _event_bus: EventBus = EventBus()
    _investigators: list[Investigator] = []

    _agenda: Agenda

    _encounter_deck = EncounterDeck()

    @classmethod
    def triggerEvent(cls, event: Event):
        cls._event_bus.trigger(event)

    @classmethod
    def registerListener(cls, listener: EventListener):
        cls._event_bus.register(listener)

    @classmethod
    def unregisterListener(cls, listener: EventListener):
        cls._event_bus.unregister(listener)

    @classmethod
    def addInvestigator(cls, investigator: Investigator):
        cls._investigators.append(investigator)

    @classmethod
    def getInvestigators(cls):
        return cls._investigators

    @classmethod
    def makeEncounter(cls):
        # cls._encounter_deck.
        ...

    @classmethod
    def useAgenda(cls, agenda: Agenda):
        cls._agenda = agenda

    @classmethod
    def getAgenda(cls) -> Agenda:
        return cls._agenda

    @classmethod
    def currentAgenda(cls) -> AgendaCard:
        return cls._agenda.deck.getTop()

    @classmethod
    def getDoomCount(cls) -> int:
        # TODO
        # Now count only on agenda
        return cls._agenda.currentAgenda.token.doom
