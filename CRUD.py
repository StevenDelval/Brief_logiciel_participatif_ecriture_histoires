import sqlite3 
from datetime import datetime

from matplotlib.pyplot import text

import function

#### Create ####
def create_user(username, password):
    password = function.crypt(password)
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("INSERT INTO User VALUES (?,?,?);", (None,username, password))
    connexion.commit()
    connexion.close()



def create_paragraph (ChapterID, UserID, paragraph):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("INSERT INTO Paragraph VALUES (?,?,?,?,?);", (None, ChapterID, UserID, str(datetime.now()), paragraph))
    connexion.commit()
    connexion.close()


def create_Chapter(Summary_TEXT):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("INSERT INTO Chapter VALUES (?,?);", (None, Summary_TEXT))
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
    pw = function.crypt(pw)
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("SELECT Username FROM User WHERE Username= ? and Password = ?",(username,pw))
    if len(curseur.fetchall()) != 0:
        return True
    else:
        return False


def read_sommary(ChapterID):
    """
    fonction afficher sommaire 
    : parametre numero de chapitre ID
    : return sommaire

    """
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("SELECT  Summary FROM Chapter WHERE ChapterID= ?",(ChapterID,))
    return curseur.fetchone()



def afficher_dernier_paragraph():
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    # curseur.execute("SELECT text, UserID, date FROM Paragraph")
    # curseur.lastrowid 
    curseur.execute("SELECT User.Username, date, text FROM Paragraph JOIN USER ON USER.USERID = Paragraph.UserID ORDER BY ParagraphID DESC LIMIT 1")
    last_paragraph = curseur.fetchone()
    return last_paragraph





#### Update ####

def change_pw(id, password):
    password = function.crypt(password)
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("UPDATE User SET Password = ? WHERE UserId = ?", (password, id))
    connexion.commit()
    connexion.close()

#### Delete ####



