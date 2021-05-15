from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
img = PhotoImage(file="/home/k/Desktop/Python_projects/Python projects/password_manager/logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=2, row=1)

website_label = Label(text="Website", bg="white")
website_label.grid(column=1, row=2)

usr_label = Label(text="Email/Username", bg="white")
usr_label.grid(column=1, row=3)

password_label = Label(text="Password", bg="white")
password_label.grid(column=1, row=4)




window.mainloop()
