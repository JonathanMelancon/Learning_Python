import random


card_names:list[str] =["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", " Jack", "Queen", "King" ]
card_values:list[int]= [14, 2, 3 ,4 ,5 ,6 ,7 ,8 ,9 ,10 ,11, 12, 13]
card_shapes:list[str] = ["Heart", "Spades", "Diamond", "Club"]

class Card:

    def __init__(self, name, shape, value, graphic) -> None:
        self.name:str = name
        self.shape:str = shape
        self.value:int = value
        self.graphic = graphic

def create_deck():

    card_deck:list[Card] = []
    i:int = 0

    for shapes in card_shapes:
        for names in card_names:
            values:int = card_values[i]
            card_deck.append(Card(names,shapes,values,None))
            i += 1
        i = 0

    return(card_deck)

card_deck = create_deck()

def shuffle_deck():
    i = 0
    for _ in card_deck:
        rand = random.randrange(0,51)
        card_deck[i], card_deck[rand] = card_deck[rand], card_deck[i]
        i += 1
    return(card_deck)

card_deck = shuffle_deck()

        
# # class Player:

# #     def __init__(self, name , cards):
# #         self.name:str = name
# #         self.cards:list = cards\

print("new")

for cards in card_deck:
    print(cards.__dict__)
 

print (len(card_deck))