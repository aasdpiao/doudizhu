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
        
    #判断大小
    def bigger_than(self, card):
        return self.rank > card.rank

    def __str__(self):
        return '(Card: %s, %s)' % (self.color, self.name)