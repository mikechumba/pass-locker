import unittest
from user_class import User

class TestUser(unittest.TestCase):

   '''
   Test class that checks the behaviours of the User class.
   '''

   def setUp(self):
      
      self.new_user = User("michael","password") # create user object


   def test_init(self):
      

      self.assertEqual(self.new_user.username,"michael")
      self.assertEqual(self.new_user.password,"password")

   def test_save_user(self):

      self.new_user.save_user()
      self.assertEqual(len(User.user_list),1)

   def tearDown(self):
      '''
      this will clean up after each test run.
      '''
      User.user_list = []

   def test_save_multiple_user(self):
      '''
      check if we can hold multiple user accounts
      '''
      self.new_user.save_user()
      test_user = User("andrew","password") 
      test_user.save_user()
      self.assertEqual(len(User.user_list),2)

   def test_delete_user(self):
      '''
      test_delete_user to test if we can remove a user from our user list
      '''
      self.new_user.save_user()
      test_user = User("michael", "password")
      test_user.save_user()

      self.new_user.delete_user()
      self.assertEqual(len(User.user_list),1)


if __name__ == '__main__':
   unittest.main()
