import random

class Player:

    def __init__(self, name , cards):
        self.name:str = name
        self.cards:list = cards

player_1_name:str =input("Please input your name and press enter")

player1 = Player(player_1_name, player_one_cards) #need to create deck of cards and suffle it