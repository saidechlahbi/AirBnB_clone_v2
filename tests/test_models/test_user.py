#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.password), str)
	
    def test_init_with_first_name(self):
        """Test initialization of User with a first name"""
        user = User(first_name="John")
        self.assertEqual(user.first_name, "John")


    def test_attribute_modification(self):
        """Test modification of User attributes"""
        user = User()
        user.first_name = "Alice"
        self.assertEqual(user.first_name, "Alice")


    def test_deletion(self):
        """Test deletion of User instance"""
        user = User()
        user_id = user.id
        user.delete()
        self.assertIsNone(User.get(user_id))

