import random


def check_guess(num, guess, remaining_lives):
    if guess > num:
        print("Too high.")
        return remaining_lives - 1
    elif guess < num:
        print("Too low.")
        return remaining_lives - 1
    else:
        print(f"You got it! The answer was {num}.")
        return num


def lives(level):
    if level == 'easy':
        return 10
    elif level == 'hard':
        return 5


def game_on():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    num = random.choice(range(1, 101))

    try:
        level = input("Chose a difficulty. type 'easy' or 'hard': ")
        remaining_lives = lives(level)
        guess = 0

        while remaining_lives > 0 and guess is not num:
            print(f"You have {remaining_lives} attempts remaining to guess the number.")

            try:
                guess = int(input("Take a guess: "))
                remaining_lives = check_guess(num, guess, remaining_lives)
            except Exception:
                print("Invalid input.")
                continue

        if remaining_lives <= 0:
            print(f"Sorry, you lose... The answer was: {num}")

        if input("Play again? ['y' to keep playing, any other key to exit.]") == 'y':
            game_on()
    except Exception:
        print("invalid input")
        game_on()


game_on()
