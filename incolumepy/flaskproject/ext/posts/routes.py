#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '@britodfbr'
from flask import Blueprint, render_template, redirect, url_for, flash, abort, request
from flask_login import login_required, current_user
from incolumepy.flaskproject.ext.dbase.models import Post, db
from incolumepy.flaskproject.ext.posts.forms import PostForm


bp = Blueprint('posts', __name__)


@bp.route("/post/new", methods=["GET", "POST"])
@login_required
def post_create():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash("Post criado com sucesso", "success")
        return redirect(url_for("main.home"))
    return render_template('post_create.html', title='New Post', form=form, legend="New Post")


@bp.route("/post/<int:post_id>")
def post_read(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)


@bp.route("/post/<int:post_id>/update", methods=["GET", "POST"])
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
        return redirect(url_for('bp.post_read', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('post_create.html', title='Update Post', form=form, legend="Update Post")


@bp.route("/post/<int:post_id>/delete", methods=["POST"])
@login_required
def post_delete(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Post deleted', 'success')
    return redirect(url_for('main.home'))

