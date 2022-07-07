
import function
import CRUD
import sqlite3 

function.clear_terminal()

last_chapter = str(CRUD.find_id_last_chapter())
print("Chapitre"+last_chapter)
print(CRUD.read_chapter(last_chapter))
print("----------------------")
print("Liste des personnages:"+CRUD.read_personnage(last_chapter))
print("----------------------")
print("dernier message:")
print("posté par:"+CRUD.read_date_comment(last_chapter))
print(CRUD.read_comment(last_chapter))

input("Entrez votre commande:\n  \n (s : écrire la suite | R : retourner au menu précedent |A : ajouter un personnege existant| C: créer un nouveau personnage|x: clore la chapitre")



