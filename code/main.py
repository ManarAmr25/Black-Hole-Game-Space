from models import player, stats
from database import db_manager

# player test
'''p = player.Player("Momo")
print(p.get_name())
print(p.get_level())
p.increase_xp(0)
print(p.get_level())
'''

db = db_manager.DBManager()
print(db.connect())
print(db.get_quote())
print(db.get_quote())
print(db.get_player("GameAd"))
print(db.get_player("Game"))
#print(db.add_quote("Time is the mind of space"))
print(db.get_quote())
print(db.add_player("test_player", "123456789", True))

