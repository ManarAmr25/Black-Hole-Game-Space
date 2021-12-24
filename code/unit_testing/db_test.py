import unittest

from database.db_manager import DBManager
from models.player import Player

correct_token = "6390ed339b8270b"
wrong_token = "1390ed339b8270b"


class MyTestCase(unittest.TestCase):
    def test_singleton(self):  # first connection with init
        with self.assertRaises(Exception):  # wrong token first initialization
            db = DBManager(wrong_token)

        db1 = DBManager(correct_token) # correct and first
        with self.assertRaises(Exception):  # correct token second initialization
            db = DBManager(correct_token)

        db2 = DBManager.get_instance(correct_token)
        self.assertEqual(db1, db2)  # same instance

        DBManager.__instance = None

        ################################

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
        self.assertTrue(db.add_quote("Never give up")) # successful addition
        self.assertNotEqual(db.get_quote(),"Welcome Alien") # sucessful query
        # invalid inputs
        self.assertFalse(db.add_quote(None))
        self.assertFalse(db.add_quote(""))
        self.assertFalse(db.add_quote(85))

    def test_new_player(self):
        db = DBManager.get_instance(correct_token)




if __name__ == '__main__':
    unittest.main()
