#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '@britodfbr'

from flask import Blueprint, request, render_template, abort
from incolumepy.flaskproject.ext.dbase.models import Post
from markdown import markdown
from pathlib import Path
bp = Blueprint('main', __name__)


@bp.route("/")
@bp.route("/home")
def home():
    title = "Home Page"
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.id.desc()).paginate(page=page, per_page=3)
    return render_template("home.html", title=title, posts=posts)


@bp.route("/about")
def about():
    f = Path(__file__[:__file__.index('incolumepy')]).joinpath('README.md')
    content = f.read_text()
    html = markdown(content)
    return render_template("generic_page.html", content=html, title='About')


@bp.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"


@bp.route('/401')
def error401():
    abort(401)


@bp.route('/403')
def error403():
    abort(403)


@bp.route('/404')
def error404():
    abort(404)


@bp.route('/405')
def error405():
    abort(405)


@bp.route('/500')
def error500():
    abort(500, "Ops.. Erro interno")
