#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '@britodfbr'
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .forms import RegistrationForm, LoginForm
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config["SECRET_KEY"] = "FVrpmovvW7LblKlVFmfLIk4n8X7sjuUOdIwe97udBDwLrVQtWge1cpKTwm0u137JovWZKDtFQXvZtOfBE0dLAz8H7LV"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///flask_blog.db"

db = SQLAlchemy(app)
bc = Bcrypt(app)

from . import routes
