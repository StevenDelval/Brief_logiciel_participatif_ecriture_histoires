
import function
import CRUD
import sqlite3 
import hashlib
connexion = sqlite3.connect("Chinook_Sqlite.sqlite")
curseur = connexion.cursor()

clear_terminal()

print("Chapitre"+CRUD.find_id_last_chapter)
print(CRUD.read_chapter(CRUD.find_id_last_chapter))
print("----------------------")
print("Liste des personnages:")
"CRUD.read_chapter(CRUD.find_id_last_chapter())"/n /n Dernier message :/n")


input 