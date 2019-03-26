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
        self.cards_type = ['A-方块-12',  'A-梅花-12',  'A-红桃-12',   'A-黑桃-12',
                           '2-方块-13',  '2-梅花-13',  '2-红桃-13',   '2-黑桃-13',
                           '3-方块-1',   '3-梅花-1',   '3-红桃-1',    '3-黑桃-1',
                           '4-方块-2',   '4-梅花-2',   '4-红桃-2',    '4-黑桃-2',
                           '5-方块-3',   '5-梅花-3',   '5-红桃-3',    '5-黑桃-3',
                           '6-方块-4',   '6-梅花-4',   '6-红桃-4',    '6-黑桃-4',
                           '7-方块-5',   '7-梅花-5',   '7-红桃-5',    '7-黑桃-5',
                           '8-方块-6',   '8-梅花-6',   '8-红桃-6',    '8-黑桃-6',
                           '9-方块-7',   '9-梅花-7',   '9-红桃-7',    '9-黑桃-7',
                           '10-方块-8',  '10-梅花-8',  '10-红桃-8',   '10-黑桃-8',
                           'j-方块-9',   'j-梅花-9',   'j-红桃-9',    'j-黑桃-9',
                           'Q-方块-10',  'Q-梅花-10',  'Q-红桃-10',   'Q-黑桃-10',
                           'K-方块-11',  'K-梅花-11',  'K-红桃-11',   'K-黑桃-11',
                           'w-小王-14',  'W-大王-15']

    def get_cards(self):
        cards = []
        for card_type in self.cards_type:
            cards.append(Card(card_type))
        random.shuffle(cards)
        return cards

    def deal_poker(self):
        cards = self.get_cards()
        card_groups = [[], [], []]
        landlord_cards = []
        for i in xrange(17):
            card_groups[0].append(cards.pop())
            card_groups[1].append(cards.pop())
            card_groups[2].append(cards.pop())
        for i in xrange(3):
            landlord_cards.append(cards.pop())
        return card_groups, landlord_cards

