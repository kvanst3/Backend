import html
from question_model import Question


class Quiz():

    def __init__(self, q_bank):
        self.question_bank = q_bank
        self.question_number = 1
        self.right_answers = 0
        self.current_question = self.question_bank[self.question_number]

    def next_question(self):
        self.question_number += 1
        self.current_question = self.question_bank[self.question_number]

    def check_answer(self, usr_answer):
        if self.current_question.answer == usr_answer:
            self.right_answers += 1
            print("Seikou!\n")
            return True
        else:
            print("Batsu...\n")
            return False
        
    def still_has_questions(self):
        return self.question_number < len(self.question_bank)
