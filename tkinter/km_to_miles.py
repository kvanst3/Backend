import tkinter
from tkinter import font

window = tkinter.Tk()
window.title("First GUI")
window.minsize(width=200, height=80)
window.config(padx=10, pady=10)

# Title Label

label = tkinter.Label(text="new text here", font=("Arial"))
label.config(text="Convert Km to Miles")
label.grid(column=1, row=0)

# KM label

km_label = tkinter.Label(text="Km", font="Arial")
km_label.grid(column=3, row=1)

# Button


def click_button():
    usr_input = int(input_field.get())
    result.config(text=f"{round(usr_input * 1.609, 2)} Miles")


button = tkinter.Button(text="Convert!", command=click_button)
button.grid(column=2, row=2)

# Entry

input_field = tkinter.Entry(width=10)
input_field.grid(column=2, row=1)

# Result Label

result = tkinter.Label(text="0 Miles", font="Arial")
result.grid(column=3, row=3)



window.mainloop()