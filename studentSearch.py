import sqlite3
from myAlgorithms import quickSort, binarySearch

# this script is used to search for a particular student using their name or account number

connection = sqlite3.connect("database.s3db")
cursor = connection.cursor()

row = cursor.execute("select * from students").fetchall()

studentRows = list(row)

sortedStudentRowsName = quickSort(studentRows, key = lambda student: student[1].lower())
sortedStudentRowsStudentNumber = quickSort(studentRows, key = lambda student: student[2])

def searchName():
    print("When searching a name, follow the format:\nSurname, FirstName MiddleInitial (if it exists)")
    name = input("Please enter student's name (Please capitalize properly and full name is required): ")

    result = binarySearch(sortedStudentRowsName, name, key = lambda student: student[1])

    print(f"\nStudent's name: {result[1]}")
    print(f"Student number: {result[2]}")
    print(f"Student's grade: {result[3]}")

def searchStudentNumber():
    studentNumber = int(input("Please enter student's student number: "))

    result = binarySearch(sortedStudentRowsStudentNumber, studentNumber, key = lambda student: student[2])

    print(f"\nStudent's name: {result[1]}")
    print(f"Student number: {result[2]}")
    print(f"Student's grade: {result[3]}")

def studentSearch():
    while True:
        print("""
Do you want to search a student using their:

Name? (Type "1")
Student number? (Type "2")

Type "0" if you want to quit.
        """)
        choice = input("Please choose: ")
        print("\n")

        if choice == "1":
            try:
                searchName()
            except TypeError:
                print("\nA student with that name doesn't exist.")
            except:
                print("\nAn unexpected error occured. Please try again.")
        elif choice == "2":
            try:
                searchStudentNumber()
            except TypeError:
                print("\nA student with that student number doesn't exist.")
            except:
                print("\nAn unexpected error occured. Please try again.")
        elif choice == "0":
            break
            quit()
        else:
            print("Please choose properly!")
