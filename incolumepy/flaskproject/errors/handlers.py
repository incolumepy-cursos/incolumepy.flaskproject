#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '@britodfbr'
from flask import Blueprint, render_template
errors = Blueprint('errors', __name__)


@errors.errorhandler(401)
@errors.errorhandler(403)
@errors.errorhandler(404)
@errors.errorhandler(405)
def internal_server_error(e):
    # note that we set the HTTP status code explicitly
    return render_template('error.html', error=e, title=e.name)
