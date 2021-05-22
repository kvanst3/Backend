import html
from question_model import Question


class Quiz():

    def __init__(self, q_bank):
        self.question_bank = q_bank
        self.question_number = 0
        self.right_answers = 0
        self.current_question = self.question_bank[self.question_number]

    def next_question(self):
        self.question_number += 1
        if self.question_number < len(self.question_bank):
            self.current_question = self.question_bank[self.question_number]
        else:
            self.current_question = Question(f"You have reach the end of the quiz.\n\nFinal Score: {self.right_answers}", "None")

    def check_answer(self, usr_answer):
        if self.current_question.answer == usr_answer:
            self.right_answers += 1
            print("Seikou!\n")
        else:
            print("Batsu...\n")
        self.next_question()
