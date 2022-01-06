import os
import shutil

from auth_proxy.sign_up import SignUp
from auth_proxy.sign_in import SignIn
from backend_layer.getter import Getter
from models.player import Player
from backend_layer.updater import Updater


class Facade:
    __instance = None

    def __init__(self):
        if Facade.__instance is not None:
            raise Exception("Can't create another instance of Facade")
        else:
            self.player = None
            self.s1 = SignUp()
            self.s2 = SignIn()
            self.u = Updater.get_instance()
            self.g = Getter.get_instance()
            Facade.__instance = self

    @staticmethod
    def get_instance():
        if Facade.__instance is not None:
            return Facade.__instance
        else:
            Facade.__instance = Facade()
            return Facade.__instance

    @staticmethod
    def reset_instance():
        Facade.__instance = None

    def signup_request(self, name, password, gender):
        check, player = self.s1.sign_up(name, password, gender)
        print("sign up : " , check, player, name, password, gender)
        if check:
            self.player = player
        return check, player

    def signin_request(self, name, password):
        check, player = self.s2.sign_in(name, password)
        if check:
            self.player = player
        return check, player

    def save_player(self):
        check = self.u.save_player(self.player)
        if check:
            self.player = None
        return check

    def save_name(self, new_name):
        return self.u.save_name(self.player, new_name)

    def save_password(self, old_password, new_password):
        return self.u.save_password(self.player, old_password, new_password)

    def change_profile_pic(self, path):
        # path validation
        if not os.path.isfile(path) or not (os.path.splitext(path)[-1] == '.png' or os.path.splitext(path)[-1] == '.jpg' or os.path.splitext(path)[-1] == '.jpeg'):
            return False, None

        try:
            new_path = "..\\storage\\Avatars\\" + self.player.get_name() + os.path.splitext(path)[-1]
            shutil.copyfile(path, new_path)
            self.player.set_avatar(new_path)
            return True, new_path
        except Exception as e:
            print(e)
            return False, None

    def notify_achievements(self, player, achievement_type):
        return self.player.update_achievements(achievement_type)

    def get_achievements(self):
        ach_list = self.player.get_achievements()
        res = []
        for ach in ach_list:
            t = ach.get_description(), ach.get_reward(), ach.get_checked()
            res.append(t)
        return res

    def get_quote(self):
        return self.g.get_quote()

    def get_leaderboard(self):
        return self.g.get_leaderboard()

    def reset_player(self):
        self.player = None
