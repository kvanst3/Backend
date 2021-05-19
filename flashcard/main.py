from tkinter import *
from random import choice
import pandas

BACKGROUND_COLOR = "#B1DDC6"
# ---------------------------- CSV TO DATA ------------------------------- #
data = pandas.read_csv("flashcard/data/french_words.csv")
data_dict = data.to_dict('records')
# ---------------------------- RANDOM WORD ------------------------------- #
def generate_word():
    ran_word = choice(data_dict)
    canvas.itemconfig(word, text=f"{ran_word['French']}")
    # canvas.create_text(400, 263, text=f"{ran_word['French']}", font=("Ariel", 60, "bold"))
# ---------------------------- COUNT DOWN ------------------------------- #
# ---------------------------- SHOW TRANSLATION ------------------------------- #
# ---------------------------- REMOVE FROM DECK ------------------------------- #
def remove_card():
    print("removing this card from deck.")
    generate_word()
# ---------------------------- NEXT CARD ------------------------------- #
def next_card():
    print("here's a new card.")
    generate_word()
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
img = PhotoImage(file="flashcard/images/card_front.png")
canvas.create_image(400, 263, image=img)
canvas.create_text(400, 150, text=f"French", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Labels

# Buttons
green_img = PhotoImage(file="flashcard/images/right.png")
green_button = Button(image=green_img, highlightthickness=0, command=next_card)
green_button.grid(row=1, column=0)

red_img = PhotoImage(file="flashcard/images/wrong.png")
red_button = Button(image=red_img, highlightthickness=0, command=remove_card)
red_button.grid(row=1, column=1)

generate_word()


window.mainloop()
