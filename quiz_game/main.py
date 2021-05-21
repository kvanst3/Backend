from question_model import Question
import requests
from ui import QuizInterface


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


quiz_ui = QuizInterface(question_bank)
