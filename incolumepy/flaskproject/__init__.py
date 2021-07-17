#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '@britodfbr'
from flask import Flask
from incolumepy.flaskproject import configure
from incolumepy.flaskproject.ext import (
    main,
    auth,
    cli,
    dbase,
    errors,
    posts,
    users,
    mail,
)
#
#
#
#
# def create_app(config_class=Config, *args, **kwargs):
#     app = Flask(__name__)
#     app.config.from_object(config_class)
#     db.init_app(app)
#     bc.init_app(app)
#     mail.init_app(app)
#
#     from incolumepy.flaskproject.ext.main.routes import main
#     from incolumepy.flaskproject.ext.users.routes import users
#     from incolumepy.flaskproject.ext.bp.routes import bp
#     from incolumepy.flaskproject.ext.bp.handlers import bp
#     app.register_blueprint(main)
#     app.register_blueprint(users)
#     app.register_blueprint(bp)
#     app.register_blueprint(bp)
#
#     return app


def create_app(*args, **kwargs):
    app = Flask(__name__)
    configure.init_app(app)
    errors.init_app(app)
    cli.init_app(app)
    dbase.init_app(app)
    mail.init_app(app)
    auth.init_app(app)
    main.init_app(app)
    users.init_app(app)
    posts.init_app(app)
    return app
