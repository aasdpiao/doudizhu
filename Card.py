# -*- coding:UTF-8 -*-
############################################
#              扑克牌相关类                 #
############################################
class Card(object):
    """
    扑克牌类
    """
    def __init__(self, card_type):
        self.card_type = card_type
        #名称
        self.name = self.card_type.split('-')[0]
        #花色
        self.color = self.card_type.split('-')[1]
        #大小
        self.rank = int(self.card_type.split('-')[2])
        #编号
        self.index = int(self.card_type.split('-')[3])
        
    #判断大小
    def __cmp__(self, other):
        if self.rank < other.rank:
            return -1
        elif self.rank > other.rank:
            return 1
        else:
            return 0

    def __str__(self):
        return '(Card: %s, %s)' % (self.color, self.name)

    def GetName(self):
        return self.name

    def GetColor(self):
        return self.color

    def GetRank(self):
        return self.rank

    def GetIndex(self):
        return self.index

    def GetCardValue(self):
        if self.rank < 13:
            return self.rank + 1
        else:
            return self.rank
