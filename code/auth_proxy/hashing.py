import hashlib
import os


def hash_password(salt, password):
    print("inside hash_password", salt, password)
    """Apply salted hashing"""
    print("in hash >> ", hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000))
    return hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)


def generate_salt():
    """Generate random salt of length 32 bytes"""
    return os.urandom(32)
