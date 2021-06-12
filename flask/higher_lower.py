from flask import Flask
from random import randint

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Guess a number between 0 and 9 </h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"

number_to_guess = randint(0, 9)



if __name__ == "__main__":
    app.run(debug=True)