import sqlite3 

#### Create ####
def create_user(Username, Password):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("INSERT INTO User VALUES (?,?,?);", (None,Username, Password))
    connexion.commit()
    connexion.close()

username=input("username :")
passw="Rien"




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
    
#### Update ####



#### Delete ####