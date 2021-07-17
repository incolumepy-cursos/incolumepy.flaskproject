#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '@britodfbr'
from .models import db


def create_db():
    """Creates database"""
    db.create_all()


def drop_db():
    """Cleans database"""
    db.drop_all()

