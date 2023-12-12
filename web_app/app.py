from flask import Flask, render_template, request, redirect, url_for, abort, make_response, session
from models import store
from models.user import User
from models.survey import Survey
from models.response import Response
from web_app.auth import Auth


auth = Auth()
app = Flask(__name__)


@app.route("/", methods=["GET"], strict_slashes=False)
def index():
    session_id = request.cookies.get('session_id')
    user = auth.get_user_from_session(session_id)
    if user:
        return "Hello World"
    else:
        return redirect(url_for("login"))


@app.route("/login", methods=["POST", "GET"], strict_slashes=False)
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        validate = auth.valid_login(email, password)
        # validate = False
        print('I am at post', email, password)
        if validate:
            print('I am at validate', email)
            session_id = auth.create_session(email)
            response = make_response(render_template("index.html"))
            response.set_cookie('session_id', session_id)
            # session['user'] = auth.get_user_from_session(session_id)
            return response
        print('I am at not at validate', email)
        return render_template("login.html")
    else:
        print('I am at get')
        session_id = request.cookies.get('session_id')
        user = auth.get_user_from_session(session_id)
        if user:
            return redirect(url_for('index'))
        else:
            return render_template('login.html')



if __name__ == '__main__':
    port = 5000
    host = '0.0.0.0'
    app.run(port=port, host=host, debug=True)

# from flask_wtf import FlaskForm
# from wtforms import StringField, PasswordField, SubmitField
# from wtforms.validators import DataRequired
# from flask import Flask, render_template, request, redirect, url_for, flash, abort
# from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import String
# from flask_migrate import Migrate
# from werkzeug.security import generate_password_hash, check_password_hash
# from config import Config
# from flask_bcrypt import Bcrypt

# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'MySecretKeys'  # Change this to a secure secret key
# app.config['SQLALCHEMY_DATABASE_URI'] = '#####'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# bcrypt = Bcrypt(app)
# app.config.from_object('config.Config')  

# db = SQLAlchemy(app)
# migrate = Migrate(app, db)
# login_manager = LoginManager(app)
# login_manager.login_view = 'login'


# @login_manager.user_loader
# def load_user(user_id):
#     for user in users:
#         if user.id == int(user_id):
#             return user
#     return None

# class LoginForm(FlaskForm):
#     username = StringField('Username', validators=[DataRequired()])
#     password = PasswordField('Password', validators=[DataRequired()])
#     submit = SubmitField('Log In')

# class RegistrationForm(FlaskForm):
#     username = StringField('Username', validators=[DataRequired()])
#     password = PasswordField('Password', validators=[DataRequired()])
#     submit = SubmitField('Register')

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         username = form.username.data
#         password = form.password.data

#         # Check if the user is registered (replace with database query)
#         user = next((u for u in users if u.username == username and u.password == password), None)

#         if user:
#             login_user(user)
#             flash('Logged in successfully!', 'success')
#             return redirect(url_for('survey'))

#         flash('Invalid username or password', 'error')

#     return render_template('login.html', form=form)


# @app.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     return redirect(url_for('index'))

# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         username = form.username.data
#         password = form.password.data

#         # Check if the username is already taken (replace with database query)
#         if any(u.username == username for u in users):
#             flash('Username already taken. Please choose another.', 'error')
#         else:
#             # Create a new user (replace with database insert)
#             user = User(len(users) + 1, username, password)
#             users.append(user)
#             flash('Registration successful! Please log in.', 'success')
#             return redirect(url_for('login'))

#     return render_template('register.html', form=form)


# @app.route('/thank_you')
# def thank_you():
#     return render_template('thank_you.html')

# @app.route('/survey', methods=['GET', 'POST'])
# @login_required
# def survey():
#     if request.method == 'POST':
#         # Process and store survey responses
#         survey_data = request.form.to_dict()
#         # You can save the survey_data to a database or a file
#         return redirect(url_for('thank_you'))

#     # Your existing logic to fetch surveys from the database
#     surveys = Survey.query.all()

#     # Your survey or quiz questions and answers
#     questions = [
#         {"question": "What is the capital of France?", "choices": ["Paris", "Berlin", "Madrid", "Rome"], "correct": "Paris"},
#         {"question": "Which programming language is this app built with?", "choices": ["Python", "JavaScript", "Java", "C++"], "correct": "Python"},
#     ]

#     return render_template('survey.html', surveys=surveys, questions=questions)


# if __name__ == '__main__':
#     app.run(debug=True)
