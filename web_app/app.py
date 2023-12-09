
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from flask import Flask, render_template, request, redirect, url_for, flash, abort
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash
from config import Config
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'MySecretKeys'  # Change this to a secure secret key
app.config['SQLALCHEMY_DATABASE_URI'] = '#####'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
bcrypt = Bcrypt(app)
app.config.from_object('config.Config')  

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view = 'login'



# Example User Model (replace with your own database model)
class User(UserMixin):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

class Survey(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    survey_name = db.Column(db.String(255), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    created_at = db.Column(db.TIMESTAMP, default=db.func.current_timestamp())

users = []  # In-memory user storage (replace with a database)

@login_manager.user_loader
def load_user(user_id):
    for user in users:
        if user.id == int(user_id):
            return user
    return None

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        # Check if the user is registered (replace with database query)
        user = next((u for u in users if u.username == username and u.password == password), None)

        if user:
            login_user(user)
            flash('Logged in successfully!', 'success')
            return redirect(url_for('survey'))

        flash('Invalid username or password', 'error')

    return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        # Check if the username is already taken (replace with database query)
        if any(u.username == username for u in users):
            flash('Username already taken. Please choose another.', 'error')
        else:
            # Create a new user (replace with database insert)
            user = User(len(users) + 1, username, password)
            users.append(user)
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('login'))

    return render_template('register.html', form=form)


@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')

@app.route('/survey', methods=['GET', 'POST'])
@login_required
def survey():
    if request.method == 'POST':
        # Process and store survey responses
        survey_data = request.form.to_dict()
        # You can save the survey_data to a database or a file
        return redirect(url_for('thank_you'))

    # Your existing logic to fetch surveys from the database
    surveys = Survey.query.all()

    # Your survey or quiz questions and answers
    questions = [
        {"question": "What is the capital of France?", "choices": ["Paris", "Berlin", "Madrid", "Rome"], "correct": "Paris"},
        {"question": "Which programming language is this app built with?", "choices": ["Python", "JavaScript", "Java", "C++"], "correct": "Python"},
    ]

    return render_template('survey.html', surveys=surveys, questions=questions)


if __name__ == '__main__':
    app.config.from_object(Config)
    app.run(debug=True)
    app.config.from_object(Config)
    with app.app_context():
        db.create_all()  # Create database tables


