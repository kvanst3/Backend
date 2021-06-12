from flask import Flask
from random import randint

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Guess a number between 0 and 9 </h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"

number_to_guess = randint(0, 9)

@app.route("/<int:user_guess>")
def check_guess(user_guess):
    if user_guess > number_to_guess:
        return "<h1 style='text-align: center; color: red'> Too high </h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    elif user_guess < number_to_guess:
        return "<h1 style='text-align: center; color: blue'> Too low</h1>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    else:
        return "<h1 style='text-align: center; color: purple'> You got it!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"

if __name__ == "__main__":
    app.run(debug=True)