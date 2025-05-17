import sqlite3

connection = sqlite3.connect("database.s3db")
cursor = connection.cursor()

def addStudent():
    while True:
        choice = input("Add students? [y or n]: ").lower()

        if choice == "y":
            addName = input("Enter student's name: ")
            addStudentNumber = int(input("Enter student's student number: "))
            addGrade = round(float(input("Enter student's grade: ")), 2)

            cursor.execute("insert into students(name, studentNumber, grade) values(?, ?, ?)", (addName, addStudentNumber, addGrade))
            connection.commit()

        elif choice == "n":
            break
            quit()
        else:
            print("Please type only y or n!")

    connection.close()
