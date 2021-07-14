#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '@britodfbr'
from pathlib import Path
from PIL import Image
from random import choices
from string import hexdigits
from flask import render_template, flash, url_for, redirect, request, abort
from . import app, db, bc, mail
from .forms import RegistrationForm, LoginForm, UpdateAccountForm, PostForm, RequestResetForm, ResetPasswordForm
from .models import posts, User, Post
from flask_login import login_user, current_user, logout_user, login_required
from flask_mail import Message






