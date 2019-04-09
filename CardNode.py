# -*- coding:UTF-8 -*-
from Common import CardType

class CardNode(object):
    def __init__(self):
        self.cards = []
        self.card_type = 0
        self.score = 0

    def __str__(self):
        return '(CardNode: %s, %s)' % (self.card_type, ",".join([card.__str__() for card in self.cards]))

    def SetCards(self,cards):
        self.cards.extend(cards)

    def SetCardType(self,card_type):
        self.card_type = card_type

    def GetCardScore(self):
        if self.card_type == CardType.NODE_BOMB_TWO:
            pass
        elif self.card_type == CardType.NODE_BOMB:
            pass
        elif self.card_type == CardType.NODE_THREEPROGRESS:
            pass
        elif self.card_type == CardType.NODE_PROGRESS:
            pass
        elif self.card_type == CardType.NODE_THREEITEM:
            pass
        elif self.card_type == CardType.NODE_LINKPAIR:
            pass
        elif self.card_type == CardType.NODE_PAIR:
            pass
        elif self.card_type == CardType.NODE_SINGLECARD:
            pass

    def CalucalateScore_Bomb(self):
        pass

    def CalucalateScore_ThreeProgress(self):
        pass

    def CalucalateScore_Progress(self):
        pass

    def CalucalateScore_ThreeItem(self):
        pass

    def CalucalateScore_LinkPair(self):
        pass

    def CalucalateScore_Pair(self):
        pass

    def CalucalateScore_Single(self):
        pass
        
