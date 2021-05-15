from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer = None
reps = 0
checks = 0

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_action():
    window.after_cancel(timer)
    global reps, checks
    reps = 0
    checks = 0
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text='Timer', fg=GREEN)
    check_label.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_action():
    global reps
    reps += 1

    if reps % 8 == 0:
        count_down_to = LONG_BREAK_MIN
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down_to = SHORT_BREAK_MIN
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down_to = WORK_MIN
        timer_label.config(text="Work", fg=GREEN)

    count_down(count_down_to * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    mins = math.floor(count / 60)
    if mins < 10:
        mins = f"0{mins}"
    secs = count % 60
    if secs < 10:
        secs = f"0{secs}"

    canvas.itemconfig(timer_text, text=f"{mins}:{secs}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        global checks
        if reps % 2 != 0:
            checks += 1
            check_label.config(text=checks * "✔")
        window.lift()
        start_action()
        
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file='pomodoro/tomato.png')
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 140, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=2, row=2)

# Labels

timer_label = Label(text="Timer", font=(FONT_NAME, 44), fg=GREEN, bg=YELLOW)
timer_label.grid(column=2, row=1)

check_label = Label(text=checks * "✔", font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW)
check_label.grid(column=2, row=4)

# Buttons
start_bt = Button(text="start", command=start_action, bg="white", highlightthickness=0)
start_bt.grid(column=1, row=3)

reset_bt = Button(text="reset", command=reset_action, bg="white", highlightthickness=0)
reset_bt.grid(column=3, row=3)


window.mainloop()
