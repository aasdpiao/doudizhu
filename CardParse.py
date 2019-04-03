# -*- coding:UTF-8 -*-
class CardParse(object):

    def __init__(self):
        self.cards = []
        self.card_node = []

        #出牌信息
        self.dan = []
        self.dui = []
        self.san = []
        self.san_dai_yi = []
        self.san_dai_er = []
        self.bomb = []
        self.shunzi = []
        
        #牌数量信息
        self.card_num_info = {}
        #牌顺序信息,计算顺子
        self.card_order_info = []
        #王牌信息
        self.king = []


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
        for card in self.cards:
            #王牌信息
            if card.rank in [14,15]:
                self.king.append(card)
            #数量
            tmp = self.card_num_info.get(card.name, [])
            if len(tmp) == 0:
                self.card_num_info[card.name] = [card]
            else:
                self.card_num_info[card.name].append(card)
            #顺序
            if card.rank in [13,14,15]: #不统计2,小王,大王
                continue
            elif len(self.card_order_info) == 0:
                self.card_order_info.append(card)
            elif card.rank != self.card_order_info[-1].rank:
                self.card_order_info.append(card)
        
        #王炸
        if len(self.king) == 2:
            self.bomb.append(self.king)
            
        #出单,出对,出三,炸弹(考虑拆开)
        for k, v in self.card_num_info.items():
            if len(v) == 1:
                self.dan.append(v)
            elif len(v) == 2:
                self.dui.append(v)
                self.dan.append(v[:1])
            elif len(v) == 3:
                self.san.append(v)
                self.dui.append(v[:2])
                self.dan.append(v[:1])
            elif len(v) == 4:
                self.bomb.append(v)
                self.san.append(v[:3])
                self.dui.append(v[:2])
                self.dan.append(v[:1])
                
        #三带一,三带二
        for san in self.san:
            for dan in self.dan:
                #防止重复
                if dan[0].name != san[0].name:
                    self.san_dai_yi.append(san+dan)
            for dui in self.dui:
                #防止重复
                if dui[0].name != san[0].name:
                    self.san_dai_er.append(san+dui)  
                    
        #获取最长顺子
        max_len = []
        for i in self.card_order_info:
            if i == self.card_order_info[0]:
                max_len.append(i)
            elif max_len[-1].rank == i.rank - 1:
                max_len.append(i)
            else:
                if len(max_len) >= 5:
                   self.shunzi.append(max_len) 
                max_len = [i]
        #最后一轮
        if len(max_len) >= 5:
           self.shunzi.append(max_len)   
        #拆顺子 
        shunzi_sub = []             
        for i in self.shunzi:
            len_total = len(i)
            n = len_total - 5
            #遍历所有可能顺子长度
            while(n > 0):
                len_sub = len_total - n
                j = 0
                while(len_sub+j <= len(i)):
                    #遍历该长度所有组合
                    shunzi_sub.append(i[j:len_sub+j])
                    j = j + 1
                n = n - 1
        self.shunzi.extend(shunzi_sub)


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


