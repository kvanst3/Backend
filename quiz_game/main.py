from question_model import Question
from data import question_data
from quiz_brain import Quiz
import requests


params = {
    "amount": 10,
    "type": "boolean",
}
response = requests.get("https://opentdb.com/api.php", params=params)
response.raise_for_status()
data = response.json()['results']

question_bank = []
for i in data:
    new_question = Question(i['question'], i['correct_answer'])
    question_bank.append(new_question)


quiz = Quiz(question_bank)

quiz.ask_question()

print(f"Your Final Score is: {quiz.right_answers}/12")