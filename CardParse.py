# -*- coding:UTF-8 -*-
class CardParse(object):

    def __init__(self):
        self.cards = []
        self.card_node = []

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

    def CalucalateCallSocre(self):
        pass

    def ParseHandCardInfo(self, first_out_card):
        self.ParseHandCardData()
        self.GetOutCardNoteList()
        self.ParseOutCardProgress(first_out_card)

    #分析手中的牌数据
    def ParseHandCardData(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        cards = filter(lambda card: card.GetName() != "2", self.cards)  #去掉2
        self.CardParse_Bomb(cards)
        self.CounterScore()
        for card in cards:
            print(card)


    def GetOutCardNoteList(self):
        pass

    def ParseOutCardProgress(self, first_out_card):
        pass

    def CounterScore(self):
        pass

    def CardParse_Bomb(self,cards):
        NextCardCount = 0
        iTempCount = 0
        BombCount = 0
        while(self.GetLinkProgress(cards,0,4,1)):
            pass

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


