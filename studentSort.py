import sqlite3
from myAlgorithms import quickSort

connection = sqlite3.connect("database.s3db")
cursor = connection.cursor()

# this returns a tuple like: 
# ((1, "Roa, Alexus Enzo C.", 2022305494, 1.0), (2, "Smith, John T.", 2020400399, 3.00), ...)
# so we can basically access each student using indexing
# if we want to access the first student, we can say: row[0]

row = cursor.execute("select * from students").fetchall()

# we then typecast that tuple into a list so that we can manipulate the contents
studentRows = list(row)

# the quickSort algorithm that was written in the quickSort.py file
# was modified in a way so that we can sort each students according to a particular
# information associated to them. So we can arrange the studentRows list
# alphabetically, numberically using their studentNumber or grade.

# print(quickSort(studentRows, key = lambda student: student[3]))

sortedStudentRowsName = quickSort(studentRows, key = lambda student: student[1].lower())
sortedStudentRowsStudentNumber = quickSort(studentRows, key = lambda student: student[2])
sortedStudentRowsGrade = quickSort(studentRows, key = lambda student: student[3])

def showSortedStudents(accordingTo):
    for individualStudent in accordingTo:
        print(f"Student's name: {individualStudent[1]}")
        print(f"Student number: {individualStudent[2]}")
        print(f"Student's grade: {individualStudent[3]}\n")

def studentSort():
    while True:
        print("""
        Do you want to view students according to:

        Name? (Type "1")
        Student number? (Type "2")
        Grade? (Type "3")

        Type "0" if you want to quit.
        """)

        choice = input("Please choose: ")
        print("\n")
        if choice == "1":
            showSortedStudents(sortedStudentRowsName)
        elif choice == "2":
            showSortedStudents(sortedStudentRowsStudentNumber)
        elif choice == "3":
            showSortedStudents(sortedStudentRowsGrade)
        elif choice == "0":
            break
            quit()
        else:
            print("Please choose properly!")

