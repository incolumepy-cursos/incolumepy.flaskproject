#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '@britodfbr'
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
app.config["SECRET_KEY"] = "FVrpmovvW7LblKlVFmfLIk4n8X7sjuUOdIwe97udBDwLrVQtWge1cpKTwm0u137JovWZKDtFQXvZtOfBE0dLAz8H7LV"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///flask_blog.db"

db = SQLAlchemy(app)
bc = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
app.config["MAIL_SERVER"] = "smtp.googlemail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = os.environ.get('EMAIL_USER')
app.config["MAIL_PASSWORD"] = os.environ.get('EMAIL_PW')
mail = Mail(app)

from incolumepy.flaskproject.main.routes import main
from incolumepy.flaskproject.users.routes import users
from incolumepy.flaskproject.posts.routes import posts

app.register_blueprint(main)
app.register_blueprint(users)
app.register_blueprint(posts)
