#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '@britodfbr'
from pathlib import Path
from PIL import Image
from random import choices
from string import hexdigits
from flask import render_template, flash, url_for, redirect, request, abort
from . import app, db, bc, mail
from .forms import RegistrationForm, LoginForm, UpdateAccountForm, PostForm, RequestResetForm, ResetPasswordForm
from .models import posts, User, Post
from flask_login import login_user, current_user, logout_user, login_required
from flask_mail import Message


@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"


@app.errorhandler(401)
@app.errorhandler(403)
@app.errorhandler(404)
@app.errorhandler(405)
def internal_server_error(e):
    # note that we set the HTTP status code explicitly
    return render_template('error.html', error=e, title=e.name)


@app.route("/")
def home():
    title = "Home Page"
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.id.desc()).paginate(page=page, per_page=3)
    return render_template("home.html", title=title, posts=posts)


def save_picture(form_pic, size: tuple = (125, 125)):
    randon_hex = ''.join(choices(hexdigits, k=8))
    f = Path(form_pic.filename)
    fn = Path(app.root_path)/'static/profile_pics'/f"avatar_{randon_hex}{f.suffix}"
    i = Image.open(form_pic)
    i.thumbnail(size)
    i.save(fn)
    # print(fn)
    return fn.name


@app.route("/post/new", methods=["GET", "POST"])
@login_required
def post_create():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash("Post criado com sucesso", "success")
        return redirect(url_for("home"))
    return render_template('post_create.html', title='New Post', form=form, legend="New Post")


@app.route("/post/<int:post_id>")
def post_read(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)


@app.route("/post/<int:post_id>/update", methods=["GET", "POST"])
@login_required
def post_update(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Post updated', 'success')
        return redirect(url_for('post_read', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('post_create.html', title='Update Post', form=form, legend="Update Post")


@app.route("/post/<int:post_id>/delete", methods=["POST"])
@login_required
def post_delete(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Post deleted', 'success')
    return redirect(url_for('home'))


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message(
        'Password Reset Request',
        sender='noreply@incolume.com.br',
        recipients=[user.email]
    )
    msg.body = f""" Para prosseguir com a requisição de alteração de senha, visite o link abaixo:
{url_for('reset_token', token=token, _external=True)}

Se Você não solicitou esta mudança, simplesmente ignore esta mensagem.
"""
    mail.send(msg)
