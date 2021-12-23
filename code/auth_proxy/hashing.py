import hashlib
import os


def hash_password(salt, password):
    return hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)


def generate_salt():
    return os.urandom(32)
