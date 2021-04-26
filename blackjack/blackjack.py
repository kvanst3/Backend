import random
import time
import sys
from os import system
from art import deck, logo


def deal_card(deck, player):
    pronoun = 'Dealer drew' if player == dealer_cards else 'You were dealt'
    card = random.choice(list(deck.items()))
    card[1]['remaining'] -= 1
    while card[1]['remaining'] < 0:
        card = random.choice(list(deck.items()))
    player.append(card)
    if len(player) > 2:
        print(f"{pronoun} a {card[0]}...\n")
        score = check_score(player)
        print(f"Current score: {score}\n")
        if score > 21:
            return False


def initial_dealing(deck, player, dealer):
    [deal_card(deck, player) for _ in range(2)]
    [deal_card(deck, dealer) for _ in range(2)]


def current_cards(player_cards):
    cards = []
    for card in player_cards:
        cards.append(card[0])
    return cards


def check_score(player_cards):
    score = 0
    for card in player_cards:
        score += card[1]['value']
    if score > 21 and 1 in dict(player_cards):
        score -= 10
    return score


def dealer_time(dealer_cards, player_cards, deck):
    print("The dealer is revealing her hand")
    [slow_output('.') for _ in range(3)]
    print(f"\nDealer hand: {current_cards(dealer_cards)}")
    dealer_score = check_score(dealer_cards)
    player_score = check_score(player_cards)
    while dealer_score < player_score:
        if deal_card(deck, dealer_cards) is False:
            print('The Dealer Busted! You Win!')
            return False
        dealer_score = check_score(dealer_cards)
        [slow_output('.') for _ in range(3)]


def check_winner(player, dealer):
    player_score = check_score(player)
    dealer_score = check_score(dealer)
    if player_score > dealer_score:
        return "Congratualetion! You Win!"
    elif player_score == dealer_score:
        return 'Draw!'
    else:
        return "Sorry. You lost.."


def slow_output(char):
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.4)


def game():
    print(logo)
    initial_dealing(deck, player_cards, dealer_cards)
    print(f"\tYour cards: {current_cards(player_cards)}, current score: {check_score(player_cards)}")
    print(f"\tComputer's first card: {dealer_cards[0][0]}")
    while True:
        if input("Type 'y' to get another card, any other key to pass:\n") == 'y':
            if deal_card(deck, player_cards) is False:
                print("BUSTED!! You lose.\n")
                break
        else:
            if dealer_time(dealer_cards, player_cards, deck) is False:
                break
            else:
                print(check_winner(player_cards, dealer_cards))
                break
    if input("Type 'y' to play again, any other key to quit BlackJack2000\n") == 'y':
        player_cards.clear()
        dealer_cards.clear()
        system('clear')
        game()


player_cards = []
dealer_cards = []
game()
