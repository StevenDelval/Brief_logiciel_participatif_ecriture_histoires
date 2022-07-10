import os
import CRUD

def clear_terminal():
    """
    Fonction qui nettoye le terminal.
    """
    my_os = os.name
    if my_os == "posix":
        os.system('clear')
    else:
        os.system('cls')

def print_last_paragraph(dernier_paragraph):
    
    print("""Chapitre {0} : Résumé\n
        {4}\n
        ________
        \n
        Posté par : {1} | {2} \n
        \n
        {3}
        """.format(dernier_paragraph[0],dernier_paragraph[1],dernier_paragraph[2],dernier_paragraph[3],dernier_paragraph[4]))
        

def print_paragraph(index,paragraphs):
    """
    Fonction qui affiche le numero de chapitre, le resumer un paragraphe
    :param index(int): numero de paragraphe
    :param paragraphs(list): liste des paragraphes 
    """
    clear_terminal()
    if index < len(paragraphs) :
        print("""Chapitre {0} \n
        Resumer :\n
        {1}\n
        __________________\n
        {2}\n
        """.format(paragraphs[index][0],paragraphs[index][1],paragraphs[index][2]))
    else :
        print("Il n'y a plus de paragraphe\n")
        
def find_index_chapter(Chapter,story):
    """
    Fonction qui renvoie l'index du premier paragraphe du chapitre choisi
    :param chapter (int) Le numrero de chapitre
    :param story (list) Liste des pagragraphes
    :return (int) l'index du premier paragraphe du chapitre choisi
    """
    n = 0
    for paragraph in story:
        if paragraph[0] == Chapter:
            return n
        n +=1
    return len(paragraph)

def print_paragraph_contest(contest,paragraph):
    print("""L'utilisateur {0} conteste le paragraphe suivant:\n

        Chapitre {2}: (Résumé)\n
        {6}
        ________
        \n
        Posté par : {3} | {4} \n
        \n
        {5}

        Voici son commentaire :
        {1}
        """.format(contest[0],contest[1],paragraph[0],paragraph[1],paragraph[2],paragraph[3],paragraph[4]))

def print_comment(comment):
    print("""
    Posté par {0} | {1}
    {2}
    """.format(comment[0],comment[1],comment[2]))


def print_paragraph_and_caracter(paragraph,caracters):
    print("""Chapitre {0} : Résumé\n
        {4}\n
        ________
        \n
        Posté par : {1} | {2} \n
        \n
        {3}\n
        _________
        """.format(paragraph[0],paragraph[1],paragraph[2],paragraph[3],paragraph[4]))
    print("Liste des personnages :",end=" ")
    for perso in caracters:
        if not perso == caracters[-1]:
            print(perso[0],perso[1],end=", ")
        else :
           print(perso[0],perso[1],end="") 
    print("\n_________")