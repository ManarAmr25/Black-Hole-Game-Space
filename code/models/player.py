# player model
from models import guest


class Player(guest.Guest):
    """
    A class to represent a player.
    ...

    Attributes
    ----------
    __gender : bool
        False if Male, True if Female
    __weekly_xp : int
        total xp collected by a player during the current week
    __wins : int
        total number of wins in any games played by the player since it was registered
    __games : int
        total number of games played by the player since it was registered
    __daily_challenges : int
        total number of daily challenges completed in a row without missing a single challenge

    Methods
    -------
    set_name(name):
        Returns True if name is valid, False otherwise
    set_avatar(avatar):
        Returns True if avatar path is valid, False otherwise
    set_gender(gender):
        Returns True if gender is valid, False otherwise
    get_gender():
        Returns "Female" or "Male"
    """

    def __init__(self):
        super().__init__()
        self.__gender = False
        self.__weekly_xp = 0
        self.__wins = 0
        self.__games = 0
        self.__daily_challenges = 0

    @staticmethod
    def build_player(name, gender=False, avatar=None, lvl=1, xp=0, weekly_xp=0, wins=0, games=0, daily_challenges=0):
        """Build a player with the given parameters. returns none if there are invalid parameters."""
        is_successful = True
        player = Player()
        is_successful &= player.set_name(name)
        is_successful &= player.set_gender(gender)
        is_successful &= player.set_avatar(avatar)
        is_successful &= player.set_level_xp(lvl, xp)
        is_successful &= player.set_weekly_xp(weekly_xp)
        is_successful &= player.set_wins(wins)
        is_successful &= player.set_games(games)
        is_successful &= player.set_daily_challenges(daily_challenges)
        return player if is_successful else None

    def set_name(self, name):
        """
        Sets Player's name, default = "No name"
        """
        if isinstance(name, str) & len(name) > 0:
            self.__name = name
            return True
        else:
            return False

    def set_avatar(self, avatar):
        """
        Sets Player's avatar image, default = None.
        """
        if isinstance(avatar, str) & len(avatar) > 0:
            self.__avatar = avatar
            return True
        else:
            return False

    def set_gender(self, gender):
        """
        Sets Player's gender, default = False.
        """
        if isinstance(gender, bool):
            self.__gender == gender
            return True
        else:
            return False

    def set_weekly_xp(self, xp):
        if isinstance(xp, int) & xp >= 0:
            self.__weekly_xp = xp
            return True
        else:
            return False

    def set_wins(self, wins):
        if isinstance(wins, int) & wins >= 0:
            self.__weekly_xp = wins
            return True
        else:
            return False

    def set_games(self, games):
        if isinstance(games, int) & games >= 0:
            self.__weekly_xp = games
            return True
        else:
            return False

    def set_daily_challenges(self, d_ch):
        if isinstance(d_ch, int) & d_ch >= 0:
            self.__weekly_xp = d_ch
            return True
        else:
            return False

    def get_gender(self):
        """Returns Male or Female"""
        return self.__gender

    def get_weekly_xp(self):
        return self.__weekly_xp

    def get_wins(self):
        return self.__wins

    def get_games(self):
        return self.__games

    def get_daily_challenges(self):
        return self.__daily_challenges

    def increase_weekly_xp(self, xp):
        if isinstance(xp, int) & xp >= 0:
            self.__weekly_xp += xp

    def increment_wins(self):
        self.__wins += 1

    def increment_games(self):
        self.__games += 1
