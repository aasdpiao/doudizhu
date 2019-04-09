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
        self.cards_type = ['A-方块-12-1',  'A-梅花-12-14',  'A-红桃-12-27',   'A-黑桃-12-40',
                           '2-方块-13-2',  '2-梅花-13-15',  '2-红桃-13-28',   '2-黑桃-13-41',
                           '3-方块-1-3',   '3-梅花-1-16',   '3-红桃-1-29',    '3-黑桃-1-42',
                           '4-方块-2-4',   '4-梅花-2-17',   '4-红桃-2-30',    '4-黑桃-2-43',
                           '5-方块-3-5',   '5-梅花-3-18',   '5-红桃-3-31',    '5-黑桃-3-44',
                           '6-方块-4-6',   '6-梅花-4-19',   '6-红桃-4-32',    '6-黑桃-4-45',
                           '7-方块-5-7',   '7-梅花-5-20',   '7-红桃-5-33',    '7-黑桃-5-46',
                           '8-方块-6-8',   '8-梅花-6-21',   '8-红桃-6-34',    '8-黑桃-6-47',
                           '9-方块-7-9',   '9-梅花-7-22',   '9-红桃-7-35',    '9-黑桃-7-48',
                           '10-方块-8-10',  '10-梅花-8-23',  '10-红桃-8-36',   '10-黑桃-8-49',
                           'J-方块-9-11',   'J-梅花-9-24',   'J-红桃-9-37',    'J-黑桃-9-50',
                           'Q-方块-10-12',  'Q-梅花-10-25',  'Q-红桃-10-38',   'Q-黑桃-10-51',
                           'K-方块-11-13',  'K-梅花-11-26',  'K-红桃-11-39',   'K-黑桃-11-52',
                           'w-小王-14-53',  'W-大王-15-54']

    def GetCards(self):
        cards = []
        for card_type in self.cards_type:
            cards.append(Card(card_type))
        random.shuffle(cards)
        return cards

    def DealPoker(self):
        cards = self.GetCards()
        card_groups = [[], [], []]
        landlord_cards = []
        for i in xrange(17):
            card_groups[0].append(cards.pop())
            card_groups[1].append(cards.pop())
            card_groups[2].append(cards.pop())
        for i in xrange(3):
            landlord_cards.append(cards.pop())
        return card_groups, landlord_cards

