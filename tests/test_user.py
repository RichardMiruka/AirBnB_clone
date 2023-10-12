#!/usr/bin/python3
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Test cases for the User class"""

    def test_user_attributes(self):
        user = User()
        self.assertTrue(hasattr(user, 'id'))
        self.assertTrue(hasattr(user, 'created_at'))
        self.assertTrue(hasattr(user, 'updated_at'))
        self.assertTrue(hasattr(user, 'email'))
        self.assertTrue(hasattr(user, 'password'))
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertTrue(hasattr(user, 'last_name'))

    def test_to_dict_method(self):
        user = User()
        user_dict = user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertEqual(user_dict['__class__'], 'User')

    def test_str_method(self):
        user = User()
        expected_output = f"[User] ({user.id}) {{'id': '{user.id}', 'created_at': '{user.created_at}', 'updated_at': '{user.updated_at}', 'email': '', 'password': '', 'first_name': '', 'last_name': ''}}"
        self.assertEqual(str(user), expected_output)


if __name__ == '__main__':
    unittest.main()
