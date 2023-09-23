import psswd_hash
import db_connect
import datetime

UserName_Length = 25
Password_Length = 10
phonenumber_Length =10
event_datetime = datetime.datetime.now()

def register():

    #prompting the user for username
    while True:
        username = str(input("please enter your username\n"))
        if 0 != len(username) <= UserName_Length:
            break
        else: print("username should be less than 25 characters and should not be 0 characters")

    #prompting the user for password
    while True:
        register_password = str(input("please enter the password\n"))
        if 0 != len(register_password) <= Password_Length:
            #hashing the password with help of psswd_hash module
            psswd_hash.hash_password(register_password)
            salt = psswd_hash.salt
            hash_password = psswd_hash.hash_password
            break
        else: print("password should be less than 10 characters and should not be 0 characters")

    #prompting the user for phone number
    while True:
        phonenumber = str(input("please enter your phonenumber\n"))
        if len(phonenumber) == phonenumber_Length:
            break
        else: print("phone number should be ten digits")
    
    #Sending the data to database with help of db_connect module
    try:
        db_connect.db_user_register_data(username,phonenumber,salt,hash_password,event_datetime)
        print("Registration successfull")
    except db_connect.mysql.connector.Error as e:
        print(f"Error sending the data to db:-{e}") 

def signin():

    #prompting for username and password
    while True:
      signin_username = str(input("Enter your username\n"))
      if len(signin_username) != 0:
          break
      else: print("username should not be empty")
    while True:
        signin_password = str(input("please enter your password\n"))
        if len(signin_password) != 0:
            break
        else: print("password should not be empty")
    
    #Fetching stored hash password from db
    db_connect.db_fetch_usercredentials(signin_username)
    if db_connect.stored_hash_password != None:
        #Authenticating the username and password
        stored_hash_password = stored_hash_password[0]
        psswd_hash.authenticate(signin_password,stored_hash_password)
    else: print(f"\nusename '{signin_username}' doesn't exist, Try again\n")
    

    





        