from cryptography.fernet import Fernet
import os

KEY_FILE = "secret.key"

def load_key():

    if not os.path.exists(KEY_FILE):

        key = Fernet.generate_key()

        with open(KEY_FILE, "wb") as file:
            file.write(key)

    with open(KEY_FILE, "rb") as file:
        return file.read()


key = load_key()

cipher = Fernet(key)


def encrypt(password):
    return cipher.encrypt(password.encode()).decode()


def decrypt(password):
    return cipher.decrypt(password.encode()).decode()