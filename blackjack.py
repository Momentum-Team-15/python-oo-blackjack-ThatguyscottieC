# Write your blackjack game here.

import random

# make all the cards
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
          'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

# boolean to help with loops
playing = True

# make class cards


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit

# shuffle the deck and deal out the cards


class Deck:
    def __init__(self):
        self.deck = []  # Empty list
        for suit in suits:
            for rank in ranks:
                # build card objects and put them in the list
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ' '  # Empty string
        for card in self.deck:
            deck_comp += '\n ' + card. __str__()
            # add each Card then print the string
            return 'The deck has: ' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        # pop takes out the object the returns list
        return single_card

# us the dictionary above to get the values of cards


class Hand:
    def __init__(self):
        self.cards = []  # empty list
        self.value = 0  # start at 0
        self.aces = 0  # make the aces special

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1
# lets make the aces work properly

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

# lets itch that betting habit


class Chips:
    def __init__(self):
        self.total = 1000  # start with 1000 chips
        self.bet = 0
# what happens when you win

    def win_bet(self):
        self.total += self.bet
        return self.total
# what happens when you lose

    def lose_bet(self):
        self.total -= self.bet
        return self.total

    def push_bet(self):
        self.total == self.bet
        return self.total


# shut up and take my money
player_chips = Chips()  # start at 1000


def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("What's your bet? "))
        except ValueError:
            print('Sorry, bet must be an integer!')
        else:
            if chips.bet > chips.total:
                # you can't bet what you don't have
                print('Sorry, bet was over', chips.total)
            else:
                break

# how we define gameplay


def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing  # this will help with the while loop below

    while True:
        x = input("Would you like to Hit or Stand? Enter 'h' or 's' ")

        if x[0]. lower() == 'h':
            hit(deck, hand)

        elif x[0]. lower() == 's':
            print("Player stands. Dealer is playing.")
            playing = False

        else:
            print("Please try again.")
            continue
        break

# this will show some of the cards but hide one dealer card


def show_some(player, dealer):
    print("\nDealer's Cards: ")
    print(" <card hidden> ")
    print('', dealer.cards[1])
    print("\nPlayer's Cards:", *player.cards, sep='\n ')
    print("Player's Hand =", player.value)

# this will show all the cards and who will win


def show_all(player, dealer):
    print("\nDealer's Cards:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =", dealer.value)
    print("\nPlayers's Cards:", *player.cards, sep='\n ')
    print("Player's Hand =", player.value)

# lets figure out who wins


def player_busts(player, dealer, chips):
    print("Player bust!")
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print("Player wins!")
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print("Dealer bust!")
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print("Dealer wins!")
    chips.lose_bet()


def push(player, dealer, chips):
    print(" Dealer and Player Tie!")
    chips.push_bet()


while True:
    # Create and shuffle then deal two cards to both player and dealer
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    # Lets get to betting

    # Take their money
    take_bet(player_chips)
    # show some of the cards while hiding one of the dealers cards
    show_some(player_hand, dealer_hand)

    if dealer_hand.value == 21:
        dealer_wins(player_hand, dealer_hand, player_chips)

    if player_hand.value == 21:
        player_wins(player_hand, dealer_hand, player_chips)

    while playing:  # calling the hit or stand function above

        hit_or_stand(deck, player_hand)

        show_some(player_hand, dealer_hand)
        # if player bust stop there
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break
    # continuation
    if player_hand.value <= 21:
        # if the dealer has less than 17 make them hit
        while dealer_hand.value < 17:
            hit(deck, dealer_hand)
        # then show everyones hands
        show_all(player_hand, dealer_hand)
        # make the dealer loose if the get more than 21
        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)
        # if the dealer has more than the player the dealer wins
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)
        # if the player has more than the dealer than player wins
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
        # if the get the same value than no one wins
        else:
            push(player_hand, dealer_hand, player_chips)
    # lets show how much money they have
    print("\nPlayer's Chips are", player_chips.total)
    # then ask if they want to play again
    new_game = input("Would you like to play again? Enter 'y' or 'n' ")
    # if they choose yes then continue
    if new_game[0].lower() == 'y':
        playing = True
        continue
    # if they choose no then stop
    else:
        print("Better Luck next Time!")
        break
