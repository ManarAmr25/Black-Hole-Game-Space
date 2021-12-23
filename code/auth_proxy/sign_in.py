import abc
from database.db_manager import DBManager
from hashing import *


class SignInInterface(abc.ABC):
    def sign_in(self, username, password):
        pass


class SignInClass(SignInInterface):

    def __init__(self):
        self.db = DBManager()
        if not self.db.connect():
            print("Database isn't connected.")

    def sign_in(self, username, password):
        original_pw, salt = self.db.get_password()
        if len(salt) < 64:
            return False, "Player doesn't exist!"
        else:
            hashed_password = hash_password(salt, password)
            if hashed_password != original_pw:
                return False, "Wrong password!"
            else:
                return True # TODO : player
