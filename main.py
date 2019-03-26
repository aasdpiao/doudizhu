# -*- coding:UTF-8 -*-

from Cards import Cards
from Player import Player

if __name__ == "__main__":
    cards =  Cards()
    players = []
    card_group, landlord_cards = cards.deal_poker()
    for i in range(3):
        print("==========================", i, "============================")
        player = Player()
        players.append(player)
        player.set_cards(card_group[i])
        print(player)
    print("===========================landlord_cards=======================")
    for x in landlord_cards:
        print(x)


