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

   def __init__(self,account,acc_credentialsname,acc_password):

      '''
      Will define properties for this class
      '''

      self.account = account
      self.acc_credentialsname = acc_credentialsname
      self.acc_password = acc_password