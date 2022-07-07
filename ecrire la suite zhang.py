
import function
import CRUD
import sqlite3 

connexion = sqlite3.connect("Chinook_Sqlite.sqlite")
curseur = connexion.cursor()

function.clear_terminal()

last_chapter = CRUD.find_id_last_chapter
print("Chapitre"+last_chapter)
print(CRUD.read_chapter(last_chapter))
print("----------------------")
print("Liste des personnages:"+CRUD.read_personnage(last_chapter))
print("----------------------")
print("dernier message:"+CRUD.read_comment(last_chapter))
print("posté par:")



