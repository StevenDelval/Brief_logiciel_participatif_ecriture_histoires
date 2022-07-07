import sqlite3 
import hashlib

from datetime import datetime

def crypt(password):
    """
    Fonction qui crypte un mot de passe
    :param password (str): mot de passe
    :return (str) le hash du mot de passe
    """
    hash_pwd = hashlib.new('sha256')
    hash_pwd.update(password.encode())
    hash_pwd = hash_pwd.hexdigest()
    return hash_pwd

#### Create ####
def create_user(username, password):
    password = crypt(password)
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


def create_chapter(Summary_TEXT):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("INSERT INTO Chapter VALUES (?,?);", (None, Summary_TEXT))
    connexion.commit()
    connexion.close()

def create_comment(text,ChapterID,UserID):
    """
    fonction create_comment
    :parametre text,ChapterID,UserID
    :return bdd.Comment
    """

    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("""INSERT INTO Comment VALUES (?,?,?,?,?)""",(None,ChapterID,UserID,str(datetime.now()),text ) )
    connexion.commit()
    connexion.close()


def create_caracter(first_name, last_name, resume):
    """
    fonction create caracter
    :parametre first_name last_name,resume
    :return base de donnee bdd.db
    """
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("INSERT INTO Caracter VALUES (?,?,?,?);", (None, first_name, last_name, resume ))
    connexion.commit()
    connexion.close()

def create_isinchapter(caracterID,chapterID):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("INSERT INTO IsInChapter VALUES (?,?);", (caracterID,chapterID))
    connexion.commit()
    connexion.close()

def start_challenge(UserId,ParagraphID,commentaire):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("INSERT INTO Challenge VALUES (?,?,?,?)",(UserId,ParagraphID,commentaire,1))
    connexion.commit()
    connexion.close()

def liste_votant():
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
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("INSERT INTO Vote VALUES (?)",(userID,))
    connexion.commit()
    connexion.close()
#### Read   ####
def a_voter(userID):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("SELECT UserID FROM Vote WHERE UserID=?",(userID,))
    if len(curseur.fetchall()) == 0:
        return False
    else :
        return True

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
    return last_chapter

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
def nombre_vote():
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("SELECT  Vote FROM Challenge")
    vote = curseur.fetchone()
    return vote

def read_chapter(chapterID):
    """
    fonction afficher le sommaire de la chapiter
    :parametre chapiterID
    :return summary
    """
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("SELECT Summary FROM Chapter WHERE ChapterID =?",(chapterID,))
    return curseur.fetchone()

def read_personnage(chapterID):
    """
    fonction afficher les personnages d'un chapitre
    :parametre chapterID
    :return liste des personnages
    """
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("""SELECT Caracter.FirstName,Caracter.LastName
    FROM  Caracter
    JOIN Caracter ON Caracter.CaracterID=IsInChapiter.CaracterID 
    WHERE ChapterID =?
    """,(chapterID,))
    return curseur.fetchall()

def read_comment(chapterID):
    """
    fonction afficher le commentaire du chapter
    :parametre chapterID
    :return comment
    """
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute(""" SELECT Comment.text FORM Comment,WHERE ChapterID=""",(chapterID,))

def read_date_comment(chapterID):
    """
    fonction afficher la date du commentaire
    :parametre chapterID
    :return date
    """
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute(""" SELECT Comment.date FORM Comment,WHERE ChapterID=""",(chapterID,))


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
