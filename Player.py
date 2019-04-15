# -*- coding:UTF-8 -*-
############################################
#              玩家类                      #
############################################
from CardParse import CardParse
from Cards import Cards
from Common import CARDVALUE,CARDTYPE,POSITION
from OutCard import OutCard
from OutCardNode import OutCardNode
from CardCounter import CardCounter
from GuessCarder import GuessCarder
import math

class Player(object):
    def __init__(self):
        self.cards = []
        self.desk_station = 0
        self.RobotId = POSITION.DEFAULT
        self.CardCounter = CardCounter(self)
        self.CardParse = CardParse(self)
        self.OutCard = OutCard(self)
        self.GuessCarder = GuessCarder(self)
        self.HandCardCount = 0
        self.CallSocre = 0
        self.FirstLandlord = 0

    def __str__(self):
        str = ""
        for card in self.cards:
            print(card)
        return str

    def SetFirstCallLord(self):
        self.FirstLandlord = 1

    def GetCallScore(self):
        return self.CallSocre

    def GetRobotId(self):
        return self.RobotId

    def IsLandlorder(self):
        return self.RobotId == POSITION.LANDLORD

    def IsPreFarmer(self):
        return self.RobotId == POSITION.PREFARMER

    def IsNextFarmer(self):
        return self.RobotId == POSITION.NEXTFARMER

    def GetCardCounter(self):
        return self.CardCounter

    def GetCardParse(self):
        return self.CardParse

    def GetCardsCount(self):
        return len(self.cards)

    def GetGuessCarder(self):
        return self.GuessCarder

    #设置下一个出牌的玩家
    def SetNextPlayer(self,next_player):
        self.next_player = next_player

    def GetNextPlayer(self):
        return self.next_player

    def SetRobotId(self,robotId):
        self.robotId = robotId

    #设置出牌方向
    def SetDirection(self):
        pass

    #设置自己的座位号
    def SetDeskStation(self, desk_station):
        self.desk_station = desk_station

    def GetDeskStation(self):
        return self.desk_station

    #设置手上牌数据 游戏开始
    def SetCardList(self, cards):
        self.cards = cards
        self.cards.sort()
        self.HandCardCount = len(cards)
        self.SetCardCounter()
        self.CardParse = CardParse(self)
        self.CardParse.SetCardData(self.cards)
        self.CardParse.ParseHandCardData()
        self.FillOutCardNoteList()


    def SetCardCounter(self):
        cards = Cards()
        card_list = cards.GetCards()
        counter = [card for card in card_list if card.index not in [x.index for x in self.cards]]
        self.CardCounter.SetCardData(counter)
        self.CardCounter.ParseHandCardData()

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

    def CalucalateCallSocre(self):
        Res = 0
        BombCount = self.GetCardParse().GetBombCount()
        if BombCount > 0:
            Res += BombCount * 8 + math.power(2.0, BombCount-1) * 6
        return Res

    #叫分
    def CallScore(self):
        res = 0
        Score = self.CalucalateCallSocre()
        Card2Count = self.GetCardParse().GetCardValueCount(CARDVALUE.CARD_2)
        KingCount = self.GetCardParse().GetKingCount()
        if KingCount == 2:
            if Card2Count > 0:
                if Score >= 15:
                    res = 3
                elif Score >= 10:
                    res = 2
                else:
                    res = 1
            else:
                if Score >= 20:
                    res = 3
                elif Score >= 15:
                    res = 2
                else:
                    res = 1
        elif KingCount == 1:
            if self.HaveBigKing():
                if Card2Count > 0:
                    if Score >= 20:
                        res = 3
                    elif Score >= 15:
                        res = 2
                    else:
                        res = 1
                else:
                    if Score >= 30:
                        res = 3
                    elif Score >= 15:
                        res = 2
                    else:
                        res = 1
            else:
                if Card2Count > 0:
                    if Score >= 25:
                        res = 3
                    elif Score >= 20:
                        res = 2
                    else:             
                        res = 1
                else:
                    if Score >= 30:
                        res = 3
                    elif Score >= 25:
                        res = 2
                    else:
                        res = 1
        else:
            if Card2Count == 4:
                if Score >= 20:
                    res = 3
                elif Score >= 15:
                    res = 2
                else:
                    res = 1
            elif Card2Count == 3:
                if Score >= 30:
                    res = 3
                elif Score >= 20:
                    res = 2
                else:
                    res = 1
            elif Card2Count == 2:
                if Score >= 25:
                    res = 2
                elif Score >= 20:
                    res = 1
            elif Card2Count == 1:
                if Score >= 30:
                    res = 2
                elif Score >= 20:
                    res = 1
            else:
                if Score >= 30:
                    res = 1
        return res

    #叫地主
    def CallLandlord(self,score):
        self.FirstLandlord += 1
        if self.FirstLandlord >= 3:
            self.CallSocre = score
            return True
        Card2Count = self.GetCardParse().GetCardValueCount(CARDVALUE.CARD_2)
        KingCount = self.GetCardParse().GetKingCount()
        CallScore = self.CallScore()
        if score == 0:
            if CallScore > 1 or KingCount > 0 or Card2Count > 2:
                self.CallSocre = 1
                return False
        elif score == 1:
            if CallScore > 2 or CallScore == 2 and (KingCount > 0 and Card2Count >= 2):
                self.CallSocre = 2
                return False
        elif score == 2:
            if CallScore > 2 or KingCount ==2 and (Card2Count >= 2):
                self.CallSocre = 3
                return True
        else:
            if CallScore > 2 and KingCount > 0 and(Card2Count > 1):
                self.CallSocre = 3
                return True


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
        pass

    def FillOutCardNoteList(self):
        card_parse = self.GetCardParse()
        node_dict = card_parse.GetCardNodeDict()
        for card_type,node_list in node_dict.items():
            for node in node_list:
                out_node = OutCardNode()
                out_node.SetCardNode(node)
                self.OutCard.PushOutCardNode(out_node)
        self.OutCard.AmendOutCardNode()
        self.CheckBigNode()

    def CheckBigNode(self,):
        card_parse = self.GetCardParse()
        card_node = card_parse.GetCardNodeDict()
        for card_type,card_node_list in card_node.items():
            if len(card_node_list) < 1:
                continue
            bigest_node = card_node_list[-1]
            if not bigest_node:
                continue
            if self.CheckBigest(bigest_node,card_type,card_parse):
                self.OutCard.SetWin(card_type,True)
                self.OutCard.ExitBig(card_type,True)

    def CheckBigest(self,card_node,card_type,card_parse):
        if card_type == CARDTYPE.NODE_BOMB:
            if card_parse.HaveKingBomb():
                return True
            if self.CardCounter.HaveKingBomb():
                return False
            if self.CardCounter.GetCardValueCount(CARDVALUE.CARD_2) == 4:
                return False
            max_node = self.CardCounter.GetMaxCardNode(CARDTYPE.NODE_BOMB)
            if card_node.GetCardValue().rank < max_node.GetCardValue().rank:
                return False
            return True
        elif card_type == CARDTYPE.NODE_THREEPROGRESS:
            pass

    #打印手牌
    def WriteHandCardList(self):
        card_info = "["
        for card in self.cards:
            card_info += (card.color + card.name + " ")
        card_info += "]"
        print(card_info)

    def AddBottomCardList(self, cards):
        self.cards.extend(cards)

    def GetOutCardList_First(self):
        if self.HandCardCount * 4 == self.CardParse.GetCardNodeCount(CARDTYPE.NODE_BOMB):
            pass


