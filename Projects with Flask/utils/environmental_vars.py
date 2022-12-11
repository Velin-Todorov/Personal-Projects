import secrets

def secret_key():
    return secrets.token_hex()