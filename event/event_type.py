from enum import Enum

class EventType(Enum):
  
  PlayerWindow = "PlayerWindow"

  RoundStart = "RoundStart"

  MythosPhaseStart = "MythosPhaseStart"
  MythosPhaseEnd = "MythosPhaseEnd"
  DoomPlacedOnAgenda = "DoomPlacedOnAgenda"
  PlayerWouldDraw = "PlayerWouldDraw"




  InvestigationPhaseStart = "InvestigationPhaseStart"
  InvestigationPhaseEnd = "InvestigationPhaseEnd"
  
  InvestigatorTurnStart = "InvestigatorTurnStart"
  InvestigatorTurnEnd = "InvestigatorTurnEnd"