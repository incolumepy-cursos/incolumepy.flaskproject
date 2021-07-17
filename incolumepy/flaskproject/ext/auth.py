#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '@britodfbr'
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from incolumepy.flaskproject.ext.dbase.models import db, User

bc = Bcrypt()
login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


def create_user(username, email, password, image_file):
    """Registra um novo usuario caso nao esteja cadastrado"""
    if User.query.filter_by(username=username).first():
        raise RuntimeError(f'{username} já esta cadastrado')
    user = User(username=username, email=email, password=bc.generate_password_hash(password), image_file=image_file)
    db.session.add(user)
    db.session.commit()
    return user


def init_app(app):
    login_manager.login_view = 'users.login'
    login_manager.login_message_category = 'info'
    login_manager.init_app(app)
