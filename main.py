import os

import CRUD

have_account = bool(int(input("Avez-vous un compte\n0 = Non\n1 = Oui\n")))
connected = False
count = 0
while not connected:
    if have_account :
        username = input("Entrez votre nom utilisateur :")
        connected = CRUD.connexion(username,input("Entrez votre mot de passe :"))
        if connected :
            print("Bonjour {} !".format(username))
        else :
            print("Utilisateur ou mot de passe invalide")
            count += 1
    
    else:
        username = input("Entrez un nom utilisateur :")
        if CRUD.is_in_base(username) :
            print("Le nom utilisateur {} est deja pris !".format(username))
        else:
            CRUD.create_user(username, input("Entrez votre mot de passe :"))
            connected = True
            print("Bonjour {} !".format(username))

    if count > 5 and not connected :    
        forgot_pwd = bool(int(input("Avez-vous un oubliez votre mot de passe\n0 = Non\n1 = Oui\n")))
        if forgot_pwd :
            username = input("Entrez votre nom utilisateur :")
            id=CRUD.find_user_id(username)
            
            if id is not None :
                CRUD.change_pw(id[0],input("Entrez votre mot de passe :"))
            else:
                print("Erreur !")
        else:
            have_account = bool(int(input("Avez-vous un compte\n0 = Non\n1 = Oui\n")))

