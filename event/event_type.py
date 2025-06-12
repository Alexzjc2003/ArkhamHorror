from enum import Enum


class EventType(Enum):

    PlayerWindow = "PlayerWindow"

    RoundStart = "RoundStart"

    MythosPhaseStart = "MythosPhaseStart"
    MythosPhaseEnd = "MythosPhaseEnd"
    WouldPlaceDoom = "WouldPlaceDoom"
    AlreadyPlaceDoom = "AlreadyPlaceDoom"
    PlayerWouldDraw = "PlayerWouldDraw"
    PlayerAlreadyDraw = "PlayerAlreadyDraw"

    InvestigationPhaseStart = "InvestigationPhaseStart"
    InvestigationPhaseEnd = "InvestigationPhaseEnd"

    InvestigatorTurnStart = "InvestigatorTurnStart"
    InvestigatorTurnEnd = "InvestigatorTurnEnd"
