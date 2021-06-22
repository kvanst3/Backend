from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
import os

# Create the database file in /database/new-books-collection.db
FILE_URI = 'sqlite:///new-books-collection.db'

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = FILE_URI # load the configuration
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Significant overhead if True. Future default: False
db = SQLAlchemy(app)  # create the SQLAlchemy object by passing it the application


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return '<Book %r>' % self.title


# Create the database file and tables
if not os.path.isfile(FILE_URI):
    db.create_all()


@app.route('/')
def home():
    # all_books = db.session.query(Book).all()  #Alternative to below
    return render_template('index.html', books=Book.query.all())


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        try:
            # Create a book and store it in the database file
            book = Book(
                title=request.form['title'],
                author=request.form['author'],
                rating=request.form['rating']
                )

            db.session.add(book)
            db.session.commit()
        except Exception as e:
            print(e)
        return redirect(url_for('home'))
    return render_template('add.html')

@app.route("/edit/<int:book_id>", methods=["GET", "POST"])
def edit(book_id):
    if request.method == "POST":
        book_to_update = Book.query.filter_by(id=book_id).first()
        book_to_update.title = request.form['title']
        book_to_update.author = request.form['author']
        book_to_update.rating = request.form['rating']
        db.session.commit()
        return redirect(url_for('home'))
    book_to_update = Book.query.filter_by(id=book_id).first()
    return render_template("edit.html", book=book_to_update)

@app.route("/delete")
def delete():
    book_id = request.args.get('id')
    book_to_delete = Book.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
