import os
import hashlib


def crypt(password):
    """
    Fonction qui crypte un mot de passe
    :param password (str): mot de passe
    :return (str) le hash du mot de passe
    """
    hash_pwd = hashlib.new('sha256')
    hash_pwd.update(password.encode())
    hash_pwd = hash_pwd.hexdigest()
    return hash_pwd


def clear_terminal():
    my_os = os.name
    if my_os == "posix":
        os.system('clear')
    else:
        os.system('cls')