import function
import CRUD


function.clear_terminal()

def interaction_with_user(username):
    """
    Fonction qui permet de lire,contestée et écrire un paragraphe
    :return (bool): Renvoie faux lorsque l'utilisateur se deconnecte
    """
    function.clear_terminal()
    print("Bonjour {} ! \n".format(username))
    



    dernier_paragraph=CRUD.afficher_dernier_paragraph()
    print("""
    Dernier message :  Chapitre {0}\n
    Posté par : {1} | {2} \n
    \n
    {3}
    """.format(dernier_paragraph[0],dernier_paragraph[1],dernier_paragraph[2],dernier_paragraph[3]))

    actions = int(input("""Que voulez vous faire ?\n  \n 
    1 : Lire l'histoire 2 : Contester le dernier message 
    3 : Écrire la suite  4 : Se Déconnecter   \n 
    """))
    if actions == 1:
        
        function.clear_terminal()
        histoire=CRUD.afficher_histoire()
        i = 0
        actions_lire =0
        
        while actions_lire !=4:
            function.print_paragraph(i,histoire)
            actions_lire = int(input("""Que voulez vous faire ?\n  \n 
                1 : Lire paragraphe suivant 2 : Lire paragraphe précédent 
                3 : Choisir un chapitre   \n 
                4 : Retourner au menu précédent  
                5 : Lire les commentaires d'un chapitre  6 : Écrire un commentaire sur un chapitre\n
                7 : Modifez resumer d'un chapitre
                """))
            if actions_lire == 1:
                if i != len(histoire):
                    i += 1
                
                function.print_paragraph(i,histoire)
            if actions_lire == 2:
                if i > 0:
                    i -= 1
                function.print_paragraph(i,histoire)
                
            if actions_lire == 3:
                function.clear_terminal()
                chapitre = int(input("Entrez le numero du chapitre choisie:"))
                i = function.find_index_chapter(chapitre,histoire)
                function.print_paragraph(i,histoire)
            if actions_lire == 4:
                interaction_with_user(username)
            
            
            if actions_lire == 7:
                function.clear_terminal()
                chapitreid = int(input("Entrez le numero du chapitre dont vous voulez modifier le resumer :"))
                resumer = input("Entrez le nouveau resumer :")
                CRUD.update_summary(chapitreid, resumer)
                histoire=CRUD.afficher_histoire()
    if actions == 2 :
        function.clear_terminal()
        dernier_paragraph=CRUD.afficher_dernier_paragraph()
        print("""Chapitre {0} : Résumé\n
        {4}\n
        ________
        \n
        Posté par : {1} | {2} \n
        \n
        {3}
        """.format(dernier_paragraph[0],dernier_paragraph[1],dernier_paragraph[2],dernier_paragraph[3],dernier_paragraph[4]))
        contester = bool(int(input("Voulez-vous contester le dernier paragraphe ?\n0 = Non\n1 = Oui\n")))
        if contester :
            pass
        else :
            interaction_with_user(username)
        
    if actions == 4 :
        return False



# Connexion utilisateur 



have_account = bool(int(input("Avez-vous un compte ?\n0 = Non\n1 = Oui\n")))
connected = False
count = 0
while not connected:
    if have_account :
        username = input("Entrez votre nom utilisateur :")
        connected = CRUD.connexion(username,input("Entrez votre mot de passe :"))
        if connected :
            connected = interaction_with_user(username)
            count = 0
            have_account = bool(int(input("Avez-vous un compte ?\n0 = Non\n1 = Oui\n")))
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
            connected = interaction_with_user(username)
            count = 0
            have_account = bool(int(input("Avez-vous un compte ?\n0 = Non\n1 = Oui\n")))

    if count > 5 and not connected : 
        function.clear_terminal()   
        forgot_pwd = bool(int(input("Avez-vous un oubliez votre mot de passe ?\n0 = Non\n1 = Oui\n")))
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
            have_account = bool(int(input("Avez-vous un compte ?\n0 = Non\n1 = Oui\n")))


