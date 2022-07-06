import function
import CRUD

# Connexion utilisateur 

have_account = bool(int(input("Avez-vous un compte\n0 = Non\n1 = Oui\n")))
connected = False
count = 0
while not connected:
    if have_account :
        username = input("Entrez votre nom utilisateur :")
        connected = CRUD.connexion(username,input("Entrez votre mot de passe :"))
        if connected :
            function.clear_terminal()
            print("Bonjour {} !".format(username))
        else :
            function.clear_terminal()
            print("Utilisateur ou mot de passe invalide")
            count += 1
    
    else:
        username = input("Entrez un nom utilisateur :")
        if CRUD.is_in_base(username) :
            function.clear_terminal()
            print("Le nom utilisateur {} est deja pris !".format(username))
        else:
            CRUD.create_user(username, input("Entrez votre mot de passe :"))
            connected = True
            function.clear_terminal()
            print("Bonjour {} !".format(username))

    if count > 5 and not connected : 
        function.clear_terminal()   
        forgot_pwd = bool(int(input("Avez-vous un oubliez votre mot de passe\n0 = Non\n1 = Oui\n")))
        if forgot_pwd :
            function.clear_terminal()
            username = input("Entrez votre nom utilisateur :")
            id=CRUD.find_user_id(username)
            
            if id is not None :
                function.clear_terminal()
                CRUD.change_pw(id[0],input("Entrez votre mot de passe :"))
            else:
                function.clear_terminal()
                print("Erreur !")
        else:
            function.clear_terminal()
            have_account = bool(int(input("Avez-vous un compte\n0 = Non\n1 = Oui\n")))

"""
# afficher_dernier_paragraphe
# curseur.lastrowid



actions = int(input("que voulez vous faire \n  \n 0 = ecrire un paragraphe? \n 1 = ecrire un commentaire? \n 2 = lancer un vote?  \n 3 = creer un nouveau chapitre?  \n 4 = voir un résumé de chapitre? \n 5 = voter?\n 6 = voir perso? \n 7= nouv chap? \n 8= delete chapter \n "))

if actions == 0:
    paragraph = input (" Rentrez votre contribution: ")
    CRUD.create_paragraph(paragraph)

elif actions == 1 :
    commentaire = input (" Rentrez votre contribution: ")
    CRUD.create_commentaire(commentaire)
elif actions == 2:
    start_poll
elif actions ==3:
    new_chapter = input (" Rentrez votre contribution: ")
    CRUD.create_paragraph(new_chapter)
elif actions == 4:
    see_resume
elif 
"""


