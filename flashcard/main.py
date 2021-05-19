from tkinter import *
from tkinter import messagebox
from random import choice
import pandas

ran_word = {}

BACKGROUND_COLOR = "#B1DDC6"
# ---------------------------- CSV TO DATA ------------------------------- #
data = pandas.read_csv("flashcard/data/french_words.csv")
data_dict = data.to_dict('records')
# ---------------------------- RANDOM WORD ------------------------------- #
def generate_card():
    global ran_word, flip_timer
    window.after_cancel(flip_timer)
    ran_word = choice(data_dict)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=f"{ran_word['French']}", fill="black")
    canvas.itemconfig(card_bg, image=img_front)

    flip_timer = window.after(3000, flip_card)
# ---------------------------- SHOW TRANSLATION ------------------------------- #
def flip_card():
    canvas.itemconfig(card_bg, image=img_back)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=f"{ran_word['English']}", fill="white")
# ---------------------------- REMOVE FROM DECK ------------------------------- #
def remove_card():
    global data
    data = data.drop(data_dict.index(ran_word))
    print("removing this card from deck.")
    generate_card()
# ---------------------------- NEXT CARD ------------------------------- #
def next_card():
    generate_card()

# ---------------------------- UPDATE CSV ------------------------------- #
def update_csv():
    pass

# ---------------------------- ON CLOSE ------------------------------- #
def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        update_csv()
        window.destroy()
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)


canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
img_front = PhotoImage(file="flashcard/images/card_front.png")
img_back = PhotoImage(file="flashcard/images/card_back.png")
card_bg = canvas.create_image(400, 263, image=img_front)
card_title = canvas.create_text(400, 150, text=f"Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
green_img = PhotoImage(file="flashcard/images/right.png")
green_button = Button(image=green_img, highlightthickness=0, command=remove_card)
green_button.grid(row=1, column=0)

red_img = PhotoImage(file="flashcard/images/wrong.png")
red_button = Button(image=red_img, highlightthickness=0, command=next_card)
red_button.grid(row=1, column=1)

generate_card()


window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()
