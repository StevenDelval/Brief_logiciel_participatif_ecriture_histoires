import sqlite3

connexion = sqlite3.connect('bdd.db')
curseur = connexion.cursor()

curseur.execute('''CREATE TABLE User
               (
                    UserID INTEGER PRIMARY KEY,
                    Username TEXT UNIQUE,
                    Password TEXT
                )
''')

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
                    FOREIGN KEY(UserID)
                        REFERENCES User(UserID),
                    FOREIGN KEY(ParagraphID)
                        REFERENCES Paragraph(ParagraphID)
                )
''')

curseur.execute('''CREATE TABLE Caracter
                (
                    CaracterID INTEGER PRIMARY KEY,
                    FistName TEXT,
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


connexion.commit()
connexion.close