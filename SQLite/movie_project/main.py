from operator import index
from flask import Flask, render_template, redirect, url_for, request
from flask.templating import render_template_string
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
import os

DB_URI = 'sqlite:///movies.db'
ENDPOINT = 'https://api.themoviedb.org/3/search/movie'
API_KEY = os.environ.get('DB_MOVIE_KEY')

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=True)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)


if not os.path.isfile(DB_URI):
    db.create_all()


class RateMovieForm(FlaskForm):
    rating = StringField("Your Rating Out of 10 e.g. 7.5")
    review = StringField("Your Review")
    submit = SubmitField("Done")

class AddMovieForm(FlaskForm):
    title = StringField('Title of the movie you are looking for')
    submit = SubmitField("Add Movie")

@app.route("/")
def home():
    all_movies=Movie.query.all()
    return render_template("index.html", movies=all_movies)

@app.route('/add', methods=["GET", "POST"])
def add():
    form = AddMovieForm()
    if form.validate_on_submit():
        params = {
            'api_key': API_KEY,
            'query': form.title.data,
            'language': 'en-US',
            'page': 1,
            'include_adult': "false",
        }
        response = requests.get(ENDPOINT, params=params)
        response.raise_for_status

        data = response.json()
        results = data['results']
        return render_template('select.html', movies=results)
        
    return render_template('add.html', form=form)
    

@app.route("/select/<int:id>", methods=["GET", "POST"])
def select(id):
    params = {
        'api_key': API_KEY,
        'language': 'en-US',
    }
    response = requests.get(f'https://api.themoviedb.org/3/movie/{id}', params=params)
    response.raise_for_status
    data = response.json()

    title = data['title']
    year = data['release_date'].split('-')[0]
    description = data['overview']
    img_url = 'http://image.tmdb.org/t/p/w300' + data['poster_path']
    movie = Movie(title=title, year=year, description=description, img_url=img_url)
    db.session.add(movie)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/edit', methods=["GET", "POST"])
def edit():
    form = RateMovieForm()
    movie_id = request.args.get('id')
    movie = Movie.query.get(movie_id)
    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', movie=movie, form=form)


@app.route('/delete')
def delete():
    movie_id = request.args.get('id')
    movie_to_delete = Movie.query.get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))
    

if __name__ == '__main__':
    app.run(debug=True)
