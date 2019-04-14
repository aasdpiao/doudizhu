# -*- coding:UTF-8 -*-
from Common import CARDTYPE
import math

class CardNode(object):
    def __init__(self,player):
        self.player = player
        self.cards = []
        self.card_type = 0
        self.score = 0
        self.card_count = 0

    def __str__(self):
        return '(CardNode: %s, %s)' % (self.card_type, ",".join([card.__str__() for card in self.cards]))

    def SetCards(self,cards):
        self.cards.extend(cards)
        self.card_count = len(set([card.rank for card in cards]))

    def SetCardType(self,card_type):
        self.card_type = card_type

    def GetCardType(self):
        return self.card_type

    #获取牌型开始的那个牌
    def GetCardValue(self):
        return self.cards[0]

    def GetCardScore(self):
        if self.card_type == CARDTYPE.NODE_BOMB_TWO:
            return self.CalucalateScore_BombTwo()
        elif self.card_type == CARDTYPE.NODE_BOMB:
            return self.CalucalateScore_Bomb()
        elif self.card_type == CARDTYPE.NODE_THREEPROGRESS:
            return self.CalucalateScore_ThreeProgress()
        elif self.card_type == CARDTYPE.NODE_PROGRESS:
            return self.CalucalateScore_Progress()
        elif self.card_type == CARDTYPE.NODE_THREEITEM:
            return self.CalucalateScore_ThreeItem()
        elif self.card_type == CARDTYPE.NODE_LINKPAIR:
            return self.CalucalateScore_LinkPair()
        elif self.card_type == CARDTYPE.NODE_PAIR:
            return self.CalucalateScore_Pair()
        elif self.card_type == CARDTYPE.NODE_SINGLECARD:
            return self.CalucalateScore_Single()

    def IsBigest_CalucalateScore(self):
        card_counter = self.player.GetCardCounter()
        if card_counter.HaveKingBomb():
            return False
        if card_counter.HaveBomb():
            return False
        card_node = card_counter.GetMaxCardNode(self.card_type)
        if card_node == None:
            return True
        return self.GetCardValue().rank > card_node.GetCardValue().rank

    def CalucalateScore_BombTwo(self):
        res = 0
        return res

    def CalucalateScore_Bomb(self):
        res = 0
        return res

    def CalucalateScore_Progress(self):
        res = 500
        if self.IsBigest_CalucalateScore():
            res += 50
        card = self.GetCardValue()
        card_value = card.GetCardValue()
        res += 30 * (card_value + (self.card_count + 1)/2.0)
        res += 25 * self.card_count
        if self.card_count > 8:
            res += 12 * math.pow(2.0,(self.card_count + 3)/ 2.0) + (card_value + (self.card_count + 1)/2.0) * 10
        elif self.card_count > 5:
            res += 10 * math.pow(2.0,(self.card_count + 1)/ 2.0) + (card_value + (self.card_count + 1)/2.0) * 12
        return res

    def CalucalateScore_ThreeProgress(self):
        res = 1000
        if self.IsBigest_CalucalateScore():
            res += 100
        card = self.GetCardValue()
        card_value = card.GetCardValue()
        res += 115 * (card_value + (self.card_count + 1)/2.0)
        res += 45 * 5 * self.card_count
        if self.card_count > 2:
            res += 80 * 4 * math.pow(2.0,(self.card_count+1)/2.0) + 30 * card_value
        return res

    def CalucalateScore_ThreeItem(self):
        res = 450
        if self.IsBigest_CalucalateScore():
            res += 50
        card = self.GetCardValue()
        card_value = card.GetCardValue()
        if card_value == 13:
            card_value = 14
        if card_value >= 9:
            res +=30 * (2 * card_value - 9) * 25
        elif card_value >= 8:
            res += card_value * 30
        else:
            res += card_value * 20
        res += 15*4
        return res

    def CalucalateScore_LinkPair(self):
        res = 500
        if self.IsBigest_CalucalateScore():
            res += 50
        card = self.GetCardValue()
        card_value = card.GetCardValue()
        res += 50 * (card_value + (self.card_count + 1)/2.0)
        res += 25*self.card_count*2
        if self.card_count == 3:
            res += 42*math.pow(2.0,3+(self.card_count - 3)/2.0) + (card_value + (self.card_count+1)/2.0) * 20
        elif self.card_count > 3:
            res += 45*math.pow(2.0,3+(self.card_count - 3)/2.0) + (card_value + (self.card_count+1)/2.0) * 20
        return res

    def CalucalateScore_Pair(self):
        res = 450
        if self.IsBigest_CalucalateScore():
            res += 50
        card = self.GetCardValue()
        card_value = card.GetCardValue()
        if card_value == 13:
            card_value = 14
        # CARD_10
        if card_value > 9:
            res += (2 * card_value - 9) * 25
        elif card_value > 8:
            res += card_value * 25
        else:
            res += card_value * 15
        res += 15*2
        return res


    def CalucalateScore_Single(self):
        res = 0
        for card in self.cards:
            card_value = card.GetCardValue()
            res -= (14 - card_value) * 20
        return res
