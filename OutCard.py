# -*- coding:UTF-8 -*-
############################################
#              出牌列表                     #
############################################
from Common import OUTTYPE

class OutCard(object):
	def __init__(self):
		self.OutCardNodeList = []
		self.Active = False
		self.ParseAgain = False
		self.ExitBig = False
		self.OutFinish = False
		self.ParseAgain = False
		self.ParseAgain = False
	
 #    BOMB = 1                  #炸弹    
 #    FOURANDTWO_ONE = 2        #4带2张
 #    FOURANDTWO_TWO = 3        #4带2对
 #    THREEPROGRESS = 4         #飞机
 #    THREEPROGRESS_ONE = 5     #飞机带2张
 #    THREEPROGRESS_TWO = 6     #飞机带2对
 #    PROGRESS = 7              #顺子
 #    THREEITEM = 8             #三条
 #    THREEITEM_ONE = 9         #三条带1张
 #    THREEITEM_TWO = 10        #三条带1对
 #    LINKPAIR = 11             #连对
 #    PAIR = 12                 #对子
 #    SINGLECARD = 13           #单张
	def GetOutCardList(self,out_type):
		if out_type == OUTTYPE.BOMB:
			pass
			