from user_class import User

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
   print("This is Password Locker. Enter your username to proceed")

   user_name = input()

   if user_name == ''

