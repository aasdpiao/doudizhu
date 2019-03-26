# -*- coding:UTF-8 -*-
class CardParse(object):
    """
    一副扑克牌类,54张排,abcd四种花色,小王14-a,大王15-a
    """
    def __init__(self):
        self.__cards = []

    def init_cards(self,cards):
        self.__cards = cards
