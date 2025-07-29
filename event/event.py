from __future__ import annotations

from typing import TYPE_CHECKING, Tuple

from card import Icon

from .event_type import EventType


if TYPE_CHECKING:
    from area import AreaInPlay, AreaOutOfPlay
    from card import Card
    from chaos.chaos_token import ChaosToken
    from deck import Deck
    from element import Damageable
    from investigator import Investigator
    from location import Location
    from phase import InvestigationPhase, Turn
    from phase import InvestigationPhase, Turn
    from phase.mythos_phase import MythosPhase
    from phase.round import Round
    from player_window import PlayerWindow


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


class PlayerActionEvent(Event):
    investigator: Investigator
    turn: Turn

    def __init__(self, name: str, investigator: Investigator, turn: Turn):
        super().__init__(name, EventType.PlayerAction)
        self.investigator = investigator
        self.turn = turn


class RoundStartEvent(Event):
    round: Round

    def __init__(self, name: str, round: Round):
        super().__init__(name, EventType.RoundStart)
        self.round = round


class RoundEndEvent(Event):
    round: Round

    def __init__(self, name: str, round: Round):
        super().__init__(name, EventType.RoundEnd)
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
    amount: int

    def __init__(self, name: str, investigator: Investigator, deck: Deck, amount: int):
        super().__init__(name, EventType.PlayerWouldDraw)
        self.investigator = investigator
        self.deck = deck
        self.amount = amount


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
    amount: int

    def __init__(self, name: str, target: Card, amount: int):
        super().__init__(name, EventType.WouldPlaceDoom)
        self.amount = amount
        self.target = target


class AlreadyPlaceDoomEvent(Event):
    target: Card

    def __init__(self, name: str, target: Card):
        super().__init__(name, EventType.AlreadyPlaceDoom)
        self.target = target


class WouldDealDamageHorrorEvent(Event):
    target: Damageable | Investigator
    by: Card | None
    amount: Tuple[int, int]

    def __init__(
        self,
        name: str,
        target: Damageable | Investigator,
        by: Card | None,
        amount: Tuple[int, int],
    ):
        super().__init__(name, EventType.WouldDealDamageHorror)
        self.target = target
        self.by = by
        self.amount = amount


class AlreadyDealDamageHorrorEvent(Event):
    target: Damageable
    by: Card | None
    amount: Tuple[int, int]
    isFatal: bool

    def __init__(
        self,
        name: str,
        target: Damageable,
        by: Card | None,
        amount: Tuple[int, int],
        fatal: bool,
    ):
        super().__init__(name, EventType.AlreadyDealDamageHorror)
        self.target = target
        self.by = by
        self.amount = amount
        self.isFatal = fatal


class WouldDiscoverClueEvent(Event):
    investigator: Investigator
    amount: int
    location: Location

    def __init__(
        self, name: str, investigator: Investigator, amount: int, location: Location
    ):
        super().__init__(name, EventType.WouldDiscoverClue)
        self.investigator = investigator
        self.amount = amount
        self.location = location


class AlreadyDiscoverClueEvent(Event):
    investigator: Investigator
    amount: int
    location: Location

    def __init__(
        self, name: str, investigator: Investigator, amount: int, location: Location
    ):
        super().__init__(name, EventType.AlreadyDiscoverClue)
        self.investigator = investigator
        self.amount = amount
        self.location = location


class WouldGetInPlayEvent(Event):
    card: Card
    dst: AreaInPlay
    src: AreaOutOfPlay | None

    def __init__(
        self, name: str, card: Card, dst: AreaInPlay, src: AreaOutOfPlay | None = None
    ):
        super().__init__(name, EventType.WouldGetInPlay)
        self.card = card
        self.dst = dst
        self.src = src


class AlreadyGetInPlayEvent(Event):
    card: Card
    dst: AreaInPlay
    src: AreaOutOfPlay | None

    def __init__(
        self, name: str, card: Card, dst: AreaInPlay, src: AreaOutOfPlay | None = None
    ):
        super().__init__(name, EventType.AlreadyGetInPlay)
        self.card = card
        self.dst = dst
        self.src = src


class WouldGetOutOfPlayEvent(Event):
    card: Card
    dst: AreaOutOfPlay
    src: AreaInPlay | None

    def __init__(
        self, name: str, card: Card, dst: AreaOutOfPlay, src: AreaInPlay | None = None
    ):
        super().__init__(name, EventType.WouldGetOutOfPlay)
        self.card = card
        self.dst = dst
        self.src = src


class AlreadyGetOutOfPlayEvent(Event):
    card: Card
    dst: AreaOutOfPlay
    src: AreaInPlay | None

    def __init__(
        self, name: str, card: Card, dst: AreaOutOfPlay, src: AreaInPlay | None = None
    ):
        super().__init__(name, EventType.AlreadyGetOutOfPlay)
        self.card = card
        self.dst = dst
        self.src = src


class WouldRevealChaosTokenEvent(Event):
    investigator: Investigator
    amount: int

    def __init__(self, name: str, investigator: Investigator, amount: int):
        super().__init__(name, EventType.WouldRevealChaosToken)
        self.amount = amount
        self.investigator = investigator


class AlreadyRevealChaosTokenEvent(Event):
    investigator: Investigator
    token: list[ChaosToken]

    def __init__(self, name: str, investigator: Investigator, token: list[ChaosToken]):
        super().__init__(name, EventType.AlreadyRevealChaosToken)
        self.token = token
        self.investigator = investigator


class CalcModifierEvent(Event):
    skill: Icon
    modifier: int
    isSkillTest: bool

    def __init__(self, name: str, skill: Icon, isSkillTest: bool):
        super().__init__(name, EventType.CalcModifier)
        self.skill = skill
        self.isSkillTest = isSkillTest
        self.modifier = 0
