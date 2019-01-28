
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

   def delete_user(self):

      '''
      This will delete saved user from user_list
      '''

      User.user_list.remove(self)

   @classmethod
   def find_user(cls, string):
      '''
      this method accesses credentials in credentials_list
      '''

      for user in cls.user_list:
         if user.username == string:
               return user

   def __init__(self,username,password):

      '''
      Will define properties for this class
      '''

      self.username = username
      self.password = password


