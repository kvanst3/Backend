from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
#Line below only required once, when creating DB. 
# db.create_all()

##AUTH
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


##Routes

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form['email']
        name = request.form['name']
        password = generate_password_hash(request.form['password'], method='pbkdf2:sha256', salt_length=8)
        new_user = User(email=email, name=name, password=password)
        db.session.add(new_user)
        db.session.commit()
        return render_template('secrets.html', user=new_user)
    return render_template("register.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if reques.method == "POST":
        login = request.form['email']
        password = request.form['password']
        user = db.session.query(User).filter_by(email=login).first()
        pwhash = user.password
        if werkzeug.security.check_password_hash(pwhash, password):
            print("Authenticated")
            return render_template('secrets.html', user=user)
    return render_template("login.html")


@app.route('/secrets')
def secrets():
    return render_template("secrets.html")


@app.route('/logout')
def logout():
    pass


@app.route('/download')
def download():
    return send_from_directory('static', "files/cheat_sheet.pdf", as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
