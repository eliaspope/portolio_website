from datetime import date
from flask_bootstrap import Bootstrap5
from flask import Flask, abort, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_gravatar import Gravatar
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
import os

app = Flask(__name__)
app_key = os.environ.get('flask_key')
print(app_key)
app.config['SECRET_KEY'] = os.environ.get('flask_key')
Bootstrap5(app)


# home route that returns below text when root url is accessed
@app.route("/")
def home():
    return render_template('carousel.html')

@app.route("/about")
def about():
    return render_template('index.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/art")
def art():
    return render_template('art.html')



if __name__ == '__main__':
    app.run(debug=True)
