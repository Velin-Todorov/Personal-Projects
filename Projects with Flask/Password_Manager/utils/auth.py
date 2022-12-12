import bcrypt
import encodings.utf_8

def check_if_passwords_match(password, re_pass):
    if password != re_pass:
        return False
    
    return True

def hash_password(password):
    bytes = password.encode('utf-8')
    hashed_password = bcrypt._bcrypt.hashpass(bytes, bcrypt.gensalt(24))
    return hashed_password
