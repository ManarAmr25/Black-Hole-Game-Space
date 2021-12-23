from aifc import Error
import mysql.connector
from models.player import Player
from models.player_factory import PlayerFactory


class DBManager:
    def __init__(self):
        self.__connection = None
        self.__cursor = None

    def connect(self):
        try:
            self.__connection = mysql.connector.connect(
                host="localhost",
                user="GameAd",
                passwd="password",
                database="BlackHole"
            )
            print("MySQL Database connection successful")
            self.__cursor = self.__connection.cursor()
            return True
        except Exception:
            print("Connection Failed.")
            return False

    def get_quote(self):
        def_q = "Welcome Alien"
        try:
            self.__cursor.execute("SELECT quote FROM quotes ORDER BY RAND() LIMIT 1")
            res = self.__cursor.fetchall()
            if len(res) == 0:
                return def_q
            # TODO test
            print(res[0])
            return res[0]
        except Exception:
            return def_q

    def add_quote(self, q):
        try:
            self.__cursor.execute(f"INSERT INTO quotes(quote) VALUES('{str(q)}')")
            self.__connection.commit()
            return True
        except Exception:
            return False

    #for sign up
    def check_name(self, user_name):
        try:
            self.__cursor.execute(f"SELECT name FROM user_info WHERE name = '{str(user_name)}'")
            res = self.__cursor.fetchall()
            if len(res) == 0:
                False
            # TODO test
            print(res[0])
            return True
        except Exception:
            return False

    # for sign in & profile > returns pair of empty strings if user_name isn't found
    def get_password(self, user_name):
        try:
            self.__cursor.execute(f"SELECT password, salt FROM user_info WHERE name = '{str(user_name)}'")
            res = self.__cursor.fetchall()
            if len(res) == 0:
                return "", ""
            # TODO test
            print(res[0])
            return res[0]
        except Exception:
            return "", ""

    # used after authentication
    def get_player(self, user_name):
        try:
            self.__cursor.execute(f"SELECT * FROM user_info WHERE name = '{str(user_name)}'")
            res = self.__cursor.fetchall()
            if len(res) == 0:
                return False
            # TODO create player
            player = PlayerFactory.get_player("reg")
            return True
        except Exception:
            return None

    # add new player in sign up
    def add_player(self, user_name, password, salt, gender=False):
        if gender:
            gender = 1
        else:
            gender = 0

        try:
            self.__cursor.execute(f"INSERT INTO user_info(name, password, salt, gender) VALUES('{str(user_name)}', '{str(password)}','{str(salt)}', {gender})")
            self.__connection.commit()
            return True
        except Exception:
            return False

    # update progress, not name and password
    def update_player(self, player):
        if player.get_gender():
            gender = 1
        else:
            gender = 0
        try:
            self.__cursor.execute(f"UPDATE user_info SET name = '{player.get_name()}', gender = {gender}, avatar = '{player.get_avatar()}', level = {player.get_level()}, xp = {player.get_xp()}, weekly_xp = {player.get_weekly_xp()}, wins = {player.get_wins()}, games = {player.get_games()}, daily_ch = {player.get_daily_ch()}")
            self.__connection.commit()
            return True
        except Exception:
            return False

    def update_name(self, old_name, new_name):
        try:
            self.__cursor.execute(f"UPDATE user_info SET name = '{str(new_name)}' WHERE name = '{str(old_name)}'")
            return True
        except Exception:
            return False

    def update_password(self, name, old_password, new_password):
        try:
            self.__cursor.execute(
                f"UPDATE user_info SET password = '{str(new_password)}' WHERE name = '{str(name)}' AND password = '{str(old_password)}'")
            return True
        except Exception:
            return False
