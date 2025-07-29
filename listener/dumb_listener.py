from .event_listener import EventListener, Handle
from event import EventType
from event.event import (
    AlreadyRevealChaosTokenEvent,
    InvestigationPhaseEndEvent,
    InvestigationPhaseStartEvent,
    InvestigatorTurnEndEvent,
    InvestigatorTurnStartEvent,
    MythosPhaseEndEvent,
    MythosPhaseStartEvent,
    PlayerAlreadyDrawEvent,
    RoundStartEvent,
)


class DumbListener(EventListener):
    @Handle(EventType.InvestigationPhaseStart)
    def onInvestigationPhaseStart(self, event: InvestigationPhaseStartEvent):
        print("Investigation phase starts.")

    @Handle(EventType.InvestigationPhaseEnd)
    def onInvestigationPhaseEnd(self, event: InvestigationPhaseEndEvent):
        print("Investigation phase ends.")

    @Handle(EventType.InvestigatorTurnStart)
    def onInvestigatorTurnStart(self, event: InvestigatorTurnStartEvent):
        print(f"{event.investigator.name} turn starts.")

    @Handle(EventType.InvestigatorTurnEnd)
    def onInvestigatorTurnEnd(self, event: InvestigatorTurnEndEvent):
        print(f"{event.investigator.name} turn ends.")

    @Handle(EventType.PlayerAlreadyDraw)
    def onPlayerAlreadyDraw(self, event: PlayerAlreadyDrawEvent):
        print(f"{event.investigator.name} draws [{[c.name for c in event.card]}]")

    @Handle(EventType.MythosPhaseStart)
    def onMythosPhaseStart(self, event: MythosPhaseStartEvent):
        print("Mythos phase starts.")

    @Handle(EventType.MythosPhaseEnd)
    def onMythosPhaseEnd(self, event: MythosPhaseEndEvent):
        print("Mythos phase ends.")

    @Handle(EventType.RoundStart)
    def onRoundStart(self, event: RoundStartEvent):
        print(f"Round {event.round.num} starts.")

    @Handle(EventType.AlreadyRevealChaosToken)
    def onRevealChaosToken(self, event: AlreadyRevealChaosTokenEvent):
        print(f"{event.investigator.name} reveals {str(event.token)}")
