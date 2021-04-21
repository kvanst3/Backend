import random

choices = ['rock', 'paper', 'scissors']

print("Welcome to Janken2.0!")
game_on = True
while game_on == True:
    usr_ready = input("Ready?! [y/n] \n")
    while usr_ready == 'y':
        usr_choice = input("What will you choose? Rock, Paper, or Scissors?\n")
        if usr_choice not in choices:
            print("unoknown")
            continue
        cp_choice = random.choice(choices)
        print(f"Your opponent chose {cp_choice}!")
        if usr_choice == cp_choice:
            print("It's a DRAW!!")
        elif usr_choice == "rock" and cp_choice == "scissors":
            print("You WIN!!")
        elif usr_choice == "paper" and cp_choice == "rock":
            print("You WIN!!")
        elif usr_choice == "scissors" and cp_choice == "paper":
            print("You WIN!!")
        else:
            print("You LOOSE!") 
            
        if input("Ready?! [y/n] \n") == 'n':
            usr_ready = 'n'
            if input('Quit? [y/n] \n') == 'y':
                game_on = False
