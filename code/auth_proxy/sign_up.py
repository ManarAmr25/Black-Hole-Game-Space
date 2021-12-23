import abc
from models.player import Player
from database.db_manager import DBManager
from hashing import *


# formal interface


class SignUpInterface(abc.ABC):
    def sign_up(self, name, password, gender):
        pass


# class implements the interface
class SignUp(SignUpInterface):

    __secret_token = "6390ed339b8270b"

    def __init__(self):
        try:
            self.db = DBManager.get_instance(SignUp.__secret_token)
        except Exception as e:
            print(e)

    def sign_up(self, name, password, gender):
        """
        Create new player
        :param name
        :param password
        :param gender
        :return: true and player object or false and an error message
        """
        if not self.validate_password(password):
            return False, "Invalid password!"
        elif self.db.check_name(name):
            return False, "Name already exists!"
        else:
            salt = generate_salt()
            password = hash_password(salt, password)
            return self.db.add_player(name, password, salt, gender)

    # check password
    @staticmethod
    def __validate_password(password):
        return len(password) >= 8
