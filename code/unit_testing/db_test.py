import unittest

from database.db_manager import DBManager
from models.player import Player

correct_token = "6390ed339b8270b"
wrong_token = "1390ed339b8270b"
salt = "32abcdef"
p = "password1234"

class MyTestCase(unittest.TestCase):
    def test_singleton_init(self):  # first connection with init
        with self.assertRaises(Exception):  # wrong token first initialization
            db = DBManager(wrong_token)
        db1 = DBManager(correct_token)  # correct and first

        with self.assertRaises(Exception):  # correct token second initialization
            db = DBManager(correct_token)

        db2 = DBManager.get_instance(correct_token)
        self.assertEqual(db1, db2)  # same instance
        DBManager.__instance = None

    def test_singelton_get_instance(self):
        db1 = DBManager.get_instance(correct_token)
        with self.assertRaises(Exception):  # correct token second initialization
            db2 = DBManager(correct_token)
        db2 = DBManager.get_instance(correct_token)
        self.assertEqual(db1, db2)
        DBManager.__instance = None

    def test_connection_Failure(self):
        db = DBManager.get_instance(correct_token)
        db.close()
        # connection failure
        self.assertEqual(db.get_quote(), "Welcome Alien")  # default
        self.assertFalse(db.add_quote("dummy"))  # false
        self.assertFalse(db.check_name("dummy"))  # false
        self.assertEqual(db.get_password("dummy"), ("", ""))
        self.assertEqual(db.get_player("dummy"), (False, None))
        self.assertEqual(db.add_player("dummy", "password", "salt"), (False, None))
        self.assertFalse(db.update_player(Player()))
        self.assertFalse(db.update_name("old dummy", "new dummy"))
        self.assertFalse(db.update_password("dummy", "password1", "password2"))

        DBManager.__instance = None

    def test_quotes(self):
        db = DBManager.get_instance(correct_token)
        self.assertTrue(db.add_quote("Never give up"))  # successful addition
        self.assertNotEqual(db.get_quote(), "Welcome Alien")  # sucessful query
        # invalid inputs
        self.assertFalse(db.add_quote(None))
        self.assertFalse(db.add_quote(""))
        self.assertFalse(db.add_quote(85))
        DBManager.__instance = None

    def test_add_player(self):
        db = DBManager.get_instance(correct_token)
        # invalid input
        self.assertEqual(db.add_player("", "", None, 0), (False, None))
        self.assertEqual(db.add_player(None, 0, ""), (False, None))
        check, player = db.add_player("Game", p, salt)

        self.assertTrue(check)
        self.assertEqual(player.get_name(), "Game")
        self.assertFalse(player.get_gender())       # default gender false
        self.assertEqual(db.get_password("Game"), (p, salt))

        self.assertEqual(db.add_player("Game", p, salt), (False, None))
        DBManager.__instance = None


    def test_check_name(self):
        db = DBManager.get_instance(correct_token)
        # invalid input
        self.assertFalse(db.check_name(""))
        self.assertFalse(db.check_name(None))
        self.assertFalse(db.check_name("this is player"))  # user doesn't exist
        db.add_player("Game1", p, salt)
        self.assertTrue(db.check_name("Game1"))  # user exists
        DBManager.__instance = None

    def test_get_password(self):
        db = DBManager.get_instance(correct_token)
        # invalid input
        self.assertEqual(db.get_password(""), ("", ""))
        self.assertEqual(db.get_password(None), ("", ""))
        self.assertEqual(db.get_password("this is player"), ("", ""))  # user doesn't exist
        db.add_player("Game2", p, salt)
        self.assertEqual(db.get_password("Game2"), (p, salt))  # user exists
        DBManager.__instance = None

    def test_get_player(self):
        db = DBManager.get_instance(correct_token)
        # invalid input
        self.assertEqual(db.get_player(""), (False, None))
        self.assertEqual(db.get_player(None), (False, None))
        self.assertEqual(db.get_player("this is player"), (False, None))  # user doesn't exist
        db.add_player("Game3", p, salt)
        check,player = db.get_player("Game3")
        self.assertTrue(check)  # user exists

    def test_update_player(self):
        db = DBManager.get_instance(correct_token)
        # invalid input
        self.assertFalse(db.update_player(None))
        self.assertFalse(db.update_player(25))
        self.assertFalse(db.update_player("player"))
        player = Player.build_player("not_exist")
        self.assertFalse(db.update_player(player)) # player doesn't exist
        db.add_player("Game4", p, salt)
        player = Player.build_player("Game4")
        player.set_games(10)
        self.assertTrue(db.update_player(player)) # player exists

    def test_update_name(self):
        db = DBManager.get_instance(correct_token)
        # invalid input
        self.assertFalse(db.update_name(0, 5))
        self.assertFalse(db.update_name("", None))
        self.assertFalse(db.update_name("does_exist", "new_player")) # player doesn't exist
        db.add_player("Game5", p, salt)
        self.assertTrue(db.update_name("Game5", "Admin")) # player exists

    def test_update_password(self):
        db = DBManager.get_instance(correct_token)
        # invalid input
        self.assertFalse(db.update_password(0, 5, 6))
        self.assertFalse(db.update_password("", None, None))
        self.assertFalse(db.update_password("does_exist", "new_player", "514"))  # player doesn't exist
        db.add_player("Game6", p, salt)
        self.assertTrue(db.update_password("Game6", p, "passsss123" ))  # player exists

if __name__ == '__main__':
    unittest.main()