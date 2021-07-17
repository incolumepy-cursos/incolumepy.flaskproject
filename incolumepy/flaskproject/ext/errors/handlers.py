#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '@britodfbr'
from flask import Blueprint, render_template
bp = Blueprint('error', __name__)


@bp.app_errorhandler(401)
@bp.app_errorhandler(403)
@bp.app_errorhandler(404)
@bp.app_errorhandler(405)
@bp.app_errorhandler(500)
def error_page(e):
    # note that we set the HTTP status code explicitly
    return render_template('error.html', error=e, title=e.name), e.code
