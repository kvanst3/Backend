from tkinter import *
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
# ---------------------------- CSV TO JSON(maybe) ------------------------------- #
# ---------------------------- RANDOM WORD ------------------------------- #
# ---------------------------- COUNT DOWN ------------------------------- #
# ---------------------------- SHOW TRANSLATION ------------------------------- #
# ---------------------------- REMOVE FROM DECK ------------------------------- #
def remove_card():
    print("removing this card from deck.")
# ---------------------------- NEXT CARD ------------------------------- #
def next_card():
    print("here's a new card.")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
img = PhotoImage(file="flashcard/images/card_front.png")
canvas.create_image(400, 263, image=img)
canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Labels

# Buttons
green_img = PhotoImage(file="flashcard/images/right.png")
green_button = Button(image=green_img, highlightthickness=0, command=next_card)
green_button.grid(row=1, column=0)

red_img = PhotoImage(file="flashcard/images/wrong.png")
red_button = Button(image=red_img, highlightthickness=0, command=remove_card)
red_button.grid(row=1, column=1)


window.mainloop()
