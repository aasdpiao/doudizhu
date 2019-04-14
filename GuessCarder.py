# -*- coding:UTF-8 -*-
############################################
#              玩家类                      #
############################################

# BYTE          m_SelfDeskStation;//自己id
# BYTE          m_Landlorder;//地主id
# BYTE          m_FirstOutCarder;//第一个出牌
# BYTE          m_PreOutCarder;//前一个出牌者
# BYTE          m_FirstOutCarderOnce;//一轮中第一个牌
# BYTE          m_OutCardHandCount;//出牌手数
# BYTE          m_OutCardType;//当前出牌类型
# int           m_HandCardCount;
# RobotId       m_RobotId;//
# bool          m_StartGuessCard;
# BYTE          m_LandlorderMaxSingleCard;//地主手中最大的单牌
# protected:
# CGuessObject          m_Object[2];//0:下一个玩家  1：前一个玩家
# OutCardDataList       m_SelfOutCardList;
# SelfOutCardInfo       m_OutCardInfo;
# FirstOutCardItemList  m_FirstOutIdList;//第一个出牌玩家列表
# protected:
# BYTE  m_LandlordCardList[4];//地主底牌
# BYTE  m_LandlordCardCount;

# UINT m_CurOutCardType;
# BYTE m_CurKeyCardValue;


# BYTE m_OutCardDrection;  //出牌方向 1：逆时针  2：顺时针  默认逆时针
# CCardParse    m_CardData;
from Common import POSITION

class GuessCarder(object):
	def __init__(self,player):
		self.player = player
		self.SelfDeskStation = 0
		self.Landlorder = 0
		self.NextGuessObject = 0 
		self.LastGuessObject = 0

	def SetPlayerID(self,landlord,nextplayer,lastplayer):
		self.landlord = landlord
		self.LastGuessObject = lastplayer
		self.NextGuessObject = nextplayer

	def GetRivalHandCardCount(self):
		if self.player.GetRobotId() == POSITION.LANDLORD:
			count1 = self.NextGuessObject.GetCardsCount()
			count2 = self.LastGuessObject.GetCardsCount()
			return count1 if count1 > count2 else count2
		elif self.player.GetRobotId() == POSITION.NEXTFARMER or self.player.GetRobotId() == POSITION.PREFARMER:
			return self.Landlorder.GetCardsCount()
		else:
			return 0