#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '@britodfbr'
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from incolumepy.flaskproject.configure import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
bc = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

mail = Mail(app)

from incolumepy.flaskproject.main.routes import main
from incolumepy.flaskproject.users.routes import users
from incolumepy.flaskproject.posts.routes import posts

app.register_blueprint(main)
app.register_blueprint(users)
app.register_blueprint(posts)
