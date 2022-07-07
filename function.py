import os


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
        __________________
        {2}\n
        """.format(paragraphs[index][0],paragraphs[index][1],paragraphs[index][2]))
    else :
        print("Il n'y a plus de paragraphe\n")
        
def find_index_chapter(Chapter,story):
    """
    Fonction qui renvoie l'index du premier paragraphes du chapitre choisi
    """
    n = 0
    for paragraph in story:
        if paragraph[0] == Chapter:
            return n
        n +=1