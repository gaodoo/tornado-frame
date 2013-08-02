#!/usr/bin/env python
# encoding: utf-8

from .database import session
from ..models import User
# TODO:
# import md5lib as md5

def user_login(email, password):
    """
    check if the email and md5(password) exitsts
    in the databases, return the User obejct
    else return None
    """
    user = session.query(User).filter(
        User.email=email,
        User.password=md5(password)
    ).first()

    return user
