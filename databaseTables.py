import sqlite3


def database():

    connection = sqlite3.connect("database.s3db")
    cursor = connection.cursor()


    cursor.executescript("""
        CREATE TABLE IF NOT EXISTS students (
            rowID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            studentNumber INTEGER NOT NULL,
            grade TEXT NOT NULL
        );
    """)

    connection.commit()
