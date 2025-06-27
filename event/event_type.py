from enum import Enum


class EventType(Enum):

    PlayerWindow = "PlayerWindow"

    RoundStart = "RoundStart"

    MythosPhaseStart = "MythosPhaseStart"
    WouldPlaceDoom = "WouldPlaceDoom"
    AlreadyPlaceDoom = "AlreadyPlaceDoom"
    MythosPhaseEnd = "MythosPhaseEnd"

    InvestigationPhaseStart = "InvestigationPhaseStart"
    InvestigatorTurnStart = "InvestigatorTurnStart"
    InvestigatorTurnEnd = "InvestigatorTurnEnd"
    InvestigationPhaseEnd = "InvestigationPhaseEnd"

    RoundEnd = "RoundEnd"

    PlayerWouldDraw = "PlayerWouldDraw"
    PlayerAlreadyDraw = "PlayerAlreadyDraw"

    WouldDealDamageHorror = "WouldDealDamageHorror"
    AlreadyDealDamageHorror = "AlreadyDealDamageHorror"

    WouldDiscoverClue = "WouldDiscoverClue"
    AlreadyDiscoverClue = "AlreadyDiscoverClue"

    WouldGetInPlay = "WouldGetInPlay"
    AlreadyGetInPlay = "AlreadyGetInPlay"
    WouldGetOutOfPlay = "WouldGetOutOfPlay"
    AlreadyGetOutOfPlay = "AlreadyGetOutOfPlay"
