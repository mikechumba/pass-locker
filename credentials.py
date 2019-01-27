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

   def __init__(self,account,acc_username,acc_password):

      '''
      Will define properties for this class
      '''

      self.account = account
      self.acc_username = acc_username
      self.acc_password = acc_password