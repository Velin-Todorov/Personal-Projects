from cryptography.fernet import Fernet
import os

def generate_key():
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    
    
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    """
    Load the previously generated key
    """
    return open("secret.key", "rb").read()