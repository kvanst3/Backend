from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file='pomodoro/tomato.png')
canvas.create_image(100, 112, image=tomato_image)
canvas.create_text(100, 145, text="00:00", fill="white", font=(FONT_NAME, 32, "bold"))
canvas.grid(column=2, row=2)

# Labels
reset_num = 1

timer_label = Label(text="Timer", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
timer_label.grid(column=2, row=1)

check_label = Label(text=reset_num * "✔", font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW)
check_label.grid(column=2, row=4)

# Buttons

def start_action():
    print("start")

def reset_action():
    reset_num += 1

start_bt = Button(text="start", command=start_action, bg="white", highlightthickness=0)
start_bt.grid(column=1, row=3)

reset_bt = Button(text="reset", command=reset_action, bg="white", highlightthickness=0)
reset_bt.grid(column=3, row=3)


window.mainloop()
