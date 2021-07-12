#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import Length, DataRequired, Email, EqualTo, ValidationError
from .models import User
__author__ = "@britodfbr"


class RegistrationForm(FlaskForm):
    username = StringField(
        "Username", validators=[DataRequired(), Length(min=3, max=20)]
    )
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField(
        "Confirm Password", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField('Sign Up')

    def validate_username(self, field):
        user = User.query.filter_by(username=field.data).first()
        if user:
            raise ValidationError(f'alrady exist <<{field.data}>>, choice another')

    def validate_email(self, field):
        user = User.query.filter_by(email=field.data).first()
        if user:
            raise ValidationError(f'alrady exist <<{field.data}>>, choice another')


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    username = StringField(
        "Username", validators=[DataRequired(), Length(min=3, max=20)]
    )
    email = StringField("Email", validators=[DataRequired(), Email()])
    picture = FileField("Update profile picture", validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Uptate')

    def validate_username(self, field):
        if self.username.data != current_user.username:
            user = User.query.filter_by(username=field.data).first()
            if user:
                raise ValidationError(f'alrady exist <<{field.data}>>, choice another')

    def validate_email(self, field):
        if self.email.data != current_user.email:
            user = User.query.filter_by(email=field.data).first()
            if user:
                raise ValidationError(f'alrady exist <<{field.data}>>, choice another')
