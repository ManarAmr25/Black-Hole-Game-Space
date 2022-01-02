import abc


class AchievementInterface(abc.ABC):
    # to notify
    def update(self, achievement_type):
        pass
