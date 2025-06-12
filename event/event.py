from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from card import Card
    from deck import Deck
    from investigator import Investigator
    from phase import InvestigationPhase, Turn
    from phase.mythos_phase import MythosPhase
    from phase.round import Round
    from player_window import PlayerWindow
    from agenda import Agenda

from .event_type import EventType


class Event:
    name: str
    type: EventType

    cancelled: bool

    def __init__(self, name: str, type: EventType):
        self.name = name
        self.type = type

        self.cancelled = False

    def setCancelled(self):
        self.cancelled = True

    @property
    def isCancelled(self) -> bool:
        return self.cancelled


class InvestigationPhaseStartEvent(Event):
    phase: InvestigationPhase

    def __init__(self, name: str, phase: InvestigationPhase):
        super().__init__(name, EventType.InvestigationPhaseStart)
        self.phase = phase


class InvestigationPhaseEndEvent(Event):
    phase: InvestigationPhase

    def __init__(self, name: str, phase: InvestigationPhase):
        super().__init__(name, EventType.InvestigationPhaseEnd)
        self.phase = phase


class InvestigatorTurnStartEvent(Event):
    turn: Turn
    investigator: Investigator

    def __init__(self, name: str, turn: Turn):
        super().__init__(name, EventType.InvestigatorTurnStart)
        self.turn = turn
        self.investigator = turn.investigator


class InvestigatorTurnEndEvent(Event):
    turn: Turn
    investigator: Investigator

    def __init__(self, name: str, turn: Turn):
        super().__init__(name, EventType.InvestigatorTurnEnd)
        self.turn = turn
        self.investigator = turn.investigator


class PlayerWindowEvent(Event):
    window: PlayerWindow

    def __init__(self, name: str, window: PlayerWindow):
        super().__init__(name, EventType.PlayerWindow)
        self.window = window


class RoundStartEvent(Event):
    round: Round

    def __init__(self, name: str, round: Round):
        super().__init__(name, EventType.RoundStart)
        self.round = round


class MythosPhaseStartEvent(Event):
    phase: MythosPhase

    def __init__(self, name: str, phase: MythosPhase):
        super().__init__(name, EventType.MythosPhaseStart)
        self.phase = phase


class MythosPhaseEndEvent(Event):
    phase: MythosPhase

    def __init__(self, name: str, phase: MythosPhase):
        super().__init__(name, EventType.MythosPhaseEnd)
        self.phase = phase


class PlayerWouldDrawEvent(Event):
    investigator: Investigator
    deck: Deck
    count: int

    def __init__(self, name: str, investigator: Investigator, deck: Deck, count: int):
        super().__init__(name, EventType.PlayerWouldDraw)
        self.investigator = investigator
        self.deck = deck
        self.count = count


class PlayerAlreadyDrawEvent(Event):
    investigator: Investigator
    deck: Deck
    card: list[Card]

    def __init__(
        self, name: str, investigator: Investigator, deck: Deck, card: list[Card]
    ):
        super().__init__(name, EventType.PlayerAlreadyDraw)
        self.investigator = investigator
        self.deck = deck
        self.card = card


class WouldPlaceDoomEvent(Event):
    target: Card
    count: int

    def __init__(self, name: str, target: Card, count: int):
        super().__init__(name, EventType.WouldPlaceDoom)
        self.count = count
        self.target = target


class AlreadyPlaceDoomEvent(Event):
    target: Card

    def __init__(self, name: str, target: Card):
        super().__init__(name, EventType.AlreadyPlaceDoom)
        self.target = target
