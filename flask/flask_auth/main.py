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
    return User.query.get(int(user_id))


##Routes

@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form['email']
        if not User.query.filter_by(email=email).first():
            name = request.form['name']
            password = generate_password_hash(request.form['password'], method='pbkdf2:sha256', salt_length=8)
            new_user = User(email=email, name=name, password=password)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect(url_for("secrets"))
        else:
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for('login'))
    return render_template("register.html", logged_in=current_user.is_authenticated)


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == "POST":
        login = request.form['email']
        password = request.form['password']
        user = db.session.query(User).filter_by(email=login).first()

        if not user:
            flash('Incorrect email, please try again.')
        elif check_password_hash(user.password, password):
            login_user(user)
            flash('Logged in successfully.')
            return redirect(url_for('secrets'))
        else:
            flash('Password incorrect, please try again.')
            return redirect(url_for('login'))

    return render_template("login.html", logged_in=current_user.is_authenticated)


@app.route('/secrets')
@login_required
def secrets():
    print(current_user.name)
    return render_template("secrets.html", current_user=current_user, logged_in=current_user.is_authenticated)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    return send_from_directory('static', "files/cheat_sheet.pdf", as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
