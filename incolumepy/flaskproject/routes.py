#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '@britodfbr'

from flask import render_template, flash, url_for, redirect
from . import app
from .forms import RegistrationForm, LoginForm
from .models import posts


@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"


@app.errorhandler(404)
def internal_server_error(e):
    # note that we set the 500 status explicitly
    return render_template('error.html', error=e)


@app.route("/")
def home():
    title = "Home Page"
    return render_template("home.html", title=title, posts=posts)


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Conta "{form.email.data}" criada com sucesso!', "success")
        return redirect(url_for("home"))
    return render_template("register.html", form=form, title="Register")


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'user@incolume.com.br' and form.password.data == '123':
            flash("Login with success", 'success')
            return redirect(url_for('home'))
        else:
            flash('Please check your user or password', 'danger')
    return render_template("login.html", form=form, title="Login")
