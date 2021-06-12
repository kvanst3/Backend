from flask import Flask

app = Flask(__name__)


def bold_decorator(func):
    def wrapper_function():
        return f"<b>{func()}</b>"
    return wrapper_function


def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/1")
def details():
    return "<h1>YESSEREE!!</h1>"

@app.route("/<name>")
def greet(name):
    return f"Hello {name}"

@app.route("/bye")
@bold_decorator
@make_emphasis
def bye():
    return "Bye"

# if __name__ == "__main__":
#     app.run()

# to activate auto reload
if __name__ == "__main__":
    app.run(debug=True)