# -*- coding:UTF-8 -*-
############################################
#              玩家类                      #
############################################

class Player(object):
    def __init__(self):
        self.__cards = []

    def __str__(self):
        str = ""
        for card in self.__cards:
            print(card)
        return str

    def set_cards(self, cards):
        self.__cards = cards