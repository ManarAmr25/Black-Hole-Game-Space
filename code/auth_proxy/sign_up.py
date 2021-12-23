import abc
from models.player import Player
from database.db_manager import DBManager
from models.player_factory import PlayerFactory


# formal interface


class SignUpInterface(abc.ABC):
    def sign_up(self, name, password, gender):
        pass


# class implements the interface
class SignUp(SignUpInterface):

    def __init__(self):
        self.db = DBManager()
        if not self.db.connect():
            print("Database isn't connected.")

    def sign_up(self, name, password, gender):
        if not self.validate_password(password):
            return False, "Invalid password!"
        elif self.db.check_name(name):
            return False, "Name already exists!"
        else:
            # TODO : create and get player
            return True, player

    # check password
    @staticmethod
    def __validate_password(password):
        return len(password) >= 8
