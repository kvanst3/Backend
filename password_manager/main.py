from tkinter import *

FONT = 10
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    print("generating...")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    print("saving...")

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
email_entry = Entry(width=36)
email_entry.grid(column=1, row=2, columnspan=2)
password_entry = Entry(width=24)
password_entry.grid(column=1, row=3)

# Buttons
password_generation_button = Button(text="Generate", command=generate_password, bg="white", font=("Arial", FONT), width=9)
password_generation_button.grid(column=2, row=3)

add_button = Button(text="Add", command=save_password, bg="white", width=38, font=("Arial", FONT))
add_button.grid(column=1, row=4, columnspan=2)



window.mainloop()
