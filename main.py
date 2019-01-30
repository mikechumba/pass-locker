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

def disp_cred(name):
   '''
   Function to display saved credentials
   '''
   cred = Credentials.display_credentials()

   for credential in cred:
      if credential.username == name:
         return f'''
         ________________________________________
         {credential.account.title()}  **  {credential.acc_credentialsname}  **  {credential.acc_password}
         ________________________________________ 
         '''


def find_cred(cred):
   '''
   Method to find specific credential
   '''

   credential = Credentials.find_credentials(cred)

   return f'''
              ******
   Your search for {cred} returned:
   _________________________________
   {credential.account.title()}  |  {credential.acc_credentialsname}  |  {credential.acc_password}
   _________________________________
   '''


def del_cred(credential):
   '''
   Method to delete credentials
   '''

   Credentials.delete_credentials(credential)

def del_user(user):
   '''
   Function to delete a User
   '''
   User.delete_user(user)


def generate_pass(length = 8):

   characters = ['1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','m','n','o','p','.','-','$','@']

   pass_word = ''

   while (len(pass_word) < length):
      index = random.randint(0,22)
      character = characters[index]
      pass_word += character

   return pass_word


# functions to reusable conditions

# main funtion that performs all the user actions

def log_in():

   while True:
      print('''
      -------------------------------------
      |     Welcome To Password Locker    |
      -------------------------------------
      To LOG IN, enter 'l'. To SIGN UP, enter 's'. To exit, enter 'exit' 
      ''')

      user_input = input()

      if user_input == 'l':
         print('''
             ****
         Account log in.

             ****
         ''')
         print('Enter your username:')
         user_name = input()

         print('Enter Password:')
         pass_word = input()

         for user in User.user_list:
            if user_name == user.username and pass_word == user.password:
               print('''
                  ***
               Log in successful.
               ''')
               while True:
                  print('''
                  To ADD new credentials, enter 'new'. To DELETE credentials, enter 'del'. To FIND credentials, enter 'find'. 
                  To LOG Out, enter 'out'.          
                  ''')

                  if disp_cred(user_name):
                     print(disp_cred(user_name))
                  else:
                     print('''

                                 ********
                     You don't have any saved credentials

                                 ********
                     ''')


                  user_input = input()

                  if user_input == 'new':
                     print("Enter account name (Twitter, Instagram, Github, etc):")

                     acc_name = input().title()

                     print("Enter your chosen username:")

                     acc_user = input()

                     print("""
                     To enter your own password, enter 'me'.
                     To have us generate a password for you, press any key then enter to have it generated for you.""")

                     action_cmd = input()

                     if action_cmd == 'me':
                        input("Enter a password. Ensure it's long enough")

                        pass_word = input('\n')

                        print(f"You've succesfully created new credentials. Here is your password: {pass_word}.")

                        save_credentials(create_credentials(user_name,acc_name,acc_user,pass_word))

                     else:
                        print("Please enter your desired password length. We advice greater than 8")

                        length = input()

                        if length == '':
                           length = 8
                                                   
                           pass_word = generate_pass(int(length))
                           print(f"You've succesfully created new credentials. Here's your password: {pass_word}")

                           save_credentials(create_credentials(user_name,acc_name,acc_user,pass_word))
                        else:
                           pass_word = generate_pass(int(length))
                           print(f"You've succesfully created new credentials. Here's your password: {pass_word}")

                           save_credentials(create_credentials(user_name,acc_name,acc_user,pass_word))


                  elif user_input == 'find':
                     print("Enter name of the account you want to find:")

                     acc_name = input('\n')

                     print(find_cred(acc_name))

                  elif user_input == 'del':
                     print('Enter name of account you want to delete:')

                     acc_name = input('\n').title()

                     for credential in Credentials.credentials_list:
                        if credential.account == acc_name:
                           del_cred(credential)
                           print(f'''
                           You have successfully deleted the credentials for {acc_name}.
                           ''')
                        else:
                           print(f'''
                           {acc_name} doesn't exist in your saved credentials.
                           ''')
                     
                  elif user_input == 'out':
                     break

            else:

               print("The username or password you entered isn't valid.")
               user_input = 's'

      elif user_input == 's':
         print('''
                 ****
         Sign up for an account.

         ______________________
         
                 ****

         After creating your account you'll be taken to the main page where you can log in using your sign up details.

         ----
         ''')

         print('Enter your username:')
         user_name = input()

         print('Enter Password:')
         pass_word = input()
         
         save_user(create_user(user_name,pass_word))

         print('''
             ***
         Sign up successful.
         ''')

      elif user_input == 'exit':
         exit()

   

print(log_in())
