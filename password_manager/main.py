#!/usr/bin/env python3
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

FONT = 10
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, END)

    password_letters = [choice(LETTERS) for _ in range(randint(8, 10))]
    password_numbers = [choice(NUMBERS) for _ in range(randint(2, 4))]
    password_symbols = [choice(SYMBOLS) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    web = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(web) > 0 and len(password) > 0:
        save_message = messagebox.askokcancel(title=web, message=f"Details:\nEmail: {email}\nPassword: {password}")
        if save_message:
            with open("password_manager/passwords.txt", mode="a") as file:
                file.write(f"{web}, {email}, {password}\n")

            website_entry.delete(0, END)
            password_entry.delete(0, END)
    else:
        messagebox.showerror(title="Error", message= "You need to populate all the fields before hitting Add")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
img = PhotoImage(file="/home/k/Desktop/Python_projects/Python projects/password_manager/logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:", bg="white", pady=5, font=("Arial", FONT))
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:", bg="white", pady=5, font=("Arial", FONT))
email_label.grid(column=0, row=2)

password_label = Label(text="Password:", bg="white", pady=5, font=("Arial", FONT))
password_label.grid(column=0, row=3)

fake_label = Label(text=" ", bg="white", pady=5, font=("Arial", FONT))
fake_label.grid(column=0, row=4)

# Entries
website_entry = Entry(width=36)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=36)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "email@email.com")

password_entry = Entry(width=24)
password_entry.grid(column=1, row=3)

# Buttons
password_generation_button = Button(text="Generate", command=generate_password, bg="white", font=("Arial", FONT), width=9)
password_generation_button.grid(column=2, row=3)

add_button = Button(text="Add", command=save_password, bg="white", width=38, font=("Arial", FONT))
add_button.grid(column=1, row=4, columnspan=2)



window.mainloop()
