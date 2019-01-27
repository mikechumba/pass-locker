import unittest
from credentials import Credentials

class TestCredentials(unittest.TestCase):

   '''
   Test class that checks the behaviours of the User class.
   '''

   def setUp(self):
      
      self.new_credentials = Credentials("Instagram","michael", "password") # create contact object


   def test_init(self):
      

      self.assertEqual(self.new_credentials.account,"Instagram")
      self.assertEqual(self.new_credentials.acc_username,"michael")
      self.assertEqual(self.new_credentials.acc_password,"password")

   def test_save_credentials(self):

      self.new_credentials.save_credentials()
      self.assertEqual(len(Credentials.credentials_list),1)

   def test_save_multiple_contact(self):
      '''
      check if a user account can hold multiple credentials
      '''
      self.new_credentials.save_credentials()
      test_credentials = Credentials("Twitter","michael","password") 
      test_credentials.save_credentials()
      self.assertEqual(len(Credentials.credentials_list),2)


if __name__ == '__main__':
   unittest.main()
