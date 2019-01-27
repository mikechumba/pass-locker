
class User:

   '''
   Class that generates instances of user accounts. 
   It will hold the username and password of an account
   '''

   user_list = []

   def save_user(self):

      '''
      This method saves users into the user_list
      '''

      User.user_list.append(self)

   def __init__(self,username,password):

      '''
      Will define properties for this class
      '''

      self.username = username
      self.password = password


