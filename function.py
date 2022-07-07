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

def print_paragraph(index,paragraphs):
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
    n = 0
    for paragraph in story:
        if paragraph[0] == Chapter:
            return n
        n +=1