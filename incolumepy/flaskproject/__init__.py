#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '@britodfbr'
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from incolumepy.flaskproject.configure import Config


db = SQLAlchemy()
bc = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    bc.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from incolumepy.flaskproject.main.routes import main
    from incolumepy.flaskproject.users.routes import users
    from incolumepy.flaskproject.posts.routes import posts

    app.register_blueprint(main)
    app.register_blueprint(users)
    app.register_blueprint(posts)
