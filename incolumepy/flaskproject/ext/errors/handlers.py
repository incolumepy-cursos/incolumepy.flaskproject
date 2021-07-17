#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '@britodfbr'
from flask import Blueprint, render_template
errors = Blueprint('errors', __name__)


@errors.app_errorhandler(401)
@errors.app_errorhandler(403)
@errors.app_errorhandler(404)
@errors.app_errorhandler(405)
@errors.app_errorhandler(500)
def error_page(e):
    # note that we set the HTTP status code explicitly
    return render_template('error.html', error=e, title=e.name), e.code
