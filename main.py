from time import sleep
from datetime import datetime
from datetime import timedelta


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
    conteste = CRUD.challenge_is_in_progress()

    if conteste :
        date_format_str = "%d/%m/%Y %H:%M:%S.%f"
        date_debut= CRUD.temps_challenge()[0]
        date_debut= datetime.strptime(date_debut, date_format_str)
        
        now = datetime.now()
        date_now = now.strftime(date_format_str)
        date_now = datetime.strptime(date_now, date_format_str)
        
        date_fin = date_debut  + timedelta(seconds=30)
        if date_now > date_fin:
            conteste = False
            if CRUD.nombre_vote()[0] > 1:
                CRUD.delete_paragraph(CRUD.find_id_last_paragraph()[0])
            CRUD.delete_challenge()
            CRUD.fin_vote()

    dernier_paragraph=CRUD.afficher_dernier_paragraph()
    if conteste:
        paragraph_contest = CRUD.read_challenge()
        function.print_paragraph_contest(paragraph_contest,dernier_paragraph)
        action_connection = "Que voulez vous faire ?\n  \n 1 : Lire l'histoire 2 : Voter  4 : Se Déconnecter   \n "
    else :
        action_connection = "Que voulez vous faire ?\n  \n 1 : Lire l'histoire 2 : Contester le dernier message 3 : Écrire la suite  4 : Se Déconnecter   \n "
        function.print_last_paragraph(dernier_paragraph)


    

    actions = int(input(action_connection))
    if actions == 1:
        ###########################
        #  1 : Lire l'histoire    #
        ###########################
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
                print("Il y a {} chapitre".format(CRUD.find_id_last_chapter()))
                chapitre = int(input("Entrez le numero du chapitre choisie:"))
                i = function.find_index_chapter(chapitre,histoire)
                function.print_paragraph(i,histoire)


            if actions_lire == 4:
                interaction_with_user(username)

            if actions_lire == 5:
                function.clear_terminal()
                chapitre_com = int(input("Dans quelle chapitre voulez vous lire les commentaires ? "))
                comments = CRUD.read_comment(chapitre_com)
                if len(comments) != 0:
                    for com in comments:
                        function.print_comment(com) 
                else:
                    print("Il n'y a pas de commentaire")
                input("Appuyer sur entrée lorsque vous avez fini.")


            if actions_lire == 6:
                print("Il y a {} chapitre".format(CRUD.find_id_last_chapter()))
                chapitre_com = int(input("Dans quelle chapitre voulez vous ecrire un commentaire ? "))
                if chapitre_com <= CRUD.find_id_last_chapter():
                    commentaire_chap= input("Votre commentaire :")
                    CRUD.create_comment(commentaire_chap,chapitre_com,CRUD.find_user_id(username)[0])
                else:
                    print("Le numero de chapitre n'existe pas")
                    sleep(4)
            
            if actions_lire == 7:
                function.clear_terminal()
                print("Il y a {} chapitre".format(CRUD.find_id_last_chapter()))
                chapitreid = int(input("Entrez le numero du chapitre dont vous voulez modifier le resumer :"))
                resumer = input("Entrez le nouveau resumer :")
                CRUD.update_summary(chapitreid, resumer)
                histoire=CRUD.afficher_histoire()

    if actions == 2 :
        #############################################
        # 2 : Contester le dernier message Voter    #
        #############################################
        if not conteste and CRUD.find_id_last_paragraph()[0]:
            function.clear_terminal()
            dernier_paragraph=CRUD.afficher_dernier_paragraph()
            function.print_last_paragraph(dernier_paragraph)
            contester = bool(int(input("Voulez-vous contester le dernier paragraphe ?\n0 = Non\n1 = Oui\n")))
            if contester :
                commentaire = input("Entrez un commentaire :")
                CRUD.start_challenge(CRUD.find_user_id(username)[0],CRUD.find_id_last_paragraph()[0],commentaire)
                CRUD.liste_votant()
                CRUD.vote_utilisateur(CRUD.find_user_id(username)[0])
                interaction_with_user(username)
            else :
                interaction_with_user(username)

        elif CRUD.find_id_last_paragraph()[0] == 0 :
            print("vous ne pouvez pas supprimer ce paragraphe.\n Retour au menu Principal dans 5sec")
            sleep(5)
            interaction_with_user(username)

        else :
            if not CRUD.a_voter(CRUD.find_user_id(username)[0]):
                vote_user = bool(int(input("Voulez-vous voter pour supprimer le paragraphe\n0 = Non\n1 = Oui\n")))
                if vote_user :
                    resultat = CRUD.nombre_vote()[0]
                    resultat +=1
                    CRUD.update_vote(resultat)
                    CRUD.vote_utilisateur(CRUD.find_user_id(username)[0])
                    interaction_with_user(username)
                else:
                    resultat = CRUD.nombre_vote()[0]
                    resultat -=1
                    CRUD.update_vote(resultat)
                    CRUD.vote_utilisateur(CRUD.find_user_id(username)[0])
                    interaction_with_user(username)
            else :
                print("Vous avez deja voter\n Retour au menu Principal dans 5sec")
                sleep(5)
                interaction_with_user(username)


    if actions == 3 and not conteste:
        
        ##########################
        # 3 : Écrire la suite    #
        ##########################
        function.clear_terminal()
        function.print_paragraph_and_caracter(dernier_paragraph,CRUD.every_caracter_in_chapter(CRUD.find_id_last_chapter()))
        
        ##CRUD.create_paragraph (CRUD.find_id_lastchapter(), CRUD.find_user_id(Username)[0], paragraph)
        action_ecrir=int(input("Que voulez vous faire ?\n  \n 1 : écrire la suite  \n 2 : ajouter un personnage existant dans le chapitre 3 : créer un nouveau personnage \n 4 : clore le chapitre 5 : retourner au menu précédent     \n "))
        if action_ecrir == 1:
            if username == CRUD.afficher_dernier_paragraph()[1]:
                print("Vous devais attendre qu'un autre utilisateur crée un paragraphe \n Retour au menu pricipal dans 5 secondes")
                sleep(5)
            else :
                paragraph_user = input("Entrez votre paragraphe :")
                
                CRUD.create_paragraph(CRUD.find_id_last_chapter(),CRUD.find_user_id(username)[0],paragraph_user)
            interaction_with_user(username)

        if action_ecrir == 2 :
            if username == CRUD.afficher_dernier_paragraph()[1]:
                print("Vous devais attendre qu'un autre utilisateur crée un paragraphe \n Retour au menu pricipal dans 5 secondes")
                sleep(5)
            else:
                if len(CRUD.every_caracter()) !=0 :
                    print(CRUD.every_caracter())
                
                    num_perso= input("Entrez le numero du perso :")
                    if CRUD.caracterisinchapter(CRUD.find_id_last_chapter(),num_perso):
                        print("Le perso est deja dans le chapitre \n Retour au menu pricipal dans 5 secondes")
                        sleep(5)
                    else:
                        CRUD.create_isinchapter(num_perso,CRUD.find_id_last_chapter())
                        paragraph_user = input("Entrez votre paragraphe :")
                        CRUD.create_paragraph(CRUD.find_id_last_chapter(),CRUD.find_user_id(username)[0],paragraph_user)
                else:
                    print("Il n'y a pas encore de personnage\n Retour au menu pricipal dans 5 secondes")
                    sleep(5)
            interaction_with_user(username)

        if action_ecrir == 3:
            if username == CRUD.afficher_dernier_paragraph()[1]:
                print("Vous devais attendre qu'un autre utilisateur crée un paragraphe \n Retour au menu pricipal dans 5 secondes")
                sleep(5)
            else:
                first_name = input("Entrez le prenom du perso :")
                last_name = input("Entrez le nom du perso :")
                resume_perso = input("Entrez le résumé du perso :")
                CRUD.create_caracter(first_name,last_name,resume_perso)
                paragraph_user = input("Entrez votre paragraphe :")
                
                CRUD.create_paragraph(CRUD.find_id_last_chapter(),CRUD.find_user_id(username)[0],paragraph_user)
                CRUD.create_isinchapter(CRUD.find_id_last_caracter(),CRUD.find_id_last_chapter())

            interaction_with_user(username)

        if action_ecrir == 4:
            if username == CRUD.afficher_dernier_paragraph()[1]:
                print("Vous devais attendre qu'un autre utilisateur crée un paragraphe \n Retour au menu pricipal dans 5 secondes")
                sleep(5)
            else:
                CRUD.create_chapter("En cour")
                perso_new_paragraph = int(input("1 : ajouter un personnage existant dans le chapitre 2 : créer un nouveau personnage\n"))
                if perso_new_paragraph == 1:
                    print(CRUD.every_caracter())
                    num_perso= input("Entrez le numero du perso :")
                    if CRUD.caracterisinchapter(CRUD.find_id_last_chapter(),num_perso):
                        print("Le perso est deja dans le chapitre \n Retour au menu pricipal dans 5 secondes")
                        sleep(5)
                    else:
                        CRUD.create_isinchapter(num_perso,CRUD.find_id_last_chapter())
                        paragraph_user = input("Entrez votre paragraphe :")
                        CRUD.create_paragraph(CRUD.find_id_last_chapter(),CRUD.find_user_id(username)[0],paragraph_user)
                if perso_new_paragraph == 2:
                    first_name = input("Entrez le prenom du perso :")
                    last_name = input("Entrez le nom du perso :")
                    resume_perso = input("Entrez le résumé du perso :")
                    CRUD.create_caracter(first_name,last_name,resume_perso)
                    paragraph_user = input("Entrez votre paragraphe :")

                    CRUD.create_paragraph(CRUD.find_id_last_chapter(),CRUD.find_user_id(username)[0],paragraph_user)
                    CRUD.create_isinchapter(CRUD.find_id_last_caracter(),CRUD.find_id_last_chapter())

            interaction_with_user(username)
        if action_ecrir == 5:
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
        if CRUD.username_is_in_base(username) :
            function.clear_terminal()
            print("Le nom utilisateur {} est deja pris !".format(username))
        else:
            CRUD.create_user(username, input("Entrez votre mot de passe :"))
            connected = interaction_with_user(username)
            function.clear_terminal()
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


