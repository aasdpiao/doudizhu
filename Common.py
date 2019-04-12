# -*- coding:UTF-8 -*-
from enum import Enum

#基本牌型
class CARDTYPE(Enum):
    NODE_BOMB_TWO = 1         #王炸
    NODE_BOMB = 2             #炸弹
    NODE_THREEPROGRESS = 3    #飞机
    NODE_PROGRESS = 4         #顺子
    NODE_THREEITEM = 5        #3带1
    NODE_LINKPAIR = 6         #连对
    NODE_PAIR = 7             #对子
    NODE_SINGLECARD = 8       #单张
    NODE_MAX = 9

#出牌类型
class OUTTYPE(Enum):
    BOMB = 1                  #炸弹    
    FOURANDTWO_ONE = 2        #4带2张
    FOURANDTWO_TWO = 3        #4带2对
    THREEPROGRESS = 4         #飞机
    THREEPROGRESS_ONE = 5     #飞机带2张
    THREEPROGRESS_TWO = 6     #飞机带2对
    PROGRESS = 7              #顺子
    THREEITEM = 8             #三条
    THREEITEM_ONE = 9         #三条带1张
    THREEITEM_TWO = 10        #三条带1对
    LINKPAIR = 11             #连对
    PAIR = 12                 #对子
    SINGLECARD = 13           #单张
    MAX = 14


class POSITION(Enum):
    NEXTFARMER = 1            #下一个是农民
    PREFARMER = 2             #上一个是农民
    LANDLORD = 3              #地主
    DEFAULT = 4


class CARDKIND(Enum):
    BIG = 1                   # 2 大小王
    MIDDLE = 2                # 中牌 8~Q
    SMALL = 3                 # 小牌 3~7 
    KIND_MAX = 4

class CARDVALUE(Enum):
    CARD_3 = 1,
    CARD_4 = 2,
    CARD_5 = 3,
    CARD_6 = 4,
    CARD_7 = 5,
    CARD_8 = 6,
    CARD_9 = 7,
    CARD_10 = 8,
    CARD_J = 9,
    CARD_Q = 10,
    CARD_K = 11,
    CARD_A = 12,
    CARD_2 = 13,
    CARD_w = 14,
    CARD_W = 15,

def ShowCard(cards):
    card_info = "["
    for card in cards:
        card_info += (card.color + card.name + " ")
    card_info += "]"
    print(card_info)


def GetCardValueKind(card):
    rank = card.rank
    return rank

def GetCardNameByValue(card_type):
    card_names = {}
    card_names[CARDVALUE.CARD_3] = '3'
    card_names[CARDVALUE.CARD_4] = '4'
    card_names[CARDVALUE.CARD_5] = '5'
    card_names[CARDVALUE.CARD_6] = '6'
    card_names[CARDVALUE.CARD_7] = '7'
    card_names[CARDVALUE.CARD_8] = '8'
    card_names[CARDVALUE.CARD_9] = '9'
    card_names[CARDVALUE.CARD_10] = '10'
    card_names[CARDVALUE.CARD_J] = 'J'
    card_names[CARDVALUE.CARD_Q] = 'Q'
    card_names[CARDVALUE.CARD_K] = 'K'
    card_names[CARDVALUE.CARD_A] = 'A'
    card_names[CARDVALUE.CARD_2] = '2'
    card_names[CARDVALUE.CARD_w] = 'w'
    card_names[CARDVALUE.CARD_W] = 'W'
    return card_names.get(card_type)


