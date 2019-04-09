# -*- coding:UTF-8 -*-
############################################
#              玩家类                      #
############################################
from CardParse import CardParse

class Player(object):
    def __init__(self):
        self.cards = []
        self.desk_station = 0

    def __str__(self):
        str = ""
        for card in self.cards:
            print(card)
        return str

    #设置下一个出牌的玩家
    def SetNextPlayer(self,next_player):
        self.next_player = next_player

    def GetNextPlayer(self):
        return self.next_player

    #设置出牌方向
    def SetDirection(self):
        pass

    #设置自己的座位号
    def SetDeskStation(self, desk_station):
        self.desk_station = desk_station

    #设置手上牌数据 游戏开始
    def SetCardList(self, cards):
        self.cards = cards
        self.cards.sort()

    #获取手中的牌
    def GetHandCardList(self):
        pass

    #得到出牌列表
    def GetOutCardList(self):
        pass

    #得到出牌列表
    def FollowOutCardList(self):
        pass

    #得到手中的牌个数
    def GetHandCardCount(self):
        pass

    #添加三张牌
    def AddCardList(self):
        pass

    #叫分
    def CallScore(self):
        pass

    #叫地主
    def CallLandlord(self):
        pass

    #是否加倍
    def IsAddPoint(self):
        pass

    #判断当前牌是否能出
    def CanOutCardList(self):
        pass

    #判断能否跟牌
    def CanFollowCard(self):
        pass

    def ParseHandCardInfo(self):
        card_parse = CardParse()
        card_parse.SetCardData(self.cards)
        card_parse.ParseHandCardData()
    #打印手牌
    def WriteHandCardList(self):
        card_info = "["
        for card in self.cards:
            card_info += (card.color + card.name + " ")
        card_info += "]"
        print(card_info)

    def AddBottomCardList(self):
        pass

        
