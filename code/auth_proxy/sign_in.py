import abc
from models.player import Player


class SignInInterface(abc.ABC):
    def sign_in(self, username, password):
        pass


class SignInClass(SignInInterface):
    def sign_in(self, username, password):
        if self.checkName(username)[0]:
            # if password = resPas -> true
            res_pas = self.checkName(username)[1]
            if password == res_pas:
                player = ""  # get player
                return True, player  # instance of player
            else:
                return False, "Wrong password"
        else:
            return False, "player doesn't exist"

    def __check_name(self, username):
        # password or false
        # dataBaseclass.methodName(username)
        # check database if name exists bring password if not return empty string
        res = "foo"  # password brought from database
        if res != "":
            return True, res
        else:
            return False, ""
