import random

def create_deck_of_cards():
    shapes:list[str] = ["heart", "spades", "clubs", "diamond"]

class Card:

    def __init__(self, name, shape, value, graphic) -> None:
        self.name:str = name
        self.shape:str = shape
        self.value:int = value
        self.graphic = graphic
        
class Player:

    def __init__(self, name , cards):
        self.name:str = name
        self.cards:list = cards

player_1_name:str =input("Please input your name and press enter")

player1 = Player(player_1_name, player_one_cards) #need to create deck of cards and suffle it