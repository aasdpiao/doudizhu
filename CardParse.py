# -*- coding:UTF-8 -*-
class CardData(object):

    def __init__(self):
        self.cards = []

    def SetCardData(self,cards):
        self.cards = cards

    def SetCardDataByIndex(self):
        pass

    def InitCardDataWithCardList(self):
        pass

    def AddCardData(self):
        pass

    def GetCardData(self):
        pass

    def GetBigCardData(self):
        pass

    def GetSomeCardData(self):
        pass

    def GetKingCardData(self):
        pass

    def ExitCardValue(self):
        pass

    def ValidCard(self):
        pass

    def GetCardDataCount(self):
        pass

    def GetKingCount(self):
        pass


class CardParse(CardData):
    """
    一副扑克牌类,54张排,abcd四种花色,小王14-a,大王15-a
    """
    def __init__(self):
        self.__cards = []


    def GetLinkProgress(self,cards,refer_card,same_count,card_count):
        pass

    #获取最长的顺子
    def GetLongProgress(self):
        pass

    def HaveLinkProgress(self):
        pass

    def HaveSideLinkProgress(self):
        pass

    def HaveMiddleLinkProgress(self):
        pass

    def HaveLinkProgressInclude(self):
        pass

    def IsSameColor(self):
        pass

    def HaveBigCard(self):
        pass

    def HaveBomb(self):
        pass

    def HaveKingBomb(self):
        pass

    def IsOnlyBigCard(self):
        pass

    def IsExitSmallerCard(self):
        pass

    def IsExitSmallerProgress(self):
        pass

    def IsExitSmallerLinkPair(self):
        pass

    def GetSortCardList(self):
        pass

    def GetSameCountCardCount(self):
        pass

    def GetCountByCardCount(self):
        pass

    def RemoveBomb(self):
        pass

    def RemoveCard(self):
        pass

    def GetBigestCard(self):
        pass

    def GetBigCard(self):
        pass

    def GetBigCardCount(self):
        pass

    def GetBigCardOutKing(self):
        pass

    def GetSmallestCard(self):
        pass

    def GetSmallerCard(self):
        pass

    def GetBombCardValue(self):
        pass

    def GetBombCardList(self):
        pass

    def GetBombCount(self):
        pass

    def IsThreeTakeOne(self):
        pass


#记牌器
class CardCounter(CardParse):

    def __init__(self):
        pass

