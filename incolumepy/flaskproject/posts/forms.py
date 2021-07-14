#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '@britodfbr'


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')
