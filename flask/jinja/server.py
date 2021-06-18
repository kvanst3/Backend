from flask import Flask
from flask import render_template
from os import name

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", name=name)


if __name__ == "__main__":
    app.run(debug=True)
