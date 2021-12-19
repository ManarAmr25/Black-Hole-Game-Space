import abc
from models.player import Player

# formal interface


class SignUpInterface(abc.ABC):
    def sign_up(self,name, password, gender):
        pass


# class implements the interface
class SignUp(SignUpInterface):

    def sign_up(self,name, password, gender):
        if not self.validate_password(password) :
            return False, "Invalid password"
        elif not self.validate_name(name):
            return False, "Name already exists !"
        else:
            player = Player(name)  # create player
            return (True, player)

    # check password
    def __validate_password(password):
        if password < 8 :
            return False

    # check name
    def __validate_name(name):
        in_database = True  # search in DataBase
        if in_database:
            return False
        else:
            # insert in data base
            return True