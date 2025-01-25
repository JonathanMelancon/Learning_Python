import random
import sys

card_names: list[str] = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen",
                         "King"]
card_values: list[int] = [14, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
card_shapes: list[str] = ["Hearts", "Spades", "Diamonds", "Clubs"]


class Card:

    def __init__(self, name, shape, value, graphic) -> None:
        self.name: str = name
        self.shape: str = shape
        self.value: int = value
        self.graphic = graphic


def create_deck():
    card_deck: list[Card] = []
    i: int = 0

    for shapes in card_shapes:
        for names in card_names:
            values: int = card_values[i]
            card_deck.append(Card(names, shapes, values, None))
            i += 1
        i = 0

    return card_deck


new_deck = create_deck()


def shuffle(card_deck):
    i = 0
    for _ in card_deck:
        rand = random.randrange(0, 51)
        card_deck[i], card_deck[rand] = card_deck[rand], card_deck[i]
        i += 1
    return card_deck


starting_deck = shuffle(new_deck)


class Player:

    def __init__(self, name, cards):
        self.name: str = name
        self.cards: list = cards

    def list_cards(self):
        i = 0
        for _ in self.cards:
            print(self.cards[i].name + ' of ' + self.cards[i].shape)
            i += 1

    def card_description(self, i):
        return self.cards[i].name + ' of ' + self.cards[i].shape

    def card_count(self):
        return len(self.cards)


player1 = Player('Player 1', starting_deck[0:25])
player2 = Player('Player 2', starting_deck[26:51])


def draw():
    if player1.card_count() > 0 and player2.card_count() > 0:
        print('Player 1 plays ' + player1.card_description(0))
        print('Player 2 plays ' + player2.card_description(0))
        return [player1.cards[0], player2.cards[0]]


def compare_values():
    if draw()[0].value > draw()[1].value:
        print(draw()[0].value, draw()[1].value)
        print('Player 1 wins this round')
        player1.cards.append(player2.cards.pop(0))
        player1.cards.append(player1.cards.pop(0))

    elif draw()[0].value < draw()[1].value:
        print('Player 2 wins this round')
        print(draw()[0].value, draw()[1].value)
        player2.cards.append(player1.cards.pop(0))
        player2.cards.append(player2.cards.pop(0))

    elif draw()[0].value == draw()[1].value:
        print('Battle! First player to draw a ' + draw()[0].name + ' wins the battle!')

    else:
        print(draw()[0].value, draw()[1].value)
        print('wtf')

    print('Player 1 has ' + str(player1.card_count()) + ' cards')
    print('Player 2 has ' + str(player2.card_count()) + ' cards')


def show_card_count(player):
    print(player + ' has ' + str(player.card_count()) + ' cards')


def play_round():
    draw()
    compare_values()


key = ''

while key != 'e':

    play_round()
    if player1.card_count() < 52 and player2.card_count() < 52:
        key = input('Press enter to draw next cards')

    if key == 'e':
        sys.exit()

    elif player1.card_count() == 52:
        print('Player one wins!')
        sys.exit()

    elif player2.card_count() == 52:
        print('Player two wins!')
        sys.exit()

# print(player1.card_description())
# player1.list_cards()


# print (len(card_deck))
# print (player1.cards[1].name)
