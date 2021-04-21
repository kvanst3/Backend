import random
from os import system
from random_word import RandomWords
r = RandomWords()

# generates a list of 100 random words - stores a random word into var
def gen_word():
    words = r.get_random_words(hasDictionaryDef="true", includePartOfSpeech="noun,verb", limit=100)
    word = random.choice(words).lower()
    return word

# generates a guessing dispay of the word to be guessed
def display_guess(word):
    guessed_word = ['_'] * len(word)
    return guessed_word

# checks if the guessed letter appears somewhere in the word - if yes, replace the guessing display appropriate position with the guessed letter
def check_matches(word, guessed_word, guessed_letter, lives):
    guessed_right = False

    for i, l in enumerate(word):
        if guessed_letter == l:
            guessed_word[i] = l
            guessed_right = True

    if guessed_right is False:
        lives -= 1

    return lives

def check_success(guessed_word):
    if '_' not in guessed_word:
        return True


stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

keep_playing = True
while keep_playing:
    lives = 6
    letters_guessed = []
    print("let's play hangman! Generating new set of words...")
    word = gen_word()
    # print(word)
    guessed_word = display_guess(word)
    print(' '.join(guessed_word))

    while lives > 0:
        try:
            guessed_letter = input("Guess a letter:\n").lower()[0]
            system('clear')
        except Exception as e:
            print("Invalid input")
            print(type(e))
            continue
        if guessed_letter not in letters_guessed:
            letters_guessed += guessed_letter
            lives = check_matches(word, guessed_word, guessed_letter, lives)
            print(' '.join(guessed_word))
            print(stages[lives])
            print(f"attempted letters: {letters_guessed}")
            if check_success(guessed_word):
                print("congratulation! You Win!\n")
                break
            elif lives <= 0:
                print(f"Sorry, you ran out of lives! You Lose!\nThe word was: {word}")
        else:
            print("You've already tried that. Try another one!")

    if input("Wanna play again? [n/y]\n") == "n":
        keep_playing = False
