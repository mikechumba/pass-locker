from user_class import User
from credentials import Credentials

def create_User(username,password):
    '''
    Function to create a new User
    '''
    new_user = User(username,password)
    return new_user


def del_user(user):
   '''
   Function to delete a User
   '''
   User.delete_user()


# def find_user(number):
#     '''
#     Function that finds a User by number and returns the User
#     '''
#     return User.find_by_number(number)

def log_in():

   print("Do you have an account? Y/n")

   has_account = input()

   if has_account == "Y":
      print("This is Password Locker. Enter your username to proceed:")

      user_name = input()

      if user_name in User.user_list:
         print(f"Enter the password for {user_name}:")

         pass_word = input()

         print(User.user_list)
      else:
         print("Oops! Seems like you don't have an account. Press esc to go to the main page.")

   else:
      print("""
      Create a new account
      ________________________________________
      """)
      print("Enter a username:")

      user_name = input()

      if len(user_name) > 1:
         print("Enter a password")

         pass_word = input()

      else:
         print("Enter a valid username")
   

print(log_in())

   

