# -*- coding:UTF-8 -*-
############################################
#              玩家类                      #
############################################
class OutCardNode(object):
	def __init__(self):
		pass

	def __cmp__(self, other):
		rank = self.card_node.GetCardValue().rank
		other_rank = other.card_node.GetCardValue().rank
		if rank < other_rank:
			return -1
		elif rank > other_rank:
			return 1
		else:
			return 0

	def SetCardNode(self,card_node):
		self.card_node = card_node

	def GetCardNode(self):
		return self.card_node