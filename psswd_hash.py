import bcrypt
import register_signin
import db_connect

def hash_password(register_password):
    global salt, hash_password
    salt = bcrypt.gensalt()
    hash_password = bcrypt.hashpw(register_password.encode("utf-8"),salt)
    return salt,hash_password

def authenticate(signin_password,stored_hash_password):
    if bcrypt.checkpw(signin_password.encode("utf-8"),stored_hash_password.encode("utf-8")):
        print("Login successful")
    else: print("username or password is wrong, please re enter your credentials")