from collections import defaultdict
import inspect

from agenda import Agenda, AgendaCard
from deck import EncounterDeck
from event import Event, EventType
from investigator import Investigator
from listener import EventListener


class Game:

    _handlers: dict[EventType, list] = defaultdict(list)
    _investigators: list[Investigator] = []

    _agenda: Agenda

    _encounter_deck = EncounterDeck()

    @classmethod
    def triggerEvent(cls, event: Event):
        for func in cls._handlers[event.type]:
            func(event)

    @classmethod
    def registerListener(cls, listener: EventListener):
        for name, method in inspect.getmembers(listener, inspect.ismethod):
            if hasattr(method, "_event_type"):
                cls._handlers[getattr(method, "_event_type")].append(method)

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
