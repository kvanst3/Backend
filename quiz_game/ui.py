from tkinter import *
import html


THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        self.quiz = quiz
        
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question = self.canvas.create_text(150, 125, width=250, text=f"{html.unescape(self.quiz.current_question.text)}", font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50, padx=0)

        green_img = PhotoImage(file="quiz_game/images/true.png")
        self.green_button = Button(image=green_img, highlightthickness=0, command=self.is_true)
        self.green_button.grid(row=2, column=0)

        red_img = PhotoImage(file="quiz_game/images/false.png")
        self.red_button = Button(image=red_img, highlightthickness=0, command=self.is_false)
        self.red_button.grid(row=2, column=1)

        self.score_label = Label(text=f"Score: {self.quiz.right_answers}", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.window.mainloop()

    def is_true(self):
        self.quiz.check_answer("True")
        self.update_ui()
    
    def is_false(self):
        self.quiz.check_answer("False")
        self.update_ui()

    def update_ui(self):
        self.canvas.itemconfigure(self.question, text=f"{html.unescape(self.quiz.current_question.text)}")
        self.score_label.config(text=f"Score: {self.quiz.right_answers}")