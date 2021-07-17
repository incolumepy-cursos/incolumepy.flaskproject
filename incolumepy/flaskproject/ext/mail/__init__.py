#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '@britodfbr'
from flask_mail import Mail

mail = Mail()


def init_app(app):
    mail.init_app(app)
