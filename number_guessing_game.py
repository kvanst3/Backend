import random


def check_guess(num, guess):
    if guess > num:
        return 1
    elif guess < num:
        return 2
    else:
        return 3


def lives(level, lives):
    if level == 'easy':
        return lives + 10
    elif level == 'hard':
        return lives + 5


def game_on():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    num = random.choice(range(1, 101))

    try:
        level = input("Chose a difficulty. type 'easy' or 'hard': ")
        remaining_lives = 0
        remaining_lives = lives(level, remaining_lives)

        while remaining_lives > 0:
            print(f"You have {remaining_lives} attempts remaining to guess the number.")

            try:
                guess = int(input("Take a guess: "))
                hint = check_guess(num, guess)
            except Exception:
                print("Invalid input.")
                continue

            if hint == 1:
                print("Too high.")
                remaining_lives -= 1
            elif hint == 2:
                print("Too low.")
                remaining_lives -= 1
            else:
                print(f"You got it! The answer was {num}.")
                break

        if remaining_lives <= 0:
            print(f"Sorry, you lose... The answer was: {num}")

        if input("Play again? ['y' to keep playing, any other key to exit.]") == 'y':
            game_on()
    except Exception:
        print("invalid input")
        game_on()


game_on()
