#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '@britodfbr'
from flask import Blueprint, request, render_template
from incolumepy.flaskproject.models import Post


main = Blueprint('main', __name__)


@main.errorhandler(401)
@main.errorhandler(403)
@main.errorhandler(404)
@main.errorhandler(405)
def internal_server_error(e):
    # note that we set the HTTP status code explicitly
    return render_template('error.html', error=e, title=e.name)


@main.route("/")
@main.route("/home")
def home():
    title = "Home Page"
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.id.desc()).paginate(page=page, per_page=3)
    return render_template("home.html", title=title, posts=posts)


@main.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"
