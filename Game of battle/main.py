import random
import sys

card_names: list[str] = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen",
                         "King"]
card_values: list[int] = [14, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
card_shapes: list[str] = ["Hearts", "Spades", "Diamonds", "Clubs"]

round_number: [int] = 1
war_number: [int] = 0


class Card:

    def __init__(self, name, shape, value, graphic) -> None:
        self.name: str = name
        self.shape: str = shape
        self.value: int = value
        self.graphic = graphic

    def card_description(self):
        return str(self.name + ' of ' + self.shape)


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
        rand = random.randrange(0, len(card_deck))
        card_deck[i], card_deck[rand] = card_deck[rand], card_deck[i]
        i += 1
    return card_deck


starting_deck = shuffle(new_deck)

print(len(starting_deck))


class CardPlayer:

    def __init__(self, name, cards):
        self.name: str = name
        self.cards: list = cards

    def list_cards(self):
        i = 0
        for _ in self.cards:
            print(self.cards[i].name + ' of ' + self.cards[i].shape)
            i += 1

    def card_count(self):
        return len(self.cards)


current_card: int = 0
pile1: [Card] = []
pile2: [Card] = []
winner: CardPlayer

player1 = CardPlayer('Player 1', starting_deck[0:26])
player2 = CardPlayer('Player 2', starting_deck[26:52])


def check_win():
    if player1.card_count() == 52:
        print('Player 1 wins the game!')
        sys.exit(0)
    elif player2.card_count() == 52:
        print('Player 2 wins the game!')
        sys.exit(0)


def draw():
    global pile1
    global pile2

    pile1.insert(0, (player1.cards.pop(0)))
    pile2.insert(0, (player2.cards.pop(0)))


def show_card_description():
    print('Player 1 plays ' + pile1[0].card_description())
    print('Player 2 plays ' + pile2[0].card_description())


def battle():
    global winner

    if player1.card_count() < 52 and player2.card_count() < 52:

        if pile1[0].value > pile2[0].value:
            print('Player 1 wins this round')
            winner = player1

        elif pile1[0].value < pile2[0].value:
            print('Player 2 wins this round')
            winner = player2

        elif pile1[0].value == pile2[0].value:
            war()

        else:
            print('SOMETHING WENT WRONG')


    else:
        print('Error, one player has no card left')
    # print('true battle winner value is' + winner.name)


def war():
    global war_number

    print('A war begins!')

    war_factor: int = 4

    if player1.card_count()<war_factor:
        print("Player 1 doesn't have enough card to enter battle. Player 2 wins!")
        sys.exit(0)

    if player2.card_count()<war_factor:
        print("Player 2 doesn't have enough card to enter battle. Player 1 wins!")
        sys.exit(0)

    for i in range(war_factor):
        draw()
    print('Player 1 and Player 2 place ' + str(war_factor - 1) + ' cards face down on the table')
    print('Player one places ' + pile1[0].card_description() + ' face up on the table')
    print('Player two places ' + pile2[0].card_description() + ' face up on the table')
    battle()
    swap_cards()
    war_number += 1


def swap_cards():
    for cards in pile1:
        winner.cards.append(cards)
    for cards in pile2:
        winner.cards.append(cards)
    pile1.clear()
    pile2.clear()


def show_card_count():
    print(player1.name + ' has ' + str(player1.card_count()) + ' cards')
    print(player2.name + ' has ' + str(player2.card_count()) + ' cards')


def play_round():
    check_win()
    draw()
    show_card_description()
    battle()
    swap_cards()
    show_card_count()


key = ''

while key != 'e':

    print(player1.card_count())
    print(player2.card_count())

    play_round()
    if player1.card_count() < 52 and player2.card_count() < 52:
        # key = input('Press enter to draw next cards')
        print('Round number ' + str(round_number))
        print('War number ' + str(war_number))
        round_number += 1

    if key == 'e':
        sys.exit()

    if round_number%100==0:
        shuffle(player1.cards)
        shuffle(player2.cards)

    elif player1.card_count() == 52:
        print('Player one wins!')
        sys.exit()

    elif player2.card_count() == 52:
        print('Player two wins!')
        sys.exit()
