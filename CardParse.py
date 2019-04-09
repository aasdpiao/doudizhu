# -*- coding:UTF-8 -*-
from CardNode import CardNode
from Common import CardType

class CardParse(object):

    def __init__(self):
        self.cards = {}
        self.card_node = {}
        self.card_node[CardType.NODE_BOMB_TWO] = []
        self.card_node[CardType.NODE_BOMB] = []
        self.card_node[CardType.NODE_THREEPROGRESS] = []
        self.card_node[CardType.NODE_PROGRESS] = []
        self.card_node[CardType.NODE_LINKPAIR] = []
        self.card_node[CardType.NODE_THREEITEM] = []
        self.card_node[CardType.NODE_PAIR] = []
        self.card_node[CardType.NODE_SINGLECARD] = []

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
        self.CardParse_Bomb()
        self.CardParse_ThreeProgress()
        self.CardParse_Progress()
        self.CardParse_ThreeItem()
        self.CardParse_LinkPair()
        self.CardParse_Pair()
        self.CardParse_SingleCard()
        self.CounterScore()
        self.ShowCardNode()

    def ShowCardNode(self):
        for k,v in self.card_node.items():
            for card_node in v:
                print(card_node)

    def CardPerser(self):
        #牌数量信息
        self.card_num_info = {}
        #牌顺序信息,计算顺子
        self.card_order_info = []
        #王牌信息
        self.king = []

        self.dan = []
        self.dui = []
        self.san = []
        self.bomb = []
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
        #出单,出对,出三,炸弹(考虑拆开)
        num_info = self.card_num_info.values()
        num_info.sort(key=lambda cards: cards[0])
        for cards in num_info:
            if len(cards) == 1:
                self.dan.append(cards)
            elif len(cards) == 2:
                self.dui.append(cards)
                self.dan.append(cards[:1])
            elif len(cards) == 3:
                self.san.append(cards)
                self.dui.append(cards[:2])
                self.dan.append(cards[:1])
            elif len(cards) == 4:
                self.bomb.append(cards)
                self.san.append(cards[:3])
                self.dui.append(cards[:2])
                self.dan.append(cards[:1])

    def GetOutCardNoteList(self):
        pass

    def ParseOutCardProgress(self, first_out_card):
        pass

    def CounterScore(self):
        # int Res=-100000;
        # while(pNode!=NULL)
        # {
        #     if (pNode->next!=NULL)
        #     {
        #         pNode->mScore=CounterScore(pNode->next);
        #     }
        #     if (pNode->mCardType==CARDTYPE_NODE_PAIR)
        #     {
        #         int NodeCount=0,CurScore=0;
        #         CardNodePtr CurNode=pNode;
        #         while(CurNode!=NULL)
        #         {
        #             CurScore+=CounterScoreByCardType(CurNode->mCardType,CurNode->bCardList,CurNode->mCardCount);
        #             NodeCount++;
        #             CurNode=CurNode->right;
        #         }
        #         if (NodeCount>0)
        #         {
        #             //pNode->mScore+=CurScore/(NodeCount*0.5);
        #             pNode->mScore+=CurScore/2;
        #             Res=pNode->mScore;
        #             break;
        #         }
        #     }
        #     else
        #     {
        #         pNode->mScore+=CounterScoreByCardType(pNode->mCardType,pNode->bCardList,pNode->mCardCount);

        #         if (Res<pNode->mScore)
        #         {
        #             Res=pNode->mScore;
        #         }

        #         pNode=pNode->right;
        #     }
        # }
        # return Res;    
        Res=-100000


    def Remove_Cards(self,cards):
        self.cards = list(filter(lambda card: card.index not in [card.index for card in cards], self.cards))

    def CardParse_Bomb(self):
        self.CardPerser()
        if len(self.king) == 2:
            card_node = CardNode()
            card_node.SetCardType(CardType.NODE_BOMB_TWO)
            card_node.SetCards(self.king)
            self.card_node[CardType.NODE_BOMB_TWO].append(card_node)
            self.Remove_Cards(self.king)
        for bomb in self.bomb:
            card_node = CardNode()
            card_node.SetCardType(CardType.NODE_BOMB)
            card_node.SetCards(bomb)
            self.card_node[CardType.NODE_BOMB].append(card_node)
            self.Remove_Cards(bomb)

    def CardParse_ThreeProgress(self):
        self.CardPerser()
        progress = -1
        count = 0
        threeprogress = []
        for cards in self.san:
            if cards[0].rank -1 != progress:
                if count >= 2:
                    card_node = CardNode()
                    card_node.SetCardType(CardType.NODE_THREEPROGRESS)
                    card_node.SetCards(threeprogress)
                    self.card_node[CardType.NODE_THREEPROGRESS].append(card_node)
                    self.Remove_Cards(threeprogress)
                threeprogress = []
                progress = cards[0].rank
                count = 1
                threeprogress.extend(cards)
            else:
                count += 1 
                progress = cards[0].rank
                threeprogress.extend(cards)
        if count >= 2:
            card_node = CardNode()
            card_node.SetCardType(CardType.NODE_THREEPROGRESS)
            card_node.SetCards(threeprogress)
            self.card_node[CardType.NODE_THREEPROGRESS].append(card_node)
            self.Remove_Cards(threeprogress) 

    def CardParse_Progress(self):
        self.CardPerser()
        progress = []
        for card in self.card_order_info:
            if card == self.card_order_info[0]:
                progress.append(card)
            elif progress[-1].rank == card.rank - 1:
                progress.append(card)
            else:
                if len(progress) >= 5:
                    card_node = CardNode()
                    card_node.SetCardType(CardType.NODE_PROGRESS)
                    card_node.SetCards(progress)
                    self.card_node[CardType.NODE_PROGRESS].append(card_node)
                    self.Remove_Cards(progress) 
                progress = [card]
        #最后一轮
        if len(progress) >= 5:
            card_node = CardNode()
            card_node.SetCardType(CardType.NODE_PROGRESS)
            card_node.SetCards(progress)
            self.card_node[CardType.NODE_PROGRESS].append(card_node)
            self.Remove_Cards(progress)  

    def CardParse_ThreeItem(self):
        self.CardPerser()
        for cards in self.san:
            card_node = CardNode()
            card_node.SetCardType(CardType.NODE_THREEITEM)
            card_node.SetCards(cards)
            self.card_node[CardType.NODE_THREEITEM].append(card_node)
            self.Remove_Cards(cards)

    def CardParse_LinkPair(self):
        self.CardPerser()
        linkpair = []
        progress = -1
        count = 0
        for cards in self.dui:
            if cards[0].rank -1 != progress:
                if count >= 3:
                    card_node = CardNode()
                    card_node.SetCardType(CardType.NODE_LINKPAIR)
                    card_node.SetCards(linkpair)
                    self.card_node[CardType.NODE_LINKPAIR].append(card_node)
                    self.Remove_Cards(linkpair)
                linkpair = []
                progress = cards[0].rank
                count = 1
                linkpair.extend(cards)
            else:
                count += 1
                progress = cards[0].rank
                linkpair.extend(cards)
        if count >= 3:
            card_node = CardNode()
            card_node.SetCardType(CardType.NODE_LINKPAIR)
            card_node.SetCards(linkpair)
            self.card_node[CardType.NODE_LINKPAIR].append(card_node)
            self.Remove_Cards(linkpair)

    def CardParse_Pair(self):
        self.CardPerser()
        for cards in self.dui:
            card_node = CardNode()
            card_node.SetCardType(CardType.NODE_PAIR)
            card_node.SetCards(cards)
            self.card_node[CardType.NODE_PAIR].append(card_node)
            self.Remove_Cards(cards)

    def CardParse_SingleCard(self):
        self.CardPerser()
        for cards in self.dan:
            card_node = CardNode()
            card_node.SetCardType(CardType.NODE_SINGLECARD)
            card_node.SetCards(cards)
            self.card_node[CardType.NODE_SINGLECARD].append(card_node)
            self.Remove_Cards(cards) 

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
        return len(self.card_node[CardType.NODE_BOMB]) > 0

    def HaveKingBomb(self):
        return len(self.card_node[CardType.NODE_BOMB_TWO]) == 1

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


