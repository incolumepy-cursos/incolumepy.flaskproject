#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '@britodfbr'
import datetime as dt
from . import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='user_color.svg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    posted = db.Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.posted}')"


posts = [
    {
        "id": 5,
        "author": "Ada Catarina Santos Brito",
        "title": "post 5",
        "content": "content post 5",
        "posted": "09-07-2021 15:58",
    },
    {
        "id": 4,
        "author": "Ana Gabriela Santos Brito",
        "title": "post 4",
        "content": "content post 4",
        "posted": "09-07-2021 15:58",
    },
    {
        "id": 3,
        "author": "Eliana Ferreira dos Santos Brito",
        "title": "post 3",
        "content": "content post 3",
        "posted": "09-07-2021 15:53",
    },
    {
        "id": 2,
        "author": "Ricardo Brito do Nascimento",
        "title": "post 2",
        "content": "content post 2",
        "posted": "09-07-2021 15:03",
    },
    {
        "id": 1,
        "author": "Ricardo Brito do Nascimento",
        "title": "post 1",
        "content": "content post 1",
        "posted": "09-07-2021 15:00",
    },
]
