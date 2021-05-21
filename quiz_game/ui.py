from tkinter import *


THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self):
        self.score = 0

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question = self.canvas.create_text(150, 125, text= "My question here", font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50, padx=0)

        green_img = PhotoImage(file="quiz_game/images/true.png")
        self.green_button = Button(image=green_img, highlightthickness=0, command=self.is_true)
        self.green_button.grid(row=2, column=0)

        red_img = PhotoImage(file="quiz_game/images/false.png")
        self.red_button = Button(image=red_img, highlightthickness=0, command=self.is_false)
        self.red_button.grid(row=2, column=1)

        self.score_label = Label(text=f"Score: {self.score}", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        self.window.mainloop()

    def is_true(self):
        print("true?")
    
    def is_false(self):
        print("false?")

    def increase_score(self):
        self.score += 1