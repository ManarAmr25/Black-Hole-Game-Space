from achievements import AchievementInterface

class XpAchievement(AchievementInterface):

    def __init__(self, describtion, checked, player):
        self.describtion = describtion
        self.curr_player = player
        self.checked = checked
        self.parseDescribtion()

    # des >> reach xp num
    def parseDescribtion(self):
        resArr = self.describtion.split()
        self.max_achievement = int(resArr[-1])  # last index is max number


    def update(self, achievement_type):
        if achievement_type == "xp" and self.curr_player._xp >= self.max_achievement:
            i = 0
            while i < len(self.curr_player.achievements):
                if self.curr_player.achievements[i].describtion == self.describtion:
                    self.curr_player.achievements[i].checked = 1
                    break
                i = i + 1