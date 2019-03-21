# -*- coding:UTF-8 -*-
import random
from Card import Card

############################################
#              扑克牌相关类                 #
############################################
class Cards(object):
    """
    一副扑克牌类,54张排,abcd四种花色,小王14-a,大王15-a
    """
    def __init__(self):
        #初始化扑克牌类型
        self.cards_type = ['A-a-12',  'A-b-12',  'A-c-12',   'A-d-12',
                           '2-a-13',  '2-b-13',  '2-c-13',   '2-d-13',
                           '3-a-1',   '3-b-1',   '3-c-1',    '3-d-1',
                           '4-a-2',   '4-b-2',   '4-c-2',    '4-d-2',
                           '5-a-3',   '5-b-3',   '5-c-3',    '5-d-3',
                           '6-a-4',   '6-b-4',   '6-c-4',    '6-d-4',
                           '7-a-5',   '7-b-5',   '7-c-5',    '7-d-5',
                           '8-a-6',   '8-b-6',   '8-c-6',    '8-d-6',
                           '9-a-7',   '9-b-7',   '9-c-7',    '9-d-7',
                           '10-a-8',  '10-b-8',  '10-c-8',   '10-d-8',
                           'j-a-9',   'j-b-9',   'j-c-9',    'j-d-9',
                           'Q-a-10',  'Q-b-10',  'Q-c-10',   'Q-d-10',
                           'K-a-11',  'K-b-11',  'K-c-11',   'K-d-11',
                           'W-a-14',  'W-a-15']
        #初始化扑克牌类                  
        self.cards = self.get_cards()

        #初始化扑克牌类
    def get_cards(self):
        cards = []
        for card_type in self.cards_type:
            cards.append(Card(card_type))
        random.shuffle(cards)
        return cards