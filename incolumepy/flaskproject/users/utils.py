#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '@britodfbr'
from random import choices
from pathlib import Path
from PIL import Image
from string import hexdigits
from flask import url_for
from flask_mail import Message
from incolumepy.flaskproject import app, mail


def save_picture(form_pic, size: tuple = (125, 125)):
    randon_hex = ''.join(choices(hexdigits, k=8))
    f = Path(form_pic.filename)
    fn = Path(app.root_path)/'static/profile_pics'/f"avatar_{randon_hex}{f.suffix}"
    i = Image.open(form_pic)
    i.thumbnail(size)
    i.save(fn)
    # print(fn)
    return fn.name


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message(
        'Password Reset Request',
        sender='noreply@incolume.com.br',
        recipients=[user.email]
    )
    msg.body = f""" Para prosseguir com a requisição de alteração de senha, visite o link abaixo:
{url_for('users.reset_token', token=token, _external=True)}

Se Você não solicitou esta mudança, simplesmente ignore esta mensagem.
"""
    mail.send(msg)
