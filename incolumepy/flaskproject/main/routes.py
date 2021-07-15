#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '@britodfbr'
from flask import Blueprint, request, render_template, abort
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


@main.route('/401')
def error401():
    abort(401)


@main.route('/403')
def error403():
    abort(403)


@main.route('/404')
def error404():
    abort(404)


@main.route('/405')
def error405():
    abort(405)


@main.route('/500')
def error500():
    abort(500, "Ops.. Erro interno")
