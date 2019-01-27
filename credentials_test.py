import unittest
from credentials import Credentials

class TestCredentials(unittest.TestCase):

   '''
   Test class that checks the behaviours of the credentials class.
   '''

   def setUp(self):
      
      self.new_credentials = Credentials("Instagram","michael", "password") # create contact object


   def test_init(self):
      

      self.assertEqual(self.new_credentials.account,"Instagram")
      self.assertEqual(self.new_credentials.acc_credentialsname,"michael")
      self.assertEqual(self.new_credentials.acc_password,"password")

   def test_save_credentials(self):

      self.new_credentials.save_credentials()
      self.assertEqual(len(Credentials.credentials_list),1)

   def tearDown(self):
      '''
      this will clean up after each test run.
      '''
      Credentials.credentials_list = []

   def test_save_multiple_credentials(self):
      '''
      check if a credentials account can hold multiple credentials
      '''
      self.new_credentials.save_credentials()
      test_credentials = Credentials("Twitter","michael","password") 
      test_credentials.save_credentials()
      self.assertEqual(len(Credentials.credentials_list),2)


   def test_delete_credentials(self):
      '''
      test_delete_credentials to test if we can remove a credentials from our credentials list
      '''
      self.new_credentials.save_credentials()
      test_credentials = Credentials("Instagram", "michael", "password")
      test_credentials.save_credentials()

      self.new_credentials.delete_credentials()
      self.assertEqual(len(Credentials.credentials_list),1)


if __name__ == '__main__':
   unittest.main()
