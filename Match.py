# -*- coding:UTF-8 -*-

from Cards import Cards
from Player import Player
from Common import ShowCard
import random

class Match(object):
    def __init__(self, model):
        self.model = model
        self.end = False
        self.last_move = "start"
        self.players = []
        self.game_status = 0   #游戏开始  抢地主  出牌  结算

    def GameInit(self):
        for i in range(3):
            player = Player()
            player.SetDeskStation(i)
            self.players.append(player)
        self.players[0].SetNextPlayer(self.players[1])
        self.players[1].SetNextPlayer(self.players[2])
        self.players[2].SetNextPlayer(self.players[0])
        self.landlord = self.players[0]
        self.landlord.SetFirstCallLord()


    def GameStart(self):
        cards = Cards()
        card_group, landlord_cards = cards.DealPoker()
        for i, player in enumerate(self.players):
            player.SetCardList(card_group[i])
            player.WriteHandCardList()
        print("===========================landlord_cards=======================")
        ShowCard(landlord_cards)
        self.game_status = 1
        self.game_score = 0
        while self.game_status == 1:
            if self.landlord.CallLandlord(self.game_score):
                self.game_score = self.landlord.GetCallScore()
                self.landlord.AddBottomCardList(landlord_cards)
                self.game_status = 2
            self.landlord = self.landlord.GetNextPlayer()

        print(self.landlord.GetDeskStation())

if __name__ == "__main__":
    match = Match(random)
    match.GameInit()
    match.GameStart()
