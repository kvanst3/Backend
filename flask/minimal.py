from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/1")
def details():
    return "<h1>YESSEREE!!</h1>"

if __name__ == "__main__":
    app.run()