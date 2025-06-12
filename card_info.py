from typing import Literal


class CardInfo:
    name: str
    cardClass: (
        Literal["Guardian"]
        | Literal["Seeker"]
        | Literal["Rogue"]
        | Literal["Mystic"]
        | Literal["Survivor"]
        | Literal["Neutral"]
        | Literal["Mythos"]
    )
