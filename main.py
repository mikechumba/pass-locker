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

def create_credentials(username,account,acc_username,acc_password):

   '''
   Function to create new Credentials
   '''
   new_credentials = Credentials(username,account,acc_username,acc_password)
   return new_credentials

def save_credentials(credentials):
   '''
   Saves created credentials
   '''

   Credentials.save_credentials(credentials)


def save_user(user):
   '''
   Saves created credentials
   '''
   User.save_user(user)

def disp_cred():
   '''
   Function to display saved credentials
   '''

   # return Credentials.display_credentials()

   for credential in Credentials.credentials_list:
      return f'''
      ________________________________________
      {credential.account.title()}  **  {credential.acc_credentialsname}  **  {credential.acc_password}
      ________________________________________ 
      '''

def del_user(user):
   '''
   Function to delete a User
   '''
   User.delete_user(user)


# def find_user(number):
#     '''
#     Function that finds a User by number and returns the User
#     '''
#     return User.find_by_number(number)


def generate_pass(length):

   characters = ['1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','m','n','o','p','.','-','$','@']

   pass_word = ''

   while (len(pass_word) < length):
      index = random.randint(0,22)
      character = characters[index]
      pass_word += character

   return pass_word

def log_in():

   program_run = 'run';


   while program_run == 'run':
      print("""
      --------------------------------
      |  Welcome To Password Locker  |
      --------------------------------

      Do you have a Password Locker account? Y/n


      """)

      has_account = input()

      while True:
         if has_account == "Y":
            print("Enter your username to proceed:")

            user_name = input()

            if user_name in User.user_list:
               print(f"Enter the password for {user_name}:")

               pass_word = getpass.getpass()
               print(User.user_list)
            else:
               print("Oops! There's no account going by that username.")
 
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

                     acc_user = input()

                     print("""
                     To enter your own password, enter 'a'.
                     To have us generate a password for you, press any key then enter to have it generated for you""")

                     action_cmd = input()

                     if action_cmd == 'a':
                        input("Enter a password. Ensure it's long enough")

                        pass_word = input()

                        print(f"Here is your password: {pass_word}")

                        save_credentials(create_credentials(user_name,acc_name,acc_user,pass_word))

                        print(disp_cred())

                        print('\n')
                     else:
                        print("Please enter your desired password length. We advice greater than 8")

                        length = int(input())

                        pass_word = generate_pass(length)
                        print(f"Here's your password: {pass_word}")

                        save_credentials(create_credentials(user_name,acc_name,acc_user,pass_word))

                        print(disp_cred())

                        print('\n')


   
print(log_in())
