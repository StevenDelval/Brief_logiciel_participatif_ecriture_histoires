
import function
import CRUD
import sqlite3 
import hashlib
connexion = sqlite3.connect("Chinook_Sqlite.sqlite")
curseur = connexion.cursor()

clear_terminal()

print(CRUD.find_id_last_chapter())

def read_chapter(chapterID):
    """
    fonction afficher le sommaire de la chapiterid
    :parametre chapiterID
    :return summary
    """
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("SELECT Summary FROM Chapter WHERE ChapterID =?",(chapterID))
    return curseur.fetchone()

