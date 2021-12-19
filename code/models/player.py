# player model
from math import floor


class Player:
    """
    A class to represent a player.
    ...

    Attributes
    ----------
    __name : str
        player's user name. uniquely identifies a player
    __avatar : str
        a path (relative to project directory) to the player's avatar image
    __gender : bool
        False if Male, True if Female
    __lvl : int
        player's current level. minimum = 1
    __xp : int
        player's xp points in the current level. minimum = 1
    __max_lvl_xp : double
        maximum xp points in the current level. used to calculate the next level's max xp
    __max_int_lvl_xp : int
        maximum xp points without fractions. used to calculate remaining xp to complete level
        and check if level up is needed


    Methods
    -------
    set_name(name):
        Returns True if name is valid, False otherwise
    set_avatar(avatar):
        Returns True if avatar path is valid, False otherwise
    set_gender(gender):
        Returns True if gender is valid, False otherwise
    set_level_xp(level, xp):
        Returns True if level and xp are valid, False otherwise
    get_name():
        Returns player's name
    get_avatar():
        Returns player's avatar
    get_gender():
        Returns "Female" or "Male"
    get_level():
        Returns player's level
    get_xp():
        Returns player's xp
    increase_xp(xp_points):
        Adds xp_points to player's xp and resets level
    __level_up():
        Increments player's level if needed
    __xp_to_complete():
        Returns the remaining xp points to complete the current level
    """

    __name = "No name"
    __avatar = None
    __gender = False
    __lvl = 1
    __xp = 0
    __max_lvl_xp = 50
    # __max_int_lvl_xp = 10

    # TODO
    def __init__(self, name="none", avatar=None, gender=False, level=1, xp=0):
        pass

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

    # TODO : check if path exists
    def set_level_xp(self, level, xp):  # level and xp have to be set together
        """
        Sets Player's level and xp, default level = 1, default xp = 0.
        """
        if isinstance(level, int) & level > 0 & isinstance(xp, int) & xp >= 0:
            self.__lvl = level
            self.__max_lvl_xp = 25 * self.__lvl * (1+self.__lvl)
            # self.__max_int_lvl_xp = floor(self.__max_lvl_xp)
            self.__xp = xp
            self.__level_up()
            return True
        else:
            return False

    def get_name(self):
        """Returns Player's name"""
        return self.__name

    def get_avatar(self):
        """Returns Player's avatar image path (relative to project directory)"""
        return self.__avatar

    def get_gender(self):
        """Returns Male or Female"""
        return self.__gender

    def get_level(self):
        """Returns Player's current level"""
        return self.__lvl

    def get_xp(self):
        """Returns Player's xp points withing the current level"""
        return self.__xp

    def increase_xp(self, xp_points):
        """Takes xp_points and adds them to Player's current xp points.
           Returns true if params are valid, false otherwise."""
        self.__xp += xp_points
        self.__level_up()  # reset level

    def __level_up(self):
        """Increments Player's level if it has enough xp points"""
        while self.__xp >= self.__max_lvl_xp:
            self.__xp -= self.__max_lvl_xp
            self.__lvl += 1  # increment level
            self.__max_lvl_xp = 25 * self.__lvl * (1+self.__lvl)  # update level maximum xp level
            # self.__max_int_lvl_xp = floor(self.__max_lvl_xp)

    def xp_to_complete(self):
        return self.__max_int_lvl_xp - self.__xp
