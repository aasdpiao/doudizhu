# -*- coding:UTF-8 -*-
############################################
#              玩家类                      #
############################################
from CardParse import CardParse
from Common import CARDVALUE,CARDTYPE
import math

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

    def CalucalateCallSocre(self):
        Res = 0
        BombCount = self.GetBombCount()
        if BombCount > 0:
            Res += BombCount * 8 + math.power(2.0,BombCount-1) * 6
        return Res

    #叫分
    def CallScore(self):
        res = 0
        Score = self.CalucalateCallSocre()
        Card2Count = self.GetCardValueCount(CARDVALUE.CARD_2)
        KingCount = self.GetKingCount()
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
    def CallLandlord(self):
        # int KingCount=m_CardData.GetKingCount();//王的个数
        # int Card2Count=m_CardData.GetCardValueCount(CARD_2);
        # if (CurScore==0)
        # {
        #     if (m_CallScore>1||KingCount>0||Card2Count>=2)
        #     {
        #         return 1;
        #     }
        # }
        # else if (CurScore==1)
        # {
        #     if (m_CallScore>2||m_CallScore==2&&(KingCount>0||Card2Count>2))
        #     {
        #         return 1;
        #     }
        # }
        # else if (CurScore==2)
        # {
        #     if (m_CallScore>2&&KingCount>0||m_CallScore==2&&(KingCount>1||KingCount>0&&Card2Count>=2))
        #     {
        #         return 1;
        #     }
        # }
        # else 
        # {
        #     if (m_CallScore>2&&KingCount>0&&(m_CardData.HaveBigKing()||Card2Count>1))
        #     {
        #         return 1;
        #     }
        # }

        # return 0;
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

    def ParseHandCardData(self):
        card_parse = CardParse()
        card_parse.SetCardData(self.cards)
        card_parse.ParseHandCardData()
        self.GetOutCardNoteList(card_parse)

    def GetOutCardNoteList(self,card_parse):
        bombNode = card_parse.GetCardNodeList(CARDTYPE.NODE_BOMB)
        threeprogressNode = card_parse.GetCardNodeList(CARDTYPE.NODE_THREEPROGRESS)
        progressNode = card_parse.GetCardNodeList(CARDTYPE.NODE_PROGRESS)
        threeitemNode = card_parse.GetCardNodeList(CARDTYPE.NODE_THREEITEM)
        linkpairNode = card_parse.GetCardNodeList(CARDTYPE.NODE_LINKPAIR)
        pairNode = card_parse.GetCardNodeList(CARDTYPE.NODE_PAIR)
        singlecardNode = card_parse.GetCardNodeList(CARDTYPE.NODE_SINGLECARD)
        Count = 0
        

    #打印手牌
    def WriteHandCardList(self):
        card_info = "["
        for card in self.cards:
            card_info += (card.color + card.name + " ")
        card_info += "]"
        print(card_info)

    def AddBottomCardList(self):
        pass

        
