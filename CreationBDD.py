import sqlite3
from datetime import datetime
connexion = sqlite3.connect('bdd.db')
curseur = connexion.cursor()

curseur.execute('''CREATE TABLE User
               (
                    UserID INTEGER PRIMARY KEY,
                    Username TEXT UNIQUE,
                    Password TEXT
                )
''')
curseur.execute("INSERT INTO User VALUES (0,?,?);", ("welcom", "565"))

curseur.execute('''CREATE TABLE Chapter
               (
                    ChapterID INTEGER PRIMARY KEY,
                    Summary TEXT
                )
''')

curseur.execute('''CREATE TABLE Paragraph
               (
                    ParagraphID INTEGER PRIMARY KEY,
                    ChapterID INTEGER,
                    UserID INTEGER,
                    date TEXT,
                    text TEXT,
                    FOREIGN KEY(UserID)
                        REFERENCES User(UserID),
                    FOREIGN KEY(ChapterID)
                        REFERENCES Chapter(ChapterID)
                )
''')


curseur.execute('''CREATE TABLE Comment
               (
                    CommentID INTEGER PRIMARY KEY,
                    ChapterID INTEGER,
                    UserID INTEGER,
                    date TEXT,
                    text TEXT,
                    FOREIGN KEY(UserID)
                        REFERENCES User(UserID),
                    FOREIGN KEY(ChapterID)
                        REFERENCES Chapter(ChapterID)
                )
''')

curseur.execute('''CREATE TABLE Challenge
                (
                    UserID INTEGER,
                    ParagraphID INTEGER,
                    Text TEXT,
                    Vote INTEGER,
                    date TEXT, 
                    FOREIGN KEY(UserID)
                        REFERENCES User(UserID),
                    FOREIGN KEY(ParagraphID)
                        REFERENCES Paragraph(ParagraphID)
                )
''')

curseur.execute('''CREATE TABLE Caracter
                (
                    CaracterID INTEGER PRIMARY KEY,
                    FirstName TEXT,
                    LastName TEXT,
                    Resume TEXT
                )
''')

curseur.execute('''CREATE TABLE IsInChapter
                (
                    CaracterID INTEGER,
                    ChapterID INTEGER,
                    FOREIGN KEY(ChapterID)
                        REFERENCES Chapter(ChapterID),
                    FOREIGN KEY(CaracterID)
                        REFERENCES Caracter(CaracterID)
                )
''')

curseur.execute("INSERT INTO Paragraph VALUES (0,?,?,?,?);", ( 0, 0, str(datetime.now()),"Hello"))
curseur.execute("INSERT INTO Chapter VALUES (?,?);", (0, "Hello"))
curseur.execute("INSERT INTO Chapter VALUES (?,?);", (1, "En cour"))
connexion.commit()
connexion.close