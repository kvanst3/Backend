from flask import Flask, render_template
from os import name
from random import randint
from datetime import datetime as dt
import requests
import json

app = Flask(__name__)


@app.route("/")
def home():
    random_num = randint(1,10)
    current_year = dt.now().year
    return render_template("index.html", name=name, num=random_num, current_year=current_year)

@app.route("/guess/<fname>")
def guess(fname):
    response = requests.get(f"https://api.genderize.io?name={fname}")
    result = response.json()
    gender = result["gender"]
    response = requests.get(f"https://api.agify.io?name={fname}")
    result = response.json()
    age = result["age"]
    return render_template("guess.html", gender=gender, fname=fname, age=age)


if __name__ == "__main__":
    app.run(debug=True)
