from os import system
from art import logo


def add_bidder(name, bid):
    bidders.append({
        'name': name,
        'value': {
            'bid': int(bid),
        },
    })


def print_winner(bidders_list):
    winning_bid = 0
    winner = {}
    for bidder in bidders_list:
        if bidder['value']['bid'] > winning_bid:
            winning_bid = bidder['value']['bid']
            winner = bidder
    return winner


bidders = []
more_bidder = True
print(logo)
while more_bidder:
    name = input('What is your name?\n')
    bid = input('What is your bid?\n')
    add_bidder(name, bid)
    if input("More bidders? [y/n]?\n") == 'n':
        more_bidder = False
    system('clear')
winner = print_winner(bidders)
print(f"The winner of this bid is {winner['name']}, with a bid of {winner['value']['bid']}")
