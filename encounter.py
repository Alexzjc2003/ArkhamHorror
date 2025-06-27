from deck import Deck, DiscardPile
from card import Card, CardType


class EncounterDeck(Deck):

    def __init__(self):
        super().__init__(DiscardPile())

    def drawFromTop(self) -> Card:
        if len(self.cards) == 0:
            self.reset()
        return super().drawFromTop()

    def drawFromBottom(self) -> Card:
        if len(self.cards) == 0:
            self.reset()
        return super().drawFromBottom()


class TreacheryCard(Card):
    def __init__(self, name):
        super().__init__(name)
        self.type = CardType.Treachery
