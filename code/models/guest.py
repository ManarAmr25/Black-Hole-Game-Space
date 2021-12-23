
class Guest:
    """
       A class to represent a player.
       ...

       Attributes
       ----------
       __name : str
           player's user name. uniquely identifies a player
       __avatar : str
           a path (relative to project directory) to the player's avatar image
       __lvl : int
           player's current level. minimum = 1
       __xp : int
           player's xp points in the current level. minimum = 1
       __max_lvl_xp : int
           maximum xp points in the current level. used to calculate the next level's max xp

       Methods
       -------
       set_level_xp(level, xp):
           Returns True if level and xp are valid, False otherwise
       get_name():
           Returns player's name
       get_avatar():
           Returns player's avatar
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

    def __init__(self):
        self.__name = "Guest"
        self.__avatar = None
        self.__lvl = 1
        self.__xp = 0
        self.__max_lvl_xp = 50

    def set_level_xp(self, level, xp):  # level and xp have to be set together
        """
        Sets Player's level and xp, default level = 1, default xp = 0.
        """
        if isinstance(level, int) & level > 0 & isinstance(xp, int) & xp >= 0:
            self.__lvl = level
            self.__max_lvl_xp = 25 * self.__lvl * (1+self.__lvl)
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

    def get_level(self):
        """Returns Player's current level"""
        return self.__lvl

    def get_xp(self):
        """Returns Player's xp points withing the current level"""
        return self.__xp

    def increase_xp(self, xp):
        """Takes xp and adds them to Player's current xp points."""
        if isinstance(xp, int) & xp >= 0:
            self.__xp += xp
            self.__level_up()  # reset level

    def __level_up(self):
        """Increments Player's level if it has enough xp points"""
        while self.__xp >= self.__max_lvl_xp:
            self.__xp -= self.__max_lvl_xp
            self.__lvl += 1  # increment level
            self.__max_lvl_xp = 25 * self.__lvl * (1 + self.__lvl)  # update level maximum xp level
            # self.__max_int_lvl_xp = floor(self.__max_lvl_xp)

    def xp_to_complete(self):
        return self.__max_lvl_xp - self.__xp
