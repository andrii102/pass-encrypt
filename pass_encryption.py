from base64 import b64encode, b64decode
from cryptography.fernet import Fernet
import getpass

def encrypt_password(password):
    """Encrypts a password using AES-256 encryption."""
    key = Fernet.generate_key()
    cipher = Fernet(key)
    encrypted_password = cipher.encrypt(password.encode('utf-8'))
    return encrypted_password.decode('utf-8'), key.decode('utf-8')

def decrypt_password(encrypted_password, key):
    """Decrypts an encrypted password using AES-256 encryption."""
    cipher = Fernet(key)
    decrypted_password = cipher.decrypt(encrypted_password.encode('utf-8'))
    return decrypted_password.decode('utf-8')

def view():
    try:
        with open('password.txt', 'r') as f:
            for line in f.readlines():
                name, encrypted_password, key = line.strip().split('|')
                decrypted_password = decrypt_password(encrypted_password, key)
                print(f"Account name: {name}")
                print(f"Decrypted password: {decrypted_password}")
    except FileNotFoundError:
        print("Password file not found.")

def add():
    name = input("Account name: ")
    password = getpass.getpass("Password: ")

    encrypted_password, key = encrypt_password(password)

    with open('password.txt', 'a') as f:
        f.write(f"{name}|{encrypted_password}|{key}\n")

while True:
    mode = input("What do you want to do (view, add, or q to quit) - ").lower()
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue
