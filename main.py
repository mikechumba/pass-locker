from user_class import User
from credentials import Credentials
import getpass
import random

def create_user(username,password):
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


def generate_pass(length):

   characters = ['1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','m','n','o','p','.','-','$','@']

   pass_word = ''

   while (len(pass_word) < length):
      index = random.randint(0,23)
      character = characters[index]
      pass_word += character

   return pass_word

def log_in():

   print("Do you have a Password Locker account? Y/n")

   has_account = input()

   if has_account == "Y":
      print("This is Password Locker. Enter your username to proceed:")

      user_name = input()

      if user_name in User.user_list:
         print(f"Enter the password for {user_name}:")

         pass_word = getpass.getpass()
         print(User.user_list)
      else:
         print("Oops! Seems like you don't have an account. Press esc to go to the main page.")

   else:
      print("""Create a new account
      ________________________________________
      """)
      print("Enter a username:")

      user_name = input()

      if len(user_name) > 1:
         print("Enter a password")

         pass_word = getpass.getpass()

         print("Confirm password")

         pass_confirm = getpass.getpass()

         if pass_word == pass_confirm:
            create_user(user_name,pass_word)

            print(f'''

            *****************************

            Welcome {user_name.title()}''')

            acc_cred = Credentials.find_credentials(user_name)

            if acc_cred:
               for credential in Credentials.credentials_list:
                  print(f"")

            else:
               print('''
               You don't have any credentials saved

               *****

               Create new credentials
               ''')

               print("Enter account name (Twitter, Instagram, Github, etc):")

               acc_name = input()

               print("Enter your chosen username:")

               acc_username = input()

               print("""
               To enter your own password, enter 'a'.
               To have us generate a password for you, press any key then enter to have it generated for you""")

               action_cmd = input()

               if action_cmd == 'a':
                  input("Enter a password. Ensure it's long enough")

                  pass_word = input()

                  print(f"Here is your password: {pass_word}")
               else:
                  print("Please enter your desired password length. We advice greater than 8")

                  length = input()

                  pass_word = generate_pass(length)
                  print(f"Here's your password: {pass_word}")

                  Credentials.display_credentials()

                  print('\n')

print(generate_pass(15))
