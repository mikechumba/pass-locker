class Credentials:

   '''
   Class that generates instances for account credentials
   '''

   credentials_list = []

   def save_credentials(self):
      '''
      This method saves credentials in the credentials_list
      '''

      Credentials.credentials_list.append(self)

   def delete_credentials(self):
      '''
      This will delete saved credentials from credentials_list
      '''

      Credentials.credentials_list.remove(self)

   @classmethod
   def find_credentials(cls, string):
      '''
      this method accesses credentials in credentials_list
      '''

      for credential in cls.credentials_list:
         if credential.account == string:
               return credential

   @classmethod
   def display_credentials(cls):
      '''
      method that returns the credentials
      '''
      return cls.credentials_list

   def __init__(self, username, account, acc_credentialsname, acc_password):
      '''
      Will define properties for this class
      '''
      self.username = username
      self.account = account
      self.acc_credentialsname = acc_credentialsname
      self.acc_password = acc_password
