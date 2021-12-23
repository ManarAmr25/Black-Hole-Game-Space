import mysql.connector
from models.player import Player


class DBManager:
    """
    A singleton class responsible for managing queries to BlackHole database.
    ...

    Methods
    -------
    get_instance(token):
        :returns the singleton instance if token is authenticated
    get_quote():
        :returns a randomly selected quote, or a default quote if an error occurs
    add_quote(q):
        adds a new quote
        :returns true if quote is added successfully, false otherwise
    check_name(user_name):
        checks if a user name already exists
        :returns true if user name already exists, false otherwise
    get_password(user_name):
        :returns the hashed password and salt if user exists, or empty strings if user isn't found
    get_player(user_name):
        :returns true and player object or false and none if player isn't created
    add_player(user_name, password, salt, gender):
        insert a new player record into database
        :returns  true and player object or false and none if player isn't added
    update_player(player):
        post new changes in player to database
        :returns true if successful or false if an error has occurred
    update_name(old_name, new_name):
        update name of current player in database
        :returns true if successful or false if an error has occurred
    update_password(name,old_password, new_password):
        update password of current player in database
        :returns true if successful or false if an error has occurred
    """
    __instance = None
    __secret_token = "6390ed339b8270b"

    def __init__(self, token):
        if DBManager.__instance is not None:
            raise Exception("Can't create another instance")

        if token == self.__secret_token:
            self.__connection = None
            self.__cursor = None
            DBManager.__instance = self  # static private variable
            if not self.__connect():
                raise Exception("Failed to establish connection")
        else:
            raise Exception("Unauthenticated access to database")

    @staticmethod
    def get_instance(token):
        if DBManager.__secret_token == token:
            if DBManager.__instance is not None:
                return DBManager.__instance
            else:
                return DBManager(token)
        else:
            raise Exception("Unauthenticated access to database")

    def __connect(self):
        try:
            if self.__connection is not None:  # a connection is already established
                return True
            self.__connection = mysql.connector.connect(
                host="localhost",
                user="GameAd",
                passwd="password",
                database="BlackHole"
            )
            print("MySQL Database connection successful")
            self.__cursor = self.__connection.cursor()
            return True
        except Exception as e:
            print(e)
            return False

    def close(self):
        self.__connection.close()
        """self.__connection = None
        self.__cursor = None
        DBManager.__instance = None"""

    def get_quote(self):
        def_q = "Welcome Alien"  # default
        try:
            self.__cursor.execute("SELECT quote FROM quotes ORDER BY RAND() LIMIT 1")
            res = self.__cursor.fetchall()
            if len(res) == 0:
                return def_q
            print(res[0])
            return res[0]
        except Exception as e:
            print(e)
            return def_q

    def add_quote(self, q):
        if not isinstance(q,str) or len(q) == 0:
            return False
        try:
            self.__cursor.execute(f"INSERT INTO quotes(quote) VALUES('{str(q)}')")
            self.__connection.commit()
            return True
        except Exception as e:
            print(e)
            return False

    # for sign up
    def check_name(self, user_name):
        if not isinstance(user_name,str) or len(user_name) == 0:
            return False
        try:
            self.__cursor.execute(f"SELECT name FROM user_info WHERE name = '{str(user_name)}'")
            res = self.__cursor.fetchall()
            if len(res) == 0:
                False
            print(res[0])
            return True
        except Exception as e:
            print(e)
            return False

    # for sign in & profile > returns pair of empty strings if user_name isn't found
    def get_password(self, user_name):
        if not isinstance(user_name,str) or len(user_name) == 0:
            return False
        try:
            self.__cursor.execute(f"SELECT password, salt FROM user_info WHERE name = '{str(user_name)}'")
            res = self.__cursor.fetchall()
            if len(res) == 0:
                return "", ""
            print(res[0])
            return res[0]
        except Exception as e:
            print(e)
            return "", ""

    # used after authentication
    def get_player(self, user_name):
        if not isinstance(user_name,str) or len(user_name) == 0:
            return False
        try:
            self.__cursor.execute(f"SELECT * FROM user_info WHERE name = '{str(user_name)}'")
            res = self.__cursor.fetchall()
            if len(res) == 0:
                return False, None
            player_data = res[0]

            player = Player.build_player(
                player_data[0],  # name
                player_data[3],  # gender
                player_data[4],  # avatar
                player_data[5],  # level
                player_data[6],  # xp
                player_data[7],  # weekly_xp
                player_data[8],  # wins
                player_data[9],  # games
                player_data[10]  # daily_ch
            )
            if player is None:
                return False, None
            return True, player
        except Exception as e:
            print(e)
            return False, None

    # add new player in sign up
    def add_player(self, user_name, password, salt, gender=False):
        if not isinstance(user_name,str) or len(user_name) == 0 or not isinstance(password,str) or len(password) == 0 or not isinstance(salt,str) or len(salt) == 0 or not isinstance(gender,bool):
            return False
        gender = 1 if gender else 0

        try:
            self.__cursor.execute(
                f"INSERT INTO user_info(name, password, salt, gender) VALUES('{str(user_name)}', '{str(password)}','{str(salt)}', {gender})")
            self.__connection.commit()
            player = Player.build_player(
                user_name,  # name
                gender  # gender
            )
            if player is None:
                return False, None
            return True, player
        except Exception as e:
            print(e)
            return False, None

    # update progress, not name and password
    def update_player(self, player):
        if not isinstance(player, Player) or player is None:
            return False

        if player.get_gender():
            gender = 1
        else:
            gender = 0
        try:
            self.__cursor.execute(
                f"UPDATE user_info SET name = '{player.get_name()}', gender = {gender}, avatar = '{player.get_avatar()}', level = {player.get_level()}, xp = {player.get_xp()}, weekly_xp = {player.get_weekly_xp()}, wins = {player.get_wins()}, games = {player.get_games()}, daily_ch = {player.get_daily_ch()}")
            self.__connection.commit()
            return True
        except Exception as e:
            print(e)
            return False

    # update name in profile
    def update_name(self, old_name, new_name):
        if not isinstance(old_name, str) or len(old_name) == 0 or not isinstance(new_name,str) or len(new_name) == 0:
            return False
        try:
            self.__cursor.execute(f"UPDATE user_info SET name = '{str(new_name)}' WHERE name = '{str(old_name)}'")
            return True
        except Exception as e:
            print(e)
            return False

    # update password in profile
    def update_password(self, name, old_password, new_password):
        if not isinstance(name,str) or len(name) == 0 or not isinstance(old_password,str) or len(old_password) == 0 or not isinstance(new_password,str) or len(new_password) == 0:
            return False
        try:
            self.__cursor.execute(
                f"UPDATE user_info SET password = '{str(new_password)}' WHERE name = '{str(name)}' AND password = '{str(old_password)}'")
            return True
        except Exception as e:
            print(e)
            return False
