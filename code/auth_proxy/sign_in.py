import abc
from database.db_manager import DBManager
from hashing import *


class SignInInterface(abc.ABC):
    def sign_in(self, username, password):
        pass


class SignIn(SignInInterface):
    __secret_token = "6390ed339b8270b"

    def __init__(self):
        try:
            self.db = DBManager.get_instance(SignIn.__secret_token)
        except Exception as e:
            print(e)

    def sign_in(self, user_name, password):
        """
        Authenticate users
        :param user_name
        :param password
        :return: true and player if player has logged in successfully or false and message error otherwise
        """
        original_pw, salt = self.db.get_password()
        if len(salt) < 64:
            return False, "Player doesn't exist!"
        else:
            hashed_password = hash_password(salt, password)
            if hashed_password != original_pw:
                return False, "Wrong password!"
            else:
                return self.db.get_player(user_name)  # may return null
