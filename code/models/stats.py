# a player statistics

class Stats:
    def __init__(self, leaderboard_rank=-1, total_games_played=0, total_wins=0, daily_challenges=0):
        self.__lb_rank = leaderboard_rank
        self.__games = total_games_played
        self.__wins = total_wins
        self.__dch = daily_challenges

    def get_leaderboard_rank(self):
        return self.__lb_rank

    def get_total_games_played(self):
        return self.__games

    def get_daily_challenges(self):
        return self.__dch
