#!/usr/bin/env python3
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

FONT = 10
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
JSON = '/home/k/Desktop/Python_projects/Python projects/password_manager/passwords.json'
# ---------------------------- JSON WRITE ------------------------------- #
def write_json(data):
    with open(JSON, mode="w") as file:
        json.dump(data, file, indent=4)
# ---------------------------- SEARCH JSON ------------------------------- #
def search_json():
    search = website_entry.get().lower()
    try:
        with open(JSON) as file:
            result = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message=f"You currently have no saved password for {search.title()}.")
    else:
        if search in result:
            messagebox.showinfo(title=search.title(), message=f"Email: {result[search]['email']}\nPassword: {result[search]['password']}")
            pyperclip.copy(result[search]['password'])
        else:
            messagebox.showinfo(title="Error", message="No information match.")
        
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
    web = website_entry.get().lower()
    email = email_entry.get()
    password = password_entry.get()
    json_data = {
        web: {
            "email": email,
            "password": password,
        }
    }

    if len(web) > 0 and len(password) > 0:
        try:
            with open(JSON, mode="r") as file:
                data = json.load(file)
        except FileNotFoundError:
            write_json(json_data)
        else:
            # alternatively: if web in data: yada yada yada
            try:
                data[web]
            except KeyError:
                data.update(json_data)
                write_json(data)
            else:
                update = messagebox.askyesno(title="WARNING!", message="You already have a password for this website.\nAre you sure you want to update the password?")
                if update:
                    data.update(json_data)
                    write_json(data)
        finally:
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
website_entry = Entry(width=24)
website_entry.grid(column=1, row=1)
website_entry.focus()

email_entry = Entry(width=36)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "email@email.com")

password_entry = Entry(width=24)
password_entry.grid(column=1, row=3)

# Buttons
search_button = Button(text="Search", command=search_json, bg="white", font=("Arial", FONT), width=9)
search_button.grid(column=2, row=1)

password_generation_button = Button(text="Generate", command=generate_password, bg="white", font=("Arial", FONT), width=9)
password_generation_button.grid(column=2, row=3)

add_button = Button(text="Add", command=save_password, bg="white", width=38, font=("Arial", FONT))
add_button.grid(column=1, row=4, columnspan=2)



window.mainloop()
