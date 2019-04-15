# -*- coding:UTF-8 -*-
############################################
#              出牌列表                     #
############################################
from Common import OUTTYPE,CARDTYPE,CARDVALUE
from CardParse import CardParse

class OutCard(object):
	def __init__(self,player):
		self.player = player
		self.OutCardNodeList = {}
		self.Active = False
		self.ParseAgain = False
		self.ExitBig = {}
		self.OutFinish = False
		self.ParseAgain = False
		self.ParseAgain = False
		self.out_type = OUTTYPE.MAX
	
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

	def SetOutType(self,out_type):
		self.out_type = out_type

	def GetOutCardList(self,out_type):
		if out_type == OUTTYPE.BOMB:
			pass

	def SetWin(self,card_type,isBig):
		self.ExitBig[card_type] = isBig

	def PushOutCardNode(self,out_node):
		card_node = out_node.GetCardNode()
		card_type = card_node.GetCardType()
		if self.OutCardNodeList.get(card_type) == None:
			self.OutCardNodeList[card_type] = []
		self.OutCardNodeList[card_type].append(out_node)
		self.OutCardNodeList[card_type].sort()

	def NodeCount(self,card_type):
		node_list = self.OutCardNodeList.get(card_type,[])
		return len(node_list)

	def GetSingleCardCount(self):
		node_list = self.OutCardNodeList.get(CARDTYPE.NODE_SINGLECARD,[])
		if len(node_list) < 1:
			return 0
		node = node_list[0]
		return node.GetCardNode().card_count

	'''
	if (m_FirstOutCard&&GetRivalHandCardCount()==1)
		{
			//自己第一个出牌  且对手手中只有一张牌
			AmendOutCardNode_Progress_Single_Pair();
		}
		if (m_OutCardNodeHead.NodeCount(CARDTYPE_NODE_PAIR)>0&&!CCardCounter::HaveLinkProgress(m_OutCardNodeHead.mList[CARDTYPE_NODE_PAIR]->Node->GetCardValue(),2,1))
		{
			//手中有大的对子
			AmendOutCardNode_Progress_Single_Pair(1);
		}
		AmendOutCardNode_ProgressSingle_Pair();
		AmendOutCardNode_ProgressSinglePair_Three();
		AmendOutCardNode_ProgressPair_Three();
		AmendOutCardNode_ProgressLinkPair_Three();
		OutCardNodePtr SingleNode=m_OutCardNodeHead.mList[CARDTYPE_NODE_SINGLECARD];
		if (SingleNode!=NULL)
		{
			if (SingleNode->Node->mCardCount<=0)
			{
				m_OutCardNodeHead.mList[CARDTYPE_NODE_SINGLECARD]=NULL;
			}
			else if(SingleNode->Node->mCardCount>1)
			{
				//对单牌进行排序
				SortCardList(SingleNode->Node->bCardList,SingleNode->Node->mCardCount);
			}
		}

		ParseSingleToPair();
	'''
	def AmendOutCardNode(self):
		self.AmendOutCardNode_Bomb_Single()
		self.AmendOutCardNode_Progress_Pair()
		self.AmendOutCardNode_Progress_Single()
		self.AmendOutCardNode_Progress()
		self.AmendOutCardNode_Pair()
		self.AmendOutCardNode_LinkPair_Single()
		self.AmendOutCardNode_LinkPair()
		self.AmendOutCardNode_MergeLinkPair()
		self.AmendOutCardNode_Progress_Pair_Single()
		self.AmendOutCardNode_LinkPair_Pair_Three()

	def AmendOutCardNode_Bomb_Single(self):
		if self.NodeCount(CARDTYPE.NODE_BOMB) == 0 or self.GetSingleCardCount() < 3:
			return
		node_list = self.OutCardNodeList.get(CARDTYPE.NODE_SINGLECARD, [])
		card_node = node_list[0]
		card_parse = CardParse(self.player)
		card_parse.SetCardData(card_node.GetCardNode().GetCards())
		guess_carder = self.player.GetGuessCarder()
		card_count = 0
		pair_count = 0
		bflag = False
		if guess_carder.GetRivalHandCardCount() <= 2:
			if(self.player.IsLandlorder() or self.player.IsPreFarmer()):
				bflag = True
		node_list = self.OutCardNodeList.get(CARDTYPE.NODE_BOMB, [])
		for node in node_list:
			card = node.GetCardNode().GetCardValue()
			card_parse.AddCardData([card])
			progress_count,card_rank = card_parse.GetLongProgress()
			if (bflag and progress_count >= 5 or card_count>=6 and card_rank > 5 and self.player.GetCardParse().GetCardValueCount(CARDVALUE.CARD_2) < 3):
				pass


	'''
	void CBaseRobotAction::AmendOutCardNode_Progress_Pair()
	{
		if (!m_FirstOutCard&&(m_CurOutCardType==CARDTYPE_NODE_PAIR||m_CurOutCardType==CARDTYPE_NODE_PROGRESS))
		{
			//当前桌面出的是对子和顺子
			return;
		}
		OutCardNodePtr CurNode=m_OutCardNodeHead.mList[CARDTYPE_NODE_PROGRESS],CurPairNode=NULL,pNode=NULL;

		if (m_OutCardNodeHead.mList[CARDTYPE_NODE_PROGRESS]==NULL||m_OutCardNodeHead.NodeCount(CARDTYPE_NODE_PAIR)<=0)
		{
			//不存在对子 或者 顺子 直接返回
			return ;
		}
		if (!m_FirstOutCard&&!IsPartner(m_PreOutCarder)&&m_CurOutCardType==CARDTYPE_NODE_THREEITEM&&(m_OutCardNodeHead.NodeCount(CARDTYPE_NODE_THREEITEM)<=0||CompareCard(m_OutCardNodeHead.GetTailNode(CARDTYPE_NODE_THREEITEM)->Node->GetCardValue(0),m_CurKeyCardValue)<0))
		{
			//手中没有大的三条
			int Index=0;
			while(CurNode!=NULL)
			{
				if (CurNode->Node->mCardCount<7)
				{
					CurNode=CurNode->next;
					continue;
				}
				Index=-1;
				if (IsLivePair(CurNode->Node->GetCardValue(1),pNode)>0)
				{
					Index=1;
				}
				else if (IsLivePair(CurNode->Node->GetCardValue(CurNode->Node->mCardCount-2),pNode)>0)
				{
					Index=CurNode->Node->mCardCount-2;
				}

				if (Index!=-1&&CompareCard(CurNode->Node->GetCardValue(Index),m_CurKeyCardValue)>0)
				{
					//存在三条
					BYTE bCardList[4]={0};
					memcpy(bCardList,pNode->Node->bCardList,2);
					bCardList[2]=CurNode->Node->GetCardValue(Index);

					//删除对子
					m_OutCardNodeHead.RemoveNode(CARDTYPE_NODE_PAIR,pNode);

					//创建三条
					CreateOutCardNode(bCardList,3,CARDTYPE_NODE_THREEITEM,1,pNode);
					m_OutCardNodeHead.Push(pNode,CARDTYPE_NODE_THREEITEM);
					//整理顺子

					if (Index==1)
					{
						AdjustbCardList(CurNode->Node->bCardList,CurNode->Node->mCardCount,0);
						CurNode->Node->mCardCount--;
						AdjustbCardList(CurNode->Node->bCardList,CurNode->Node->mCardCount,0);
						CurNode->Node->mCardCount--;
					}
					else
					{
						CurNode->Node->mCardCount-=2;
					}

					break;
				}
				CurNode=CurNode->next;
			}
		}
		if (m_OutCardNodeHead.NodeCount(CARDTYPE_NODE_PAIR)<2)
		{
			return ;
		}
		int ThreeItemCount=0;
		CurNode=m_OutCardNodeHead.mList[CARDTYPE_NODE_PROGRESS];
		while(CurNode!=NULL)
		{
			//检查存在的三条的个数
			ThreeItemCount=0;
			if (m_OutCardNodeHead.NodeCount(CARDTYPE_NODE_PAIR)<2)
			{
				break;
			}
			for (int i=0;i<CurNode->Node->mCardCount;i++)
			{
				CurPairNode=m_OutCardNodeHead.mList[CARDTYPE_NODE_PAIR];
				while(CurPairNode!=NULL)
				{
					if (CompareCard(CurNode->Node->GetCardValue(i),CurPairNode->Node->GetCardValue(0))==0)
					{
						ThreeItemCount++;
						break;
					}
					CurPairNode=CurPairNode->next;
				}
			}
			
			if (ThreeItemCount>=CurNode->Node->mCardCount/2)
			{
				//满足条件
				for (int i=0;i<CurNode->Node->mCardCount;i++)
				{
					CurPairNode=m_OutCardNodeHead.mList[CARDTYPE_NODE_PAIR];
					while(CurPairNode!=NULL)
					{
						if (CompareCard(CurNode->Node->GetCardValue(i),CurPairNode->Node->GetCardValue(0))==0)
						{
							//创建三条
							CurPairNode->Node->bCardList[2]=CurNode->Node->GetCardValue(i);
							pNode=NULL;
							CreateOutCardNode(CurPairNode->Node->bCardList,3,CARDTYPE_NODE_THREEITEM,1,pNode);
							TASSERT(pNode!=NULL);

							m_OutCardNodeHead.Push(pNode,CARDTYPE_NODE_THREEITEM);

							CurPairNode=m_OutCardNodeHead.RemoveNode(CARDTYPE_NODE_PAIR,CurPairNode);

							CurNode->Node->bCardList[i]=0;

							continue;
						}
						CurPairNode=CurPairNode->next;
					}
				}

				//处理顺子剩余的牌压
				if (m_OutCardNodeHead.mList[CARDTYPE_NODE_SINGLECARD]==NULL)
				{
					CreateOutCardNode(CARDTYPE_NODE_SINGLECARD,pNode);
					m_OutCardNodeHead.mList[CARDTYPE_NODE_SINGLECARD]=pNode;
				}
				pNode=m_OutCardNodeHead.mList[CARDTYPE_NODE_SINGLECARD];
				for (int i=0;i<CurNode->Node->mCardCount;i++)
				{
					if (CurNode->Node->bCardList[i]!=0)
					{
						pNode->Node->AddCardValue(CurNode->Node->bCardList[i]);
					}
				}

				SortCardList(pNode->Node->bCardList,pNode->Node->mCardCount);

				//删除顺子节点
				CurNode=m_OutCardNodeHead.RemoveNode(CARDTYPE_NODE_PROGRESS,CurNode);
				
				continue;
			}
			CurNode=CurNode->next;
		}

		
	}
	'''
	def AmendOutCardNode_Progress_Pair(self):
		pass

	'''
	void CBaseRobotAction::AmendOutCardNode_Progress_Single()
	{
		OutCardNodePtr CurNode=m_OutCardNodeHead.mList[CARDTYPE_NODE_PROGRESS];
		if (m_OutCardNodeHead.mList[CARDTYPE_NODE_SINGLECARD]==NULL||m_OutCardNodeHead.mList[CARDTYPE_NODE_SINGLECARD]->Node->mCardCount+m_OutCardNodeHead.NodeCount(CARDTYPE_NODE_PAIR)<=1)
		{
			//手中的单牌不存在 或者 个数少于一个
			return ;
		}
		if (CurNode==NULL)
		{
			//不存在顺子
			return ;
		}
		if (!m_FirstOutCard&&m_CurOutCardType==CARDTYPE_NODE_PAIR&&!IsPartner(m_PreOutCarder)&&GetRivalHandCardCount()<=OUTCARD_TIME_MIDTERM_LATE&&GetBigerPairCountSomeCard(m_CurKeyCardValue)<=1)
		{
			return ;
		}
		if (m_OutCardNodeHead.mList[CARDTYPE_NODE_SINGLECARD]->Node->mCardCount+m_OutCardNodeHead.NodeCount(CARDTYPE_NODE_PAIR)-GetThreeItemCount()<=1)
		{
			return ;
		}
		//
		BYTE bCardList[CARDCOUNT_PLAYER]={0};
		int CardCount=m_OutCardNodeHead.mList[CARDTYPE_NODE_SINGLECARD]->Node->mCardCount;
		BYTE bPairCardList[CARDCOUNT_PLAYER]={0};//单牌中用于顺子的牌列表
		int  PairCardCount=0;

		memcpy(bCardList,m_OutCardNodeHead.mList[CARDTYPE_NODE_SINGLECARD]->Node->bCardList,CardCount);
		PairCardCount=GetPairCardList_Amend(bPairCardList);//从对子中获取牌数据

		if (PairCardCount>0)
		{//将对子牌数据拷贝到单牌牌数据中  组成新的单牌数据
			memcpy(&bCardList[CardCount],bPairCardList,PairCardCount);
			CardCount+=PairCardCount;

		}
		//对牌数据进行排序
		SortCardList(bCardList,CardCount);
		//从单牌中获取小于五个的顺子
		BYTE bProgressSingle[10][8]={0};//顺子列表
		int iCount=0;


		for (int i=0;i<CardCount-1;i++)
		{
			if (CompareCard(bCardList[i]+1,bCardList[i+1])==0)
			{
				//至少存在两个牌的顺子
				int SameCount=0;//相同牌值得个数
				bProgressSingle[iCount][SameCount++]=bCardList[i];
				bProgressSingle[iCount][SameCount++]=bCardList[i+1];

				for (int j=i+2;j<CardCount;j++)
				{
					if (CompareCard(bCardList[j-1]+1,bCardList[j])==0)
					{
						bProgressSingle[iCount][SameCount++]=bCardList[j];
					}
					else
					{
						break;
					}
				}

				bProgressSingle[iCount][7]=SameCount;
				i+=SameCount-1;
				iCount++;
			}
		}

		if (iCount<=0)
		{
			//不存在小顺子
			
			//寻找一个单牌 和 顺子 组成 两个大顺子 
			CardCount=m_OutCardNodeHead.mList[CARDTYPE_NODE_SINGLECARD]->Node->mCardCount;
			memcpy(bCardList,m_OutCardNodeHead.mList[CARDTYPE_NODE_SINGLECARD]->Node->bCardList,CardCount);
			CurNode=m_OutCardNodeHead.mList[CARDTYPE_NODE_PROGRESS];
		    PairCardCount=0;
			while(CurNode!=NULL)
			{
				if (CurNode->Node->mCardCount<9)
				{
					CurNode=CurNode->next;
					continue;
				}

				for (int i=0;i<CardCount&&iCount<=0;i++)
				{
					for (int j=4;j<CurNode->Node->mCardCount-4&&iCount<=0;j++)
					{
						if (!CompareCard(bCardList[i],CurNode->Node->GetCardValueByIndex(j)))
						{
							if (!HaveProgress(CurNode->Node->GetCardValueByIndex(j),1,CurNode->Node->mCardCount-j))
							{
								//后面的顺子是最大的顺子
								if (j+1==CurNode->Node->mCardCount-j)
								{
									//两个数字相同
									bProgressSingle[iCount][7]=1;
									bProgressSingle[iCount++][0]=bCardList[i];
									
								}
								else if (!HaveProgress(CurNode->Node->GetCardValue(0),1,j+1))
								{
									bProgressSingle[iCount][7]=1;
									bProgressSingle[iCount++][0]=bCardList[i];
								}
							}
							
						}
					}
				}
				if (iCount>0)
				{
					break;
				}
				CurNode=CurNode->next;
			}
			
			if (iCount<=0)
			{
				//没有找到合适的牌
				return;
			}
		}
		bool bFlag=false;
		CurNode=m_OutCardNodeHead.mList[CARDTYPE_NODE_PROGRESS];
		while(CurNode!=NULL)
		{
			if (CurNode->Node->mCardCount>=6)
			{
				for (int i=0;i<iCount;i++)
				{
					if (ValidCard(bProgressSingle[i][0])&&CompareCard(bProgressSingle[i][0],CurNode->Node->bCardList[0])>=0&&CompareCard(bProgressSingle[i][bProgressSingle[i][7]-1],CurNode->Node->GetCardValue())<=0)
					{
						if (SUBCARDPOINT(bProgressSingle[i][bProgressSingle[i][7]-1],CurNode->Node->GetCardValue(0))>=4&&SUBCARDPOINT(CurNode->Node->GetCardValue(),bProgressSingle[i][0])>=4)
						{
							//可以组成两个顺子
							BYTE bTempCardList[CARDCOUNT_PLAYER]={0};
							int TempCount=0;
							int Index=SUBCARDPOINT(bProgressSingle[i][bProgressSingle[i][7]-1],CurNode->Node->GetCardValue(0))+1;
							for (int j=0;j<bProgressSingle[i][7];j++)
							{
								bTempCardList[TempCount++]=bProgressSingle[i][j];
							}
							for(int j=Index;j<CurNode->Node->mCardCount;j++)
							{
								bTempCardList[TempCount++]=CurNode->Node->bCardList[j];
							}

							OutCardNodePtr pNode=NULL;
							CreateOutCardNode(bTempCardList,TempCount,CARDTYPE_NODE_PROGRESS,TempCount,pNode);
							TASSERT(pNode!=NULL);
							m_OutCardNodeHead.Push(pNode,CARDTYPE_NODE_PROGRESS);

							CurNode->Node->mCardCount=Index;

							//删除牌从单牌列表中
							for (int j=0;j<CardCount;j++)
							{
								for (int k=0;k<bProgressSingle[i][7];k++)
								{
									if (bCardList[j]==bProgressSingle[i][k])
									{
										bCardList[j]=0;
										bProgressSingle[i][k]=0;
										break;
									}
								}

							}
							//标志该小顺子已经用过
							bProgressSingle[i][0]=0;

							//从组顺子成功
							bFlag=true;
						}
					}
				}
			}
			CurNode=CurNode->next;
		}

		if (bFlag)
		{//重新整理单牌和对子牌数据
			int iCount=0;
			BYTE bCardValue=0;

			if (PairCardCount>0)
			{
				//判断用了哪些对子牌数据 并删除对子节点 
				for (int i=0,j=0;i<PairCardCount;i++)
				{
					for (j=0;j<CardCount;j++)
					{
						if (!ValidCard(bCardList[j]))
						{
							continue;
						}
						if (bPairCardList[i]==bCardList[j])
						{
							//找到对子的牌数据
							break;
						}
					}
					if (j>=CardCount)
					{//对子牌数据 被用于顺子中  则 删除对子节点
						CurNode=m_OutCardNodeHead.mList[CARDTYPE_NODE_PAIR];
						while(CurNode!=NULL)
						{
							if (CurNode->Node->bCardList[0]==bPairCardList[i]||CurNode->Node->bCardList[1]==bPairCardList[i])
							{
								//将对子的另一个牌 加入到单牌列表中
								bCardList[CardCount++]=CurNode->Node->GetCardValue();
								//删除对子节点
								m_OutCardNodeHead.RemoveNode(CARDTYPE_NODE_PAIR,CurNode);
								break;
							}
							CurNode=CurNode->next;
						}
					}
				}

				//从单牌中删除对子数据
				CurNode=m_OutCardNodeHead.mList[CARDTYPE_NODE_PAIR];
				int Index=0;
				while(CurNode!=NULL)
				{
					for (int i=0,j=0;i<2;i++)
					{
						for (j=0;j<CardCount;j++)
						{
							if (!ValidCard(bCardList[j]))
							{
								continue;
							}
							if (CurNode->Node->bCardList[i]==bCardList[j])
							{
								bCardList[j]=0;
								break;
							}
						}
					}
					CurNode=CurNode->next;
				}
			}
			CurNode=m_OutCardNodeHead.mList[CARDTYPE_NODE_SINGLECARD];
			TASSERT(CurNode!=NULL);
			iCount=0;
			for (int i=0;i<CardCount;i++)
			{
				if (ValidCard(bCardList[i]))
				{
					CurNode->Node->bCardList[iCount++]=bCardList[i];
				}
			}

			m_OutCardNodeHead.mList[CARDTYPE_NODE_SINGLECARD]->Node->mCardCount=iCount;
		}
	}
	'''
	def AmendOutCardNode_Progress_Single(self):
		pass

	'''
	void CBaseRobotAction::AmendOutCardNode_Progress()
	{
		OutCardNodePtr CurNode=m_OutCardNodeHead.mList[CARDTYPE_NODE_PROGRESS];
		OutCardNodePtr pNode=NULL;

		BYTE bCardList[CARDCOUNT_PLAYER]={0};
		BYTE bCardValue=0;

		if (!m_FirstOutCard&&m_CurOutCardType==CARDTYPE_NODE_PROGRESS)
		{
			//跟牌 且当前出的是顺子 
			return ;
		}
		while(CurNode!=NULL)
		{
			if (CurNode->Node->mCardCount>5)
			{
				//
				bCardValue=GETCARDPOINT(CurNode->Node->bCardList[0]);
				if (3==m_CardData.GetCardValueCount(bCardValue))
				{
					if (CurNode->Node->mCardCount>5)
					{
						if (CheckAmend(bCardValue))
						{
							m_CardData.GetSomeCardData(bCardList,bCardValue);
							pNode=NULL;
							CreateOutCardNode(bCardList,3,CARDTYPE_NODE_THREEITEM,1,pNode);
							m_OutCardNodeHead.Push(pNode,CARDTYPE_NODE_THREEITEM);

							AdjustbCardList(CurNode->Node->bCardList,CurNode->Node->mCardCount,0);
							CurNode->Node->mCardCount--;
						}

					}
				}

				bCardValue=CurNode->Node->bCardList[CurNode->Node->mCardCount-1];
				bCardValue=GETCARDPOINT(bCardValue);
				TASSERT(ValidCard(bCardValue));

				switch(m_CardData.GetCardValueCount(bCardValue))
				{
				case 2:
					{
						//手上有两张同样的牌
						if (bCardValue<CARD_K||m_OutCardNodeHead.mList[CARDTYPE_NODE_PAIR]==NULL)
						{
							//手上没有对子
							break;
						}
						if (m_OutCardNodeHead.mList[CARDTYPE_NODE_PAIR]!=NULL&&CompareCard(m_OutCardNodeHead.mList[CARDTYPE_NODE_PAIR]->Node->bCardList[0],bCardValue)>=0)
						{
							//自己手中存在对子 且大于顺子的最大牌
							break;
						}
						if (CheckAmend(bCardValue))
						{
							m_CardData.GetSomeCardData(bCardList,bCardValue);
							pNode=NULL;
							CreateOutCardNode(bCardList,2,CARDTYPE_NODE_PAIR,1,pNode);
							m_OutCardNodeHead.Push(pNode,CARDTYPE_NODE_PAIR);

							CurNode->Node->mCardCount--;
						}

					}
					break;
				case 3:
					{
						if (CheckAmend(bCardValue))
						{
							m_CardData.GetSomeCardData(bCardList,bCardValue);
							pNode=NULL;
				CreateOutCardNode(bCardList,3,CARDTYPE_NODE_THREEITEM,1,pNode);
							m_OutCardNodeHead.Push(pNode,CARDTYPE_NODE_THREEITEM);

							CurNode->Node->mCardCount--;

						}
					}
					break;
				}//switch

				//分解大的单牌
				
				int SingleCount=GetSmallSingle_Amend();
				while(SingleCount>2&&CurNode->Node->mCardCount>5&&m_CardData.GetBigCard2Count()<SingleCount)
				{
					bCardValue=CurNode->Node->bCardList[CurNode->Node->mCardCount-1];
					if (CCardCounter::HaveBigCard(bCardValue))
					{
						break;
					}

					m_OutCardProgress.mSingleCardList[m_OutCardProgress.mSingleCardCount++]=bCardValue;
					CurNode->Node->mCardCount--;

					SingleCount--;

				}
			}
			if (CurNode->Node->mCardCount>6&&IsLivePair(CurNode->Node->GetCardValue(CurNode->Node->mCardCount-2),pNode)>0)
			{
				if (CompareCard(pNode->Node->GetCardValue(0),CARD_J)>=0||!HaveProgress(pNode->Node->GetCardValue(0),2,1))
				{
					memcpy(bCardList,pNode->Node->bCardList,2);
					bCardList[2]=CurNode->Node->GetCardValue(CurNode->Node->mCardCount-2);
					m_OutCardNodeHead.RemoveNode(CARDTYPE_NODE_PAIR,pNode);

					pNode=NULL;
					CreateOutCardNode(bCardList,3,CARDTYPE_NODE_THREEITEM,1,pNode);
					m_OutCardNodeHead.Push(pNode,CARDTYPE_NODE_THREEITEM);

					m_OutCardProgress.mSingleCardList[m_OutCardProgress.mSingleCardCount++]=CurNode->Node->GetCardValue();
					CurNode->Node->mCardCount-=2;
				}

			}
			CurNode=CurNode->next;
		}

		//合并两个顺子
		if ((m_FirstOutCard&&m_CardData.GetBigCard2Count()<=1||!m_FirstOutCard)&&CompareCard(m_CardData.GetBigestCard(0),CCardCounter::GetBigestCard(0))<0)
		{
			//手中没有大的单牌  则 不合并两个顺子
			return ;
		}
		OutCardNodePtr NextNode=NULL;
		OutCardNodePtr SingleNode=m_OutCardNodeHead.mList[CARDTYPE_NODE_SINGLECARD];//单牌节点
		CurNode=m_OutCardNodeHead.mList[CARDTYPE_NODE_PROGRESS];
		bool Flag=false;
		while(CurNode!=NULL)
		{
			NextNode=CurNode->next;
			if (Get_State(CurNode->Node->mState,OUTCARD_STATE_BIGCARD))
			{
				break;
			}
			while(NextNode!=NULL)
			{
				if (Get_State(NextNode->Node->mState,OUTCARD_STATE_BIGCARD))
				{
					break;
				}
				if (CompareCard(CurNode->Node->GetCardValue(),NextNode->Node->GetCardValue(0))==0&&CCardCounter::HaveLinkProgress(NextNode->Node->GetCardValue(0),1,NextNode->Node->mCardCount))
				{
					//重叠一张牌  则合并
					Flag=true;
					if (SingleNode==NULL)
					{
						memset(bCardList,0,sizeof(bCardList));
						bCardList[0]=NextNode->Node->GetCardValue(0);

						CreateOutCardNode(bCardList,1,CARDTYPE_NODE_SINGLECARD,1,SingleNode);
						TASSERT(SingleNode!=NULL);
						m_OutCardNodeHead.mList[CARDTYPE_NODE_SINGLECARD]=SingleNode;
					}
					else
					{
						SingleNode->Node->AddCardValue(NextNode->Node->GetCardValue(0));
					}

					//合并两个顺子
					memcpy(&CurNode->Node->bCardList[CurNode->Node->mCardCount],&NextNode->Node->bCardList[1],NextNode->Node->mCardCount-1);
					CurNode->Node->mCardCount+=NextNode->Node->mCardCount-1;

					//删除节点
					m_OutCardNodeHead.RemoveNode(CARDTYPE_NODE_PROGRESS,NextNode);
					break;
				}
				NextNode=NextNode->next;
			}

			CurNode=CurNode->next;
		}

		if (Flag)
		{
			TASSERT(SingleNode!=NULL);
			if (SingleNode->Node->mCardCount>1)
			{
				SortCardList(SingleNode->Node->bCardList,SingleNode->Node->mCardCount);
			}

		}
	}
	'''
	def AmendOutCardNode_Progress(self):
		pass

	'''
	void CBaseRobotAction::AmendOutCardNode_Pair()
	{
		OutCardNodePtr CurNode=m_OutCardNodeHead.mList[CARDTYPE_NODE_PAIR];
		OutCardNodePtr CurLinkNode=NULL;

		if (m_OutCardNodeHead.mList[CARDTYPE_NODE_LINKPAIR]==NULL)
		{
			return ;
		}
		bool bFlag;
		while(CurNode!=NULL)
		{
			CurLinkNode=m_OutCardNodeHead.mList[CARDTYPE_NODE_LINKPAIR];

			bFlag=false;
			while (CurLinkNode!=NULL)
			{
				if (GETCARDPOINT(CurNode->Node->bCardList[0])+1==GETCARDPOINT(CurLinkNode->Node->bCardList[0])||GETCARDPOINT(CurNode->Node->bCardList[0])==GETCARDPOINT(CurLinkNode->Node->bCardList[0])+CurLinkNode->Node->mCardCount)
				{
					memcpy(&CurLinkNode->Node->bCardList[2*CurLinkNode->Node->mCardCount],CurNode->Node->bCardList,2);
					CurLinkNode->Node->mCardCount++;

					SortCardList(CurLinkNode->Node->bCardList,CurLinkNode->Node->mCardCount*2);

					m_OutCardNodeHead.RemoveNode(CARDTYPE_NODE_PAIR,CurNode);
					bFlag=true;
					break;
				}

				CurLinkNode=CurLinkNode->next;
			}
			if (bFlag)
			{
				CurNode=m_OutCardNodeHead.mList[CARDTYPE_NODE_PAIR];
			}
			else
			{
				CurNode=CurNode->next;
			}

		}
	}
	'''
	def AmendOutCardNode_Pair(self):
		pass

	'''
	void CBaseRobotAction::AmendOutCardNode_LinkPair_Single()
	{
		if (!m_FirstOutCard&&m_CurOutCardType==CARDTYPE_NODE_LINKPAIR)
		{
			return;
		}
		OutCardNodePtr CurNode=m_OutCardNodeHead.mList[CARDTYPE_NODE_LINKPAIR],pNode=NULL;
		BYTE bDelCardList[CARDCOUNT_PLAYER]={0};
		BYTE bDelCount=0;
		BYTE bCardList[CARDCOUNT_PLAYER]={0};
		BYTE bCardValue=0;
		if (m_OutCardNodeHead.mList[CARDTYPE_NODE_LINKPAIR]==NULL||m_OutCardNodeHead.mList[CARDTYPE_NODE_SINGLECARD]==NULL)
		{
			//基本条件不满足
			return ;
		}
		
		if (m_OutCardNodeHead.mList[CARDTYPE_NODE_SINGLECARD]->Node->mCardCount<2)
		{
			return;
		}
		CurNode=m_OutCardNodeHead.mList[CARDTYPE_NODE_LINKPAIR];
		while(CurNode!=NULL)
		{
			int i=0,iCount=0;
			for (i=0;i<CurNode->Node->mCardCount;i++)
			{
				if (IsExitCardInSingleCardList(CurNode->Node->bCardList[i*2]))
				{
					iCount++;
				}
				else if(iCount>1)
				{
					break;
				}
				else
				{
					iCount=0;
				}
			}
			if (iCount>1)
			{
				TASSERT(CurNode->Node->mCardCount-i<3);
				TASSERT(i-iCount+1<3);

				if (iCount>=CurNode->Node->mCardCount/2)
				{
					//满足条件
					i-=iCount;
					for (int j=0;j<iCount;j++)
					{
						memcpy(&bCardList[j*3],&CurNode->Node->bCardList[(i+j)*2],2);
						bCardValue=IsExitCardInSingleCardList(CurNode->Node->bCardList[(i+j)*2]);
						TASSERT(bCardValue!=0);
						bCardList[j*3+2]=bCardValue;

						bDelCardList[bDelCount++]=bCardValue;
					}

					//创建三顺
					CreateOutCardNode(bCardList,iCount*3,CARDTYPE_NODE_THREEPROGRESS,iCount,pNode);
					m_OutCardNodeHead.Push(pNode,CARDTYPE_NODE_THREEPROGRESS);
					//创建对子
					for (int j=0;j<i;j++)
					{
						memcpy(bCardList,&CurNode->Node->bCardList[j*2],2);
						CreateOutCardNode(bCardList,2,CARDTYPE_NODE_THREEPROGRESS,1,pNode);
						m_OutCardNodeHead.Push(pNode,CARDTYPE_NODE_PAIR);
					}
					for (int j=i+iCount;j<CurNode->Node->mCardCount;j++)
					{
						memcpy(bCardList,&CurNode->Node->bCardList[j*2],2);
						CreateOutCardNode(bCardList,2,CARDTYPE_NODE_THREEPROGRESS,1,pNode);
						m_OutCardNodeHead.Push(pNode,CARDTYPE_NODE_PAIR);
					}

					//删除连对
					CurNode=m_OutCardNodeHead.RemoveNode(CARDTYPE_NODE_LINKPAIR,CurNode);
					continue;
				}
			}
			CurNode=CurNode->next;
		}

		if (bDelCount>0)
		{
			//删除单牌
			if (bDelCount==m_OutCardNodeHead.mList[CARDTYPE_NODE_SINGLECARD]->Node->mCardCount)
			{
				m_OutCardNodeHead.mList[CARDTYPE_NODE_SINGLECARD]=NULL;
			}
			else
			{
				CurNode=m_OutCardNodeHead.mList[CARDTYPE_NODE_SINGLECARD];
				CurNode->Node->mCardCount=RemoveCardList(CurNode->Node->bCardList,CurNode->Node->mCardCount,bDelCardList,bDelCount);
			}
		}
	}
	'''
	def AmendOutCardNode_LinkPair_Single(self):
		pass

	'''
	void CBaseRobotAction::AmendOutCardNode_LinkPair()
	{
		OutCardNodePtr pNode=NULL;
		OutCardNodePtr CurNode=NULL;
		OutCardNodePtr SingleNode=m_OutCardNodeHead.mList[CARDTYPE_NODE_SINGLECARD];
		BYTE bCardList[CARDCOUNT_PLAYER]={0};
		if (m_OutCardNodeHead.NodeCount(CARDTYPE_NODE_LINKPAIR)<=0)
		{
			//手中没有连对
			return ;
		}
		if (!m_FirstOutCard&&m_CurOutCardType==CARDTYPE_NODE_PAIR&&!IsPartner(m_PreOutCarder)&&!IsExitBigCard_Amend(CARDTYPE_NODE_PAIR))
		{
			//当前出的是对子 且手中的对子没有大牌
			CurNode=m_OutCardNodeHead.mList[CARDTYPE_NODE_LINKPAIR];
			while(CurNode!=NULL)
			{
				if (IsSplitLinkPair(CurNode,m_CurKeyCardValue)||CompareCard(CurNode->Node->GetCardValue(0),m_CurKeyCardValue)>0&&(!HaveProgress(CurNode->Node->GetCardValue(0),2,1)||!IsLandlorder()&&GetRivalHandCardCount()==1&&CompareCard(CurNode->Node->GetCardValue(),m_CurKeyCardValue)>0))
				{
					BYTE bCardValue=0;
					for (int i=0;i<CurNode->Node->mCardCount;i++)
					{
						memcpy(bCardList,&CurNode->Node->bCardList[i*2],2);
						if (SingleNode!=NULL&&SingleNode->Node->mCardCount>0&&-1!=IsLiveSingleCard(SingleNode->Node->bCardList,SingleNode->Node->mCardCount,bCardList[0],bCardValue))
						{
							RemoveCardList(SingleNode->Node->bCardList,SingleNode->Node->mCardCount,&bCardValue,1);
							SingleNode->Node->mCardCount--;

							bCardList[2]=bCardValue;
							CreateOutCardNode(bCardList,3,CARDTYPE_NODE_THREEITEM,1,pNode);
							m_OutCardNodeHead.Push(pNode,CARDTYPE_NODE_THREEITEM);
						}
						else
						{
							CreateOutCardNode(&CurNode->Node->bCardList[i*2],2,CARDTYPE_NODE_PAIR,1,pNode);
							m_OutCardNodeHead.Push(pNode,CARDTYPE_NODE_PAIR);
						}
						
					}
					Set_State(pNode->Node->mState,OUTCARD_STATE_SIGNOUTED);

					m_OutCardNodeHead.RemoveNode(CARDTYPE_NODE_LINKPAIR,CurNode);
					break;
				}
				CurNode=CurNode->next;
			}
		}
		int SmallPair=GetSmallPairCount_Amend();//获取小对子的个数
		if (!m_FirstOutCard&&m_CurOutCardType==CARDTYPE_NODE_LINKPAIR&&!IsPartner(m_PreOutCarder)&&SmallPair<=2)
		{
			return;
		}
		if (SmallPair==1&&m_OutCardNodeHead.mList[CARDTYPE_NODE_SINGLECARD]==NULL)
		{
			return;
		}
		if (m_OutCardNodeHead.NodeCount(CARDTYPE_NODE_PAIR)<=1&&m_OutCardNodeHead.NodeCount(CARDTYPE_NODE_SINGLECARD)<=0&&CompareCard(m_CardData.GetBigestCard(0),CCardCounter::GetBigestCard(0))>0)
		{
			//手中没有单牌  且 手中有最大的单牌
			return ;
		}
		AmendOutCardNode_LinkPair_Progress();//连对拆成 两个顺子


		//连对的 第一个 或者 最后一个 存在三条

		CurNode=m_OutCardNodeHead.mList[CARDTYPE_NODE_LINKPAIR];
		BYTE bCardValue=0;
		while(CurNode!=NULL)
		{
			//
			if (CurNode->Node->mCardCount>3)
			{
				bCardValue=CurNode->Node->bCardList[CurNode->Node->mCardCount*2-2];
				if (m_CardData.GetCardValueCount(GETCARDPOINT(bCardValue))==3)
				{
					if (CanFormThree_Amend(CurNode->Node))
					{
						AmendLinkPairFormThree_Amend(CurNode->Node,true);
						CurNode->Node->mCardCount--;
					}
				}
			}

			if (CurNode->Node->mCardCount>3)
			{
				bCardValue=CurNode->Node->bCardList[0];
				if (m_CardData.GetCardValueCount(GETCARDPOINT(bCardValue))==3)
				{
					if (CanFormThree_Amend(CurNode->Node,false))
					{
						AmendLinkPairFormThree_Amend(CurNode->Node,false);
						memmove(CurNode->Node->bCardList,&CurNode->Node->bCardList[2],2*(CurNode->Node->mCardCount-1));
						CurNode->Node->mCardCount--;
					}
				}
			}
			else
			{
				bool bFlag=false;
				int BigCount=0;
				int BigThreeCount=0;
				int ThreeCount=0;
				if (CurNode->Node->mCardCount==3)
				{
					//连对 Q K A
					if (m_OutCardNodeHead.GetSingleCardCount()>0)
					{
						if (CompareCard(CurNode->Node->bCardList[0],CARD_Q)>=0&&SmallPair>0||(m_FirstOutCard||m_CurOutCardType!=CARDTYPE_NODE_LINKPAIR)&&m_OutCardProgress.GetSmallSingleCardCount()>1&&CompareCard(CurNode->Node->GetCardValue(0),CARD_10)>=0)
						{
							if (IsExitCardInSingleCardList(CurNode->Node->bCardList[0])||IsExitCardInSingleCardList(CurNode->Node->bCardList[2]))
							{
								bFlag=true;
							}
							else if (IsExitCardInSingleCardList(CurNode->Node->bCardList[4]))
							{
								bFlag=true;
							}
							else
							{
								//从顺子中获取牌数据
								BYTE bCardValue=GetCardFromProgress_Amend(CurNode->Node->bCardList[0]);
								if (bCardValue==0)
								{
									bCardValue=GetCardFromProgress_Amend(CurNode->Node->bCardList[2]);
								}
								if (bCardValue==0)
								{
									bCardValue=GetCardFromProgress_Amend(CurNode->Node->bCardList[4]);
								}
								if (bCardValue!=0)
								{
									if (m_OutCardNodeHead.mList[CARDTYPE_NODE_SINGLECARD]==NULL)
									{
										pNode=NULL;
										CreateOutCardNode(CARDTYPE_NODE_SINGLECARD,pNode);
									}
									pNode=m_OutCardNodeHead.mList[CARDTYPE_NODE_SINGLECARD];
									pNode->Node->AddCardValue(bCardValue);
									if (pNode->Node->mCardCount>1)
									{
										SortCardList(pNode->Node->bCardList,pNode->Node->mCardCount);
									}

									bFlag=true;
								}
							}
						}
					}
					
					ThreeCount=0;
					if(!bFlag)
					{

						for (int i=0;i<3;i++)
						{
							if (IsExitCardInSingleCardList(CurNode->Node->bCardList[i*2]))
							{
								ThreeCount++;
								if (!HaveProgress(CurNode->Node->bCardList[0],3,1))
								{
									BigThreeCount++;
								}
							}
							else if (!HaveProgress(CurNode->Node->bCardList[0],2,1))
							{
								BigCount++;
							}
						}
						if (GetRivalHandCardCount()==1&&ThreeCount>0)
						{
							bFlag=true;
						}
						else if (ThreeCount>1&&CompareCard(CurNode->Node->GetCardValue(0),CARD_8)>=0)
						{
							//连对中 存在一个以上的三条
							bFlag=true;
						}
					}
				}
				if (SmallPair>0)
				{
					if (!bFlag&&m_OutCardNodeHead.NodeCount(CARDTYPE_NODE_LINKPAIR)==1&&!CCardCounter::HaveLinkProgress(CurNode->Node->GetCardValue(2),2,1))
					{
						bFlag=true;
					}
				}

				if (!bFlag&&ThreeCount>0)
				{
					if (BigThreeCount==ThreeCount&&BigCount>0||BigCount==CurNode->Node->mCardCount-ThreeCount)
					{
						bFlag=true;

					}
				}
				if (bFlag)
				{
					//可以拆开连对
					BYTE bTempCardList[CARDCOUNT_PLAYER]={0};
					int TempCount=m_OutCardNodeHead.GetSingleCardCount();
					if (TempCount>0)
					{
						memcpy(bTempCardList,m_OutCardNodeHead.mList[CARDTYPE_NODE_SINGLECARD]->Node->bCardList,TempCount);

						for (int i=0;i<3;i++)
						{
							for (int j=0;j<TempCount;j++)
							{
								if (ValidCard(bTempCardList[i]))
								{
									if (CompareCard(bTempCardList[j],CurNode->Node->bCardList[i*2])==0)
									{
										BYTE bThreeList[4]={0};
										memcpy(bThreeList,&CurNode->Node->bCardList[i*2],2);
										bThreeList[2]=bTempCardList[j];
										//删除单牌
										bTempCardList[j]=0;

										//创建三条
										pNode=NULL;
										CreateOutCardNode(bThreeList,3,CARDTYPE_NODE_THREEITEM,1,pNode);
										TASSERT(pNode!=NULL);
										m_OutCardNodeHead.Push(pNode,CARDTYPE_NODE_THREEITEM);
										CurNode->Node->bCardList[i*2]=0;
									}
								}
							}
						}
					}

					//其他的组成对子
					for (int i=0;i<3;i++)
					{
						if (ValidCard(CurNode->Node->bCardList[i*2]))
						{
							pNode=NULL;
							CreateOutCardNode(&CurNode->Node->bCardList[i*2],2,CARDTYPE_NODE_PAIR,1,pNode);
							m_OutCardNodeHead.Push(pNode,CARDTYPE_NODE_PAIR);
						}
					}

					if (TempCount>0)
					{
						//剔除单牌
						pNode=m_OutCardNodeHead.mList[CARDTYPE_NODE_SINGLECARD];
						//
						int iCount=0;
						for (int i=0;i<TempCount;i++)
						{
							if (ValidCard(bTempCardList[i]))
							{
								pNode->Node->bCardList[iCount++]=bTempCardList[i];
							}
						}

						pNode->Node->mCardCount=iCount;
					}


					//删除连对
					CurNode=m_OutCardNodeHead.RemoveNode(CARDTYPE_NODE_LINKPAIR,CurNode);
					continue;
				}//if (bFlag)
			}

			CurNode=CurNode->next;
		}

		//
		if (SmallPair>1)
		{
			OutCardNodePtr CurNode=m_OutCardNodeHead.mList[CARDTYPE_NODE_LINKPAIR];
			while(CurNode!=NULL&&SmallPair>1)
			{
				if (CurNode->Node->mCardCount==3)
				{
					//三连对
					if (CompareCard(CurNode->Node->bCardList[0],CARD_10)>0)
					{
						for (int i=0;i<3;i++)
						{
							pNode=NULL;
							CreateOutCardNode(&CurNode->Node->bCardList[i*2],2,CARDTYPE_NODE_PAIR,1,pNode);
							TASSERT(pNode!=NULL);
							m_OutCardNodeHead.Push(pNode,CARDTYPE_NODE_PAIR);
						}

						SmallPair-=3;

						CurNode=m_OutCardNodeHead.RemoveNode(CARDTYPE_NODE_LINKPAIR,CurNode);

						continue;
					}
				}
				else if(CurNode->Node->mCardCount>3)
				{
					//多连对
					while(CurNode->Node->mCardCount>3&&SmallPair>1)
					{
						if (CompareCard(CurNode->Node->bCardList[CurNode->Node->mCardCount*2-2],CARD_Q)>=0)
						{
							pNode=NULL;
							CreateOutCardNode(&CurNode->Node->bCardList[(CurNode->Node->mCardCount-1)*2],2,CARDTYPE_NODE_PAIR,1,pNode);
							TASSERT(pNode!=NULL);
							m_OutCardNodeHead.Push(pNode,CARDTYPE_NODE_PAIR);

							CurNode->Node->mCardCount--;
							SmallPair--;
						}
						else
						{
							break;
						}
					}
				}
				CurNode=CurNode->next;
			}
		}
		else if (SmallPair==1)
		{
			//一个小对
			if (CompareCard(m_OutCardNodeHead.mList[CARDTYPE_NODE_PAIR]->Node->bCardList[0],CARD_8)<=0)
			{
				OutCardNodePtr CurNode=m_OutCardNodeHead.mList[CARDTYPE_NODE_LINKPAIR];
				while(CurNode!=NULL)
				{
					if (CurNode->Node->mCardCount>3&&CurNode->Node->mCardCount!=5)
					{
						//多连对
						if (CompareCard(CurNode->Node->bCardList[(CurNode->Node->mCardCount-1)*2],CARD_J)>0)
						{

							pNode=NULL;
							CreateOutCardNode(&CurNode->Node->bCardList[(CurNode->Node->mCardCount-1)*2],2,CARDTYPE_NODE_PAIR,1,pNode);
							TASSERT(pNode!=NULL);
							m_OutCardNodeHead.Push(pNode,CARDTYPE_NODE_PAIR);

							CurNode->Node->mCardCount--;
							break;
						}
					}
					CurNode=CurNode->next;
				}
			}

		}
	}
	'''
	def AmendOutCardNode_LinkPair(self):
		pass

	'''
		void CBaseRobotAction::AmendOutCardNode_MergeLinkPair()
	{
		OutCardNodePtr CurNode=m_OutCardNodeHead.mList[CARDTYPE_NODE_LINKPAIR],NextNode=NULL;

		while(CurNode!=NULL&&CurNode->next!=NULL)
		{
			NextNode=CurNode->next;
			while(NextNode!=NULL)
			{
				if (GETCARDPOINT(CurNode->Node->bCardList[0])==GETCARDPOINT(NextNode->Node->bCardList[0])+NextNode->Node->mCardCount||GETCARDPOINT(CurNode->Node->bCardList[0])+CurNode->Node->mCardCount==GETCARDPOINT(NextNode->Node->bCardList[0]))
				{
					memcpy(&CurNode->Node->bCardList[CurNode->Node->mCardCount*2],NextNode->Node->bCardList,NextNode->Node->mCardCount*2);
					CurNode->Node->mCardCount+=NextNode->Node->mCardCount;
					SortCardList(CurNode->Node->bCardList,CurNode->Node->mCardCount*2);

					NextNode=m_OutCardNodeHead.RemoveNode(CARDTYPE_NODE_LINKPAIR,NextNode);
					continue;
				}
				NextNode=NextNode->next;
			}

			CurNode=CurNode->next;
		}

	}
	'''
	def AmendOutCardNode_MergeLinkPair(self):
		pass

	'''
	void CBaseRobotAction::AmendOutCardNode_Progress_Pair_Single()
	{
		if (m_OutCardNodeHead.mList[CARDTYPE_NODE_PAIR]==NULL||m_OutCardNodeHead.mList[CARDTYPE_NODE_PROGRESS]==NULL||m_OutCardNodeHead.mList[CARDTYPE_NODE_SINGLECARD]==NULL)
		{
			//不存在对子 、单牌或者 顺子 直接返回
			return ;
		}
		if (!m_FirstOutCard&&m_CurOutCardType==CARDTYPE_NODE_PAIR&&!IsPartner(m_PreOutCarder))
		{
			if (GetBigerPairCountSomeCard(m_CurKeyCardValue)<1||m_OutCardNodeHead.NodeCount(CARDTYPE_NODE_PAIR)==1)
			{
				return ;
			}
		}
		OutCardNodePtr CurNode=m_OutCardNodeHead.mList[CARDTYPE_NODE_PROGRESS],CurPairNode=NULL;

		int PairCount=m_OutCardNodeHead.NodeCount(CARDTYPE_NODE_PAIR);
		//保存单牌数据
		BYTE bSingleCardList[CARDCOUNT_PLAYER]={0};
		int SingleCount=m_OutCardNodeHead.mList[CARDTYPE_NODE_SINGLECARD]->Node->mCardCount;
		memcpy(bSingleCardList,m_OutCardNodeHead.mList[CARDTYPE_NODE_SINGLECARD]->Node->bCardList,SingleCount);
		//匹配标志 
		bool bFlag=false;

		BYTE bCardValue=0;
		int DisCardValue=0;
		while(CurNode!=NULL)
		{
			CurPairNode=m_OutCardNodeHead.mList[CARDTYPE_NODE_PAIR];
			while(CurPairNode!=NULL)
			{
				if (PairCount==1||CurPairNode!=m_OutCardNodeHead.GetTailNode(CARDTYPE_NODE_PAIR))
				{
					BYTE bCardList[CARDCOUNT_PLAYER]={0};
					int iCount=0;
					if (CompareCard(CurNode->Node->bCardList[0]+CurNode->Node->mCardCount,CurPairNode->Node->bCardList[0])==0)
					{
						bCardList[iCount++]=CurPairNode->Node->GetCardValue();
						bCardValue=bCardList[iCount-1];
						DisCardValue=1;
					}
					else if (CompareCard(CurNode->Node->bCardList[0]+CurNode->Node->mCardCount+1,CurPairNode->Node->bCardList[0])==0)
					{
						if (IsLiveSingleCard(bSingleCardList,SingleCount,CurPairNode->Node->GetCardValue(0)-1,bCardValue)!=-1)
						{
							bCardList[iCount++]=bCardValue;
							bCardList[iCount++]=CurPairNode->Node->GetCardValue();
							bCardValue=bCardList[iCount-1];
							DisCardValue=1;
						}
					}
					else if (CompareCard(CurNode->Node->GetCardValue(0)-1,CurPairNode->Node->bCardList[0])==0)
					{
						bCardList[iCount++]=CurPairNode->Node->GetCardValue();
						bCardValue=bCardList[0];
						DisCardValue=-1;
					}
					else if (CompareCard(CurNode->Node->GetCardValue(0)-2,CurPairNode->Node->bCardList[0])==0)
					{
						if (IsLiveSingleCard(bSingleCardList,SingleCount,CurPairNode->Node->GetCardValue(0)+1,bCardValue)!=-1)
						{
							bCardList[iCount++]=CurPairNode->Node->GetCardValue();
							bCardList[iCount++]=bCardValue;
							bCardValue=bCardList[0];
							DisCardValue=-1;
						}
					}

					if (iCount>0)
					{
						//找到满足条件的对子
						for (int i=0;i<SingleCount;i++)
						{
							if (ValidCard(bSingleCardList[i])&&CompareCard(bSingleCardList[i],bCardValue+DisCardValue)==0)
							{
								//找到匹配的单牌
								bCardList[iCount++]=bSingleCardList[i];
								bCardValue+=DisCardValue;
								if (DisCardValue==-1)
								{
									i=-1;
								}
							}
						}

						if (iCount>1)
						{
							//找到匹配的对子和单牌
				
							//延长顺子
							memcpy(&CurNode->Node->bCardList[CurNode->Node->mCardCount],bCardList,iCount);
							CurNode->Node->mCardCount+=iCount;
							//对顺子进行排序
							SortCardList(CurNode->Node->bCardList,CurNode->Node->mCardCount);
							//删除单牌
							for (int i=0;i<SingleCount;i++)
							{
								for (int j=0;j<iCount;j++)
								{
									if (bSingleCardList[i]==bCardList[j])
									{
										bSingleCardList[i]=0;
									}
								}
							}
							//删除对子
							bSingleCardList[SingleCount++]=CurPairNode->Node->bCardList[0];

							CurPairNode=m_OutCardNodeHead.RemoveNode(CARDTYPE_NODE_PAIR,CurPairNode);

							bFlag=true;
							continue;
						}
					}

				}
				CurPairNode=CurPairNode->next;
			}
			CurNode=CurNode->next;
		}

		if (bFlag)
		{
			//重组顺子成功

			//删除单牌
			int iCount=0;
			for (int i=0;i<SingleCount;i++)
			{
				if (ValidCard(bSingleCardList[i]))
				{
					m_OutCardNodeHead.mList[CARDTYPE_NODE_SINGLECARD]->Node->bCardList[iCount++]=bSingleCardList[i];
				}
			}
			m_OutCardNodeHead.mList[CARDTYPE_NODE_SINGLECARD]->Node->mCardCount=iCount;
		}
	}
	void CBaseRobotAction::AmendOutCardNode_Progress_Single_Pair(BYTE Kind/* =0 */)
	{
		if (m_OutCardNodeHead.mList[CARDTYPE_NODE_SINGLECARD]==NULL||m_OutCardNodeHead.mList[CARDTYPE_NODE_PROGRESS]==NULL)
		{
			return ;
		}
		if (!m_FirstOutCard&&m_CurOutCardType==CARDTYPE_NODE_PROGRESS)
		{
			return;
		}
		OutCardNodePtr SingleNode=m_OutCardNodeHead.mList[CARDTYPE_NODE_SINGLECARD],CurNode=NULL,pNode=NULL;
		int BigPairCardCount=0;
		if (Kind==1)
		{
			CurNode=m_OutCardNodeHead.mList[CARDTYPE_NODE_PAIR];
			while(CurNode!=NULL)
			{
				if (!CCardCounter::HaveLinkProgress(CurNode->Node->GetCardValue(),2,1))
				{
					BigPairCardCount++;
				}
				CurNode=CurNode->next;
			}
		}
		BYTE bSinleCardList[CARDCOUNT_PLAYER]={0};
		int SingleCardCount=SingleNode->Node->mCardCount;
		memcpy(bSinleCardList,SingleNode->Node->bCardList,SingleCardCount);
		BYTE bCardList[4]={0};
		for (int i=0;i<SingleCardCount;i++)
		{
			CurNode=m_OutCardNodeHead.mList[CARDTYPE_NODE_PROGRESS];
			bCardList[0]=0;
			while(CurNode!=NULL)
			{
				if (CurNode->Node->mCardCount>5)
				{
					if (CompareCard(bSinleCardList[i],CurNode->Node->GetCardValue(0))==0)
					{//单牌和顺子的第一个 组成对子
						bCardList[0]=bSinleCardList[i];
						bCardList[1]=CurNode->Node->GetCardValue(0);

						AdjustbCardList(CurNode->Node->bCardList,CurNode->Node->mCardCount,0);
						CurNode->Node->mCardCount--;

					}
					else if (CompareCard(bSinleCardList[i],CurNode->Node->GetCardValue())==0)
					{//单牌和顺子的最后一个组成对子
						bCardList[0]=bSinleCardList[i];
						bCardList[1]=CurNode->Node->GetCardValue();
						CurNode->Node->mCardCount--;
					}
					if (ValidCard(bCardList[0]))
					{
						bSinleCardList[i]=0;

						//创建对子
						pNode=NULL;
						CreateOutCardNode(bCardList,2,CARDTYPE_NODE_PAIR,1,pNode);
						m_OutCardNodeHead.Push(pNode,CARDTYPE_NODE_PAIR);

						break;
					}
				}

				CurNode=CurNode->next;
			}

			if (Kind==1&&m_OutCardNodeHead.NodeCount(CARDTYPE_NODE_PAIR)/2>=BigPairCardCount)
			{
				break;
			}
		}

		//更新牌数据
		int iCount=0;
		for (int i=0;i<SingleCardCount;i++)
		{
			if (ValidCard(bSinleCardList[i]))
			{
				SingleNode->Node->bCardList[iCount++]=bSinleCardList[i];
			}
		}

		if (iCount<=0)
		{
			//没有单牌了
			m_OutCardNodeHead.RemoveNode(CARDTYPE_NODE_SINGLECARD,SingleNode);
		}
		else
		{//更新单牌的个数
			SingleNode->Node->mCardCount=iCount;
		}
	}
	'''
	def AmendOutCardNode_Progress_Pair_Single(self):
		pass

	'''
	void CBaseRobotAction::AmendOutCardNode_LinkPair_Pair_Three()
	{
		if (m_OutCardNodeHead.NodeCount(CARDTYPE_NODE_THREEITEM)<=0||m_OutCardNodeHead.NodeCount(CARDTYPE_NODE_LINKPAIR)<=0||m_OutCardNodeHead.NodeCount(CARDTYPE_NODE_PAIR)<=0)
		{
			return ;
		}

		if (!m_FirstOutCard/*&&(m_CurOutCardType==CARDTYPE_NODE_PAIR||m_CurOutCardType==CARDTYPE_NODE_THREEITEM)*/)
		{
			return ;
		}

		OutCardNodePtr CurLinkPair=m_OutCardNodeHead.mList[CARDTYPE_NODE_LINKPAIR],CurPairNode=NULL,CurThreeNode=NULL;
		OutCardNodePtr SingleNode=m_OutCardNodeHead.mList[CARDTYPE_NODE_SINGLECARD];

		if (SingleNode!=NULL&&SingleNode->Node->mCardCount>3)
		{
			return ;
		}
		int ThreeCount=0;
		BYTE bCardValue=0;
		while(CurLinkPair!=NULL)
		{
			CurThreeNode=m_OutCardNodeHead.mList[CARDTYPE_NODE_THREEITEM];
			if (CurThreeNode==NULL)
			{
				break;
			}
			ThreeCount=1;
			if (SingleNode!=NULL&&SingleNode->Node->mCardCount>0)
			{
				for (int i=0;i<CurLinkPair->Node->mCardCount;i++)
				{
					if (-1!=IsLiveSingleCard(SingleNode->Node->bCardList,SingleNode->Node->mCardCount,CurLinkPair->Node->bCardList[i*2],bCardValue))
					{
						ThreeCount++;
					}
				}
				if (ThreeCount>1)
				{
					CurLinkPair=CurLinkPair->next;
					continue;
				}
			}

			if (CurThreeNode!=NULL&&(!HaveProgress(CurThreeNode->Node->GetCardValue(0),3,1)||CompareCard(CurThreeNode->Node->bCardList[0],CARD_J)>=0))
			{
				CurThreeNode=NULL;
			}
			while(CurThreeNode!=NULL)
			{
				if (CompareCard(CurThreeNode->Node->GetCardValue()+1,CurLinkPair->Node->GetCardValue(0))==0||CompareCard(CurThreeNode->Node->GetCardValue(),CurLinkPair->Node->GetCardValue()+1)==0)
				{
					CurPairNode=m_OutCardNodeHead.mList[CARDTYPE_NODE_PAIR];

					while(CurPairNode!=NULL)
					{
						if (!HaveProgress(CurPairNode->Node->GetCardValue(),2,1)||CompareCard(CurPairNode->Node->GetCardValue(),CARD_K)>=0)
						{
							CurPairNode=CurPairNode->next;
							continue;
						}
						if (CompareCard(CurPairNode->Node->GetCardValue()+1,CurThreeNode->Node->GetCardValue(0))==0||CompareCard(CurPairNode->Node->GetCardValue(),CurThreeNode->Node->GetCardValue()+1)==0)
						{
							//对子 、三条 和 连对 可以组成新连对
							break;
						}
						CurPairNode=CurPairNode->next;
					}

					if (m_CardData.GetCardDataCount()==CurLinkPair->Node->mCardCount*2+3||CurPairNode!=NULL)
					{
						//重组连对
						//将三条 加入到连对中
						CurLinkPair->Node->AddCardList(CurThreeNode->Node->bCardList,2,2);

						//将另外一个 牌加入到单牌中
						if (SingleNode==NULL)
						{
							//创建单牌节点
							CreateOutCardNode(CARDTYPE_NODE_SINGLECARD,SingleNode);
							m_OutCardNodeHead.Push(SingleNode,CARDTYPE_NODE_SINGLECARD);
						}

						TASSERT(SingleNode!=NULL);

						SingleNode->Node->AddCardValue(CurThreeNode->Node->GetCardValue());

						if (CurPairNode!=NULL)
						{
							CurLinkPair->Node->AddCardList(CurPairNode->Node->bCardList,2,2);
							m_OutCardNodeHead.RemoveNode(CARDTYPE_NODE_PAIR,CurPairNode);
						}

						//删除三条
						CurThreeNode=m_OutCardNodeHead.RemoveNode(CARDTYPE_NODE_THREEITEM,CurThreeNode);

						//排序连对
						SortCardList(CurLinkPair->Node->bCardList,CurLinkPair->Node->mCardCount*2);

						continue;
					}
				}


				CurThreeNode=CurThreeNode->next;
			}

			CurLinkPair=CurLinkPair->next;
		}
	}
	'''
	def AmendOutCardNode_LinkPair_Pair_Three(self):
		pass

