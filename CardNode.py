# -*- coding:UTF-8 -*-
from Common import CARDTYPE

class CardNode(object):
    def __init__(self):
        self.cards = []
        self.card_type = 0
        self.score = 0
        self.card_count = 0

    def __str__(self):
        return '(CardNode: %s, %s)' % (self.card_type, ",".join([card.__str__() for card in self.cards]))

    def SetCards(self,cards):
        self.cards.extend(cards)
        self.card_count = len(set([card.rank for card in cards]))

    def SetCARDTYPE(self,card_type):
        self.card_type = card_type

    def GetCardScore(self):
        if self.card_type == CARDTYPE.NODE_BOMB_TWO:
            pass
        elif self.card_type == CARDTYPE.NODE_BOMB:
            pass
        elif self.card_type == CARDTYPE.NODE_THREEPROGRESS:
            pass
        elif self.card_type == CARDTYPE.NODE_PROGRESS:
            pass
        elif self.card_type == CARDTYPE.NODE_THREEITEM:
            pass
        elif self.card_type == CARDTYPE.NODE_LINKPAIR:
            pass
        elif self.card_type == CARDTYPE.NODE_PAIR:
            pass
        elif self.card_type == CARDTYPE.NODE_SINGLECARD:
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
        
