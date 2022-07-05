import sqlite3 
from datetime import datetime

#### Create ####
def create_user(Username, Password):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("INSERT INTO User VALUES (?,?,?);", (None,Username, Password))
    connexion.commit()
    connexion.close()



def create_paragraph (ChapterID, UserID, paragraph):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("INSERT INTO Paragraph VALUES (?,?,?,?,?);", (None, ChapterID, UserID, str(datetime.now()), paragraph))
    connexion.commit()
    connexion.close()




#### Read   ####

def see_users():
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("SELECT Username,Password FROM User")
    print(curseur.fetchall())
    connexion.close()


def is_in_base(username):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("SELECT Username FROM User WHERE Username= ?",(username,))
    if len(curseur.fetchall()) != 0:
        return True
    else:
        return False

def find_user_id(Username):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("SELECT UserID FROM User WHERE Username= ?",(Username,))
    return curseur.fetchone()

def connexion(username,pw):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("SELECT Username FROM User WHERE Username= ? and Password = ?",(username,pw))
    if len(curseur.fetchall()) != 0:
        return True
    else:
        return False


#### Update ####

def change_pw(id, password):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("UPDATE User SET Password = ? WHERE UserId = ?", (password, id))
    connexion.commit()
    connexion.close()

#### Delete ####



###reader_sommary##

def reader_sommary(ChapterID):
    """
    fonction afficher sommaire 
    : parametre numero de chapitre ID
    : return sommaire

    """
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("SELECT  Summary FROM Chapiter WHERE ChapterID= ?",(ChapterID,))
    return curseur.fetchone()
   