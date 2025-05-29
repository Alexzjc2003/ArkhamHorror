from .event_listener import EventListener, Handle 
from event import EventType
from event.event import InvestigationPhaseEndEvent, InvestigationPhaseStartEvent, InvestigatorTurnEndEvent, InvestigatorTurnStartEvent


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