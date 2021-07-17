#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '@britodfbr'
from .handlers import bp


def init_app(app):
    app.register_blueprint(bp)
