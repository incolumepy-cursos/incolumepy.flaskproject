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


def create_app(config_class=Config, *args, **kwargs):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    bc.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from incolumepy.flaskproject.ext.main.routes import main
    from incolumepy.flaskproject.ext.users.routes import users
    from incolumepy.flaskproject.ext.posts.routes import posts
    from incolumepy.flaskproject.ext.errors.handlers import errors
    app.register_blueprint(main)
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(errors)

    return app
