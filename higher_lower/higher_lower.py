import random
from art import logo, vs
from game_data import data
from os import system


def generate_celeb():
    return random.choice(data)


def prompt(value1, value2):
    print(logo)
    print(f"\nCompare A: {value1['name']}, {value1['description']}, from {value1['country']}.")
    print(vs)
    print(f"\nCompare B: {value2['name']}, {value2['description']}, from {value2['country']}.")


def compare_values(usr_choice, value1, value2):
    winner = value2
    if value1["follower_count"] > value2["follower_count"]:
        winner = value1
    if usr_choice == winner:
        return winner
    else:
        return False


def game_on():
    usr_right = True
    initial_value = generate_celeb()
    score = 0
    while usr_right:
        vs_value = generate_celeb()
        if score > 0:
            print(f"You're right! Current score: {score}.")
        prompt(initial_value, vs_value)
        usr_input = input("Who has more followers? Type 'a' or 'b: ")
        final_input = initial_value if usr_input == 'a' else vs_value
        initial_value = compare_values(final_input, initial_value, vs_value)
        if initial_value is False:
            print(f"Sorry... Score: {score}, before you miserably failed.")
            break
        else:
            score += 1
        system('clear')
    if (input("Type 'y' to play again, any other key to exit.\n")) == 'y':
        game_on()


game_on()
