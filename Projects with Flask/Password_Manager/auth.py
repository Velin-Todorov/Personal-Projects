import bcrypt
import encodings.utf_8

def check_if_passwords_match(password, re_pass):
    if password != re_pass:
        return False
    
    return True

