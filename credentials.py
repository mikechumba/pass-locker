class Credentials:

   '''
   Class that generates instances for account credentials
   '''

   credentials_list = []

   def __init__(self,account,acc_username,acc_password):

      '''
      Will define properties for this class
      '''

      self.account = account
      self.acc_username = acc_username
      self.acc_password = acc_password