#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '@britodfbr'
from flask import Blueprint, request, render_template
from incolumepy.flaskproject.models import Post


main = Blueprint('main', __name__)


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
