import sqlite3 

#### Create ####
def create_user(Username, Password):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("INSERT INTO User VALUES (?,?,?);", (None,Username, Password))
    connexion.commit()
    connexion.close()



#### Read   ####

def see_users():
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("SELECT Username FROM User")
    print(curseur.fetchall())
    connexion.close()
    

#### Update ####



#### Delete ####