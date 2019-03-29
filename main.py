# -*- coding:UTF-8 -*-

from Cards import Cards
from Player import Player

if __name__ == "__main__":
    cards =  Cards()
    players = []
    card_group, landlord_cards = cards.DealPoker()
    for i in range(3):
        player = Player()
        player.SetSelfDeskStation(i)
        players.append(player)
        player.SetCardList(card_group[i])
        player.WriteHandCardList()
    print("===========================landlord_cards=======================")
    for x in landlord_cards:
        print(x)
    for player in players:
        player.ParseHandCardInfo()


