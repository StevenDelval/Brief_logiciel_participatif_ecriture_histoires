import sqlite3 
import hashlib

from datetime import datetime

def crypt(password):
    """
    Fonction qui crypte un mot de passe
    :param password: (str) mot de passe
    :return: (str) le hash du mot de passe
    """
    hash_pwd = hashlib.new('sha256')
    hash_pwd.update(password.encode())
    hash_pwd = hash_pwd.hexdigest()
    return hash_pwd

##############################################################  CREATE  ############################################################### 
##############################################################  CREATE  ############################################################### 

def create_user(username, password):      # CREER UN UTILISATEUR 
    """
    Fonction qui crée un utilisateur et l'ajoute dans la table user 
    :param username: (str) nom de l'utilisateur à ajouté dans la base de données 
    :param password: (str) mot de passe
    :return: None
    """
    password = crypt(password)
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("INSERT INTO User VALUES (?,?,?);", (None,username, password))
    connexion.commit()
    connexion.close()
def create_user_welcom(password=0):      # CREER UN UTILISATEUR 
    """
    Fonction qui crée un utilisateur et l'ajoute dans la table user 
    :param username: (str) nom de l'utilisateur à ajouté dans la base de données 
    :param password: (str) mot de passe
    :return: None
    """
    password = crypt(password)
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("INSERT INTO User VALUES (0,?,?);", ("welcom", "565"))
    connexion.commit()
    connexion.close()

def create_paragraph (ChapterID, UserID, paragraph):        # CREER UN PARAGRAPHE 
    """
    Fonction qui crée un paragraphe et l'ajoute dans la table Paragraph
    :param ChapterID: (int) Numéro du chapitre
    :param UserID:    (int) Numéro de l'utilisateur 
    :param Paragraph: (str) Paragraphe
    :return: None 
    """
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("INSERT INTO Paragraph VALUES (?,?,?,?,?);", (None, ChapterID, UserID, str(datetime.now()), paragraph))
    connexion.commit()
    connexion.close()


def create_chapter(Summary):               # CREER UN CHAPITRE 
    """
    Fonction qui crée un chapitre avec un résumé et l'ajoute dans la table Chapter
    :param Chapter: (str) chapitre 
    :param Summary_TEXT: (str) résumé du chapitre 
    :return: None
    """
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("INSERT INTO Chapter VALUES (?,?);", (None, Summary))
    connexion.commit()
    connexion.close()

def create_comment(text,ChapterID,UserID):      # CREER UN COMMENTAIRE D'UN CHAPITRE 
    """
    Fonction qui crée un commentaire et l'ajoute dans la table Comment  
    :param text: (str) commentaire 
    :param ChapterID: (str) numéro du chapitre
    :param UserID: (str) numéro de l'utilisateur 
    :return: None 
    """
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("""INSERT INTO Comment VALUES (?,?,?,?,?)""",(None,ChapterID,UserID,str(datetime.now()),text ) )
    connexion.commit()
    connexion.close()


def create_caracter(FirstName, LastName, Resume):   # CREER UN PERSONNAGE 
    """
    Fonction qui créer un personnage et l'ajoute dans la table caracter
    :param FirstName: (str) prénom du personnage 
    :param LastName: (str) nom du personnage
    :param Resume: (str) description du personnage
    :return: None
    """
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("INSERT INTO Caracter VALUES (?,?,?,?);", (None, FirstName, LastName, Resume ))
    connexion.commit()
    connexion.close()

def create_isinchapter(caracterID,chapterID):  # AJOUT DE L'ID DU PERSO ET LE CHAPITRE OU IL APPARAIT DANS LA TABLE ISINCHAPTER
    """
    Fonction qui insere l'id d'un personnage et le chapitre correspondant dans la table IsInChapter
    :param caracterID: (int) l'id du personnage 
    :param chapterID: (int) chapitre où apparait le personnage
    :return: None
    """
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("INSERT INTO IsInChapter VALUES (?,?);", (caracterID,chapterID))
    connexion.commit()
    connexion.close()

def start_challenge(UserId, ParagraphID, Text):  # DEMARRER UN VOTE 
    """
    Fonction qui crée la table du vote Challenge et crée l'instance de Vote 
    :param UserId: (int) l'id de l'utilisateur  
    :param ParagraphID: (int) l'id du paragraphe sur lequel les utilisateurs vont voter
    :param Text: (str) texte qui justifie le début du vote 
    :return: None
    """
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    now = datetime.now()
    date_format_str = "%d/%m/%Y %H:%M:%S.%f"
    date_now = now.strftime(date_format_str)
    curseur.execute("INSERT INTO Challenge VALUES (?,?,?,?,?)",(UserId,ParagraphID,Text,1,date_now))
    connexion.commit()
    connexion.close()

def liste_votant():                          # CREER ET IMPLEMENTER LA TABLE VOTE 
    """
    Fonction qui crée la table Vote et l'implémente avec l'UserID qui a voter.
    :param UserId: (int) l'id de l'utilisateur  
    :return: None
    """
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute('''CREATE TABLE Vote
               (
                    UserID INTEGER,
                    FOREIGN KEY(UserID)
                        REFERENCES User(UserID)
                )
    ''')
    connexion.commit()
    connexion.close()

def vote_utilisateur(userID):
    """
    Fonction qui crée la table Vote et l'implémente avec l'UserID qui a voter.
    :param UserId: (int) l'id de l'utilisateur  
    :return: None
    """
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("INSERT INTO Vote VALUES (?)",(userID,))
    connexion.commit()
    connexion.close()   

##############################################################  READ  ############################################################### 
##############################################################  READ  ############################################################### 

def temps_challenge():
    """
    Fonction qui affiche la date du début du challenge.
    :param UserId: (int) l'id de l'utilisateur  
    :return: None
    """
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("SELECT date FROM Challenge")
    return curseur.fetchone()


def a_voter(UserID):
    """
    Fonction qui vérifie si l'utilisateur a voter, la requête renvoie toutes les entrées quand elle verra l'id de l'utilisateur
    c'est un booléen si elle renvoie vrai, l'utilisateur a voter, si c'est faux, il n'a pas voter. 
    :param UserId: (int) l'id de l'utilisateur  
    :return: None
    """
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("SELECT UserID FROM Vote WHERE UserID=?",(UserID,))
    if len(curseur.fetchall()) == 0:
        return False
    else :
        return True

def see_users():
    """
    Fonction qui affiche .
    :param UserId: (int) l'id de l'utilisateur  
    :return: None
    """
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

def caracterisinchapter(ChapterID,CaracterID):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("SELECT CaracterID FROM IsInChapter  WHERE ChapterID = ? and CaracterID =?",(ChapterID,CaracterID))
    if len(curseur.fetchall()) != 0:
        return True
    else:
        return False
def find_id_last_caracter():
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("SELECT CaracterID FROM Caracter ORDER BY CaracterID DESC LIMIT 1")
    return curseur.fetchone()[0]
def isInChapter(FirstName):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("SELECT ChapterId FROM IsInChapter JOIN Caracter ON Caracter.CaracterID = IsInChapter.CaracterID WHERE FirstName = ? ",(FirstName,))
    print(curseur.fetchall())
    connexion.close()


def find_user_id(Username):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("SELECT UserID FROM User WHERE Username= ?",(Username,))
    return curseur.fetchone()

def connexion(username,pw):
    pw = crypt(pw)
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
    curseur.execute("SELECT  Summary FROM Chapiter WHERE ChapterID= ?",(ChapterID,))
    return curseur.fetchone()

def read_caracter(caracterID):
    """
    fonction afficher  carater dans chapiter
    : parametre caracterID
    : return chapterID
    """
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("SELECT  ChapterID FROM IsInChapter WHERE CaracterID= ?",(caracterID,))
    return curseur.fetchall()

def every_caracter():
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("SELECT  CaracterID,FirstName,LastName FROM Caracter")
    return curseur.fetchall()

def afficher_dernier_paragraph():
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("SELECT Paragraph.ChapterID, User.Username, date, text,Summary FROM Paragraph JOIN User ON User.UserID = Paragraph.UserID JOIN Chapter ON Chapter.ChapterID = Paragraph.ChapterID  ORDER BY ParagraphID DESC LIMIT 1")
    last_paragraph = curseur.fetchone()
    return last_paragraph

def afficher_histoire():
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("SELECT Paragraph.ChapterID, Summary, text FROM Chapter JOIN Paragraph ON Chapter.ChapterID = Paragraph.ChapterID ORDER BY ParagraphID ")
    return curseur.fetchall()

def find_id_last_paragraph():
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("SELECT ParagraphID FROM Paragraph ORDER BY ParagraphID DESC LIMIT 1")
    return curseur.fetchone()

def find_id_last_chapter():
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("SELECT ChapterID FROM Chapter ORDER BY ChapterID DESC LIMIT 1")
    last_chapter = curseur.fetchone()
    return last_chapter[0]

def challenge_is_in_progress():
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("SELECT * FROM Challenge")
    if len(curseur.fetchall()) !=0:
        return True
    else:
        return False

def read_challenge():
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("SELECT  Username, Challenge.text FROM Challenge JOIN User ON User.UserID=Challenge.UserID")
    challenge = curseur.fetchone()
    return challenge

def find_user(UserID):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("SELECT Username FROM User WHERE UserID= ?",(UserID,))
    return curseur.fetchone()

def find_caracterID(FirstName):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("SELECT caracterID FROM caracter WHERE FirstName = ?",(FirstName,))
    return curseur.fetchone()

def nombre_vote():
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("SELECT  Vote FROM Challenge")
    vote = curseur.fetchone()
    return vote

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

def read_comment(chapterID):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("SELECT Username,date,text FROM Comment JOIN User ON User.UserID = Comment.UserID WHERE ChapterID = ?",(chapterID,))
    return curseur.fetchall()
#### Update ####

def change_pw(id, password):
    password = crypt(password)
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("UPDATE User SET Password = ? WHERE UserId = ?", (password, id))
    connexion.commit()
    connexion.close()

def update_summary(ChapterID, Summary):  #changer le résumé 
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("UPDATE Chapter SET Summary  = ? WHERE ChapterID = ?",(Summary,ChapterID ))
    connexion.commit()
    connexion.close()

def update_user(UserID,Username=None,password=None,):
    """
    function update chapter
    :parametre chapterID,summary
    :return Chapter
    """
    
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    if password is not None:
        password = crypt(password)
        curseur.execute("UPDATE User SET Password = ? WHERE UserId = ?", (password, UserID))
    if Username is not None:
        curseur.execute("UPDATE User SET Username = ? WHERE UserId = ?", (Username, UserID))
    connexion.commit()
    connexion.close()

def update_caracter(CaracterID,FirstName=None,LastName=None,Resume=None):
    """
    function update caracter
    :parametre CaracterID,FirstName=None,LastName=None,Resume=None
    :return Caracter
    """
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    if  FirstName is not None:
       curseur.execute("UPDATE Caracter SET FirstName = ? WHERE UserId = ?", (FirstName, CaracterID))
    if  LastName is not None:
       curseur.execute("UPDATE Caracter SET LastName = ? WHERE UserId = ?", (LastName, CaracterID))
    if  Resume is not None:
       curseur.execute("UPDATE Caracter SET Resume = ? WHERE UserId = ?", (LastName, CaracterID))
    connexion.commit()
    connexion.close()

def update_vote(vote):
    """
    function update challenge
    :parametre ParagraphID,Vote=None
    :return Challenge
    """
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("UPDATE Challenge SET Vote= ? ", (vote,))
   
    connexion.commit()
    connexion.close()

def update_chapter(chapterID,summary):
    """
    function update chapter
    :parametre chapterID,summary
    :return Chapter
    """
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("UPDATE Chapter SET Summary = ? WHERE ChapterID = ?", (summary, chapterID))
    connexion.commit()
    connexion.close()

def update_comment(commentID,text,userID):
    """
    function update comment
    :parametre chapterID,summary
    :return Chapter
    """
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("UPDATE Comment SET  Text= ? WHERE CommentID = ?", (text, commentID))
    curseur.execute("UPDATE Comment SET  Date = ?WHERE CommentID=?", (str(datetime.now()),commentID))
    curseur.execute("UPDATE Comment SET UserID=? WHERE CommentID=?", (userID, commentID))
    connexion.commit()
    connexion.close()



#### Delete ####

def delete_paragraph(ParagraphID):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("DELETE FROM Paragraph WHERE ParagraphID = ?; " , (ParagraphID,))
    connexion.commit()
    connexion.close()

def delete_challenge():
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("DELETE FROM Challenge")
    connexion.commit()
    connexion.close()

def fin_vote():
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("DROP TABLE Vote")
    connexion.commit()
    connexion.close()
