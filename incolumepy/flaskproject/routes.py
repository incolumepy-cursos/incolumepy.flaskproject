#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '@britodfbr'

from flask import render_template, flash, url_for, redirect
from . import app, db, bc
from .forms import RegistrationForm, LoginForm
from .models import posts, User
from flask_login import login_user, current_user, logout_user, login_required


@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"


@app.errorhandler(401)
@app.errorhandler(403)
@app.errorhandler(404)
def internal_server_error(e):
    # note that we set the 500 status explicitly
    return render_template('error.html', error=e, title=e.name)


@app.route("/")
def home():
    title = "Home Page"
    return render_template("home.html", title=title, posts=posts)


@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pw = bc.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        flash(f'Conta "{form.email.data}" criada com sucesso!', "success")
        return redirect(url_for("login"))
    return render_template("register.html", form=form, title="Register")


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bc.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            flash("Login with success", 'success')
            return redirect(url_for('home'))
        else:
            flash('Please check your user or password', 'danger')
    return render_template("login.html", form=form, title="Login")


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')
