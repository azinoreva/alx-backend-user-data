#!/usr/bin/env python3
"""
Module for password encryption and validation.
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """ Generates a hashed password with a salt, returns it as a byte string. """
    encoded = password.encode()
    hashed = bcrypt.hashpw(encoded, bcrypt.gensalt())

    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ Checks if the given password matches the stored hashed password. """
    valid = False
    encoded = password.encode()
    if bcrypt.checkpw(encoded, hashed_password):
        valid = True
    return valid

