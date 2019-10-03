#!/usr/bin/python3
import sys, os, pprint
'''
Ian I. Salazar
2019-04060
CMSC 12 B-4L
A script that stores a student record using objects and lists
'''
# student record data
'''
sample record 
studentRecord = [
    {
        'student number': '2019-04060',           String
        'name': "Ian Salazar",                String
        'degree': "BS Computer Science",         String
        'year level': 1,                       Integer
        'age': 19                             Integer
    }
]
'''
studentRecords = [
    {
        'student number' : '2019-04060',
        'name' : 'Ian Salazar',
        'degree': 'BS Computer Science',
        'year level' : 1,
        'age' : 19
    },
    {
        'student number' : '2019-55555',
        'name' : 'Ivan Grey',
        'degree': 'BS Computer Science',
        'year level' : 1,
        'age' : 19
    },
]

def showMenu():
    print('''
[1] Add Student
[2] View a Student
[3] View all Students
[4] Delete a Student
[5] Delete all Students
[6] Exit
    ''')


'''
def checkIfStudentExist(studentNumber):
    for key, studentRecord in studentRecord.items():
        if studentRecord['student number'] == studentNumber:
            return True
    return False
'''
def getStudent(studentNumber):
    for student in studentRecords:
        if student['student number'] == studentNumber:
            return student
    return None

# a method that pushes to the global studentRecord list
def addStudent():
    os.system('clear')
    global studentRecords
    record = {
        'student number' : '',
        'name' : '',
        'degree' : '',
        'year level' : 0,
        'age' : 0
    }
    for key, value in record.items():
        while True:
            value = input("Input your {}: ".format(key))
            if key == 'student number':
                student = getStudent(value)
                if student is not None:
                    print("Error! Student with student # {} already exists".format(value))
                    continue
                else:
                    break
            else:
                break
        if key == 'year level' or key == 'age':
            value = int(value)
        record[key] = value
    studentRecords.append(record)


            
# a method to view either a single student or all students
def viewStudent(studentNumber = None):
    # this if block is executed when no student number is passed to this function
    if studentNumber is None:
        records = []
        # checks if there are no records
        if len(studentRecords) == 0:
            print("No records yet...")
            return
        # loops through all the records
        for student in studentRecords:
            studentRecord = []
            # loops through all the record entry of a student 
            for key, value in student.items():
                studentRecord.append('{} - {}'.format(key, value)) # pushes them to the list
            # converts the records to a string
            records.append('\n'.join(studentRecord))
        # converts all records to a string
        print('\n'.join(records))
        return
    
    student = getStudent(studentNumber) # gets a single student
    # checks if the returned value is None -> student does not exist
    if student is None:
        print ("Error! Student with student # {} does not exist".format(studentNumber))
        return
    for key, value in student.items():
        print('{} - {}'.format(key, value))
        

def askStudentNumber():
    studNumber = input("Your student number: ")
    return studNumber

def deleteStudent(studentNumber = None):
    global studentRecords
    if studentNumber is None:
        print("Deleting all students...")
        studentRecords = {}
        return
    
    student = getStudent(studentNumber)
    if student is None:
        print ("Error! Student with student # {} does not exist".format(studentNumber))
        return
    
    studentRecordsCopy = []
    studentRecordsCopy.extend(studentRecords)
    for stud in studentRecordsCopy:
        if stud['student number'] == student['student number']:
            studentRecordsCopy.remove(stud)
            print('Deleted in record!! {}'.format(student['student number']))
            break
    studentRecords = studentRecordsCopy
    return

if __name__ == '__main__':
    while True:
        showMenu()
        choice = int(input("Menu: "))
        if choice == 6:
            print("Thank you for using me...")
            break
        elif choice == 1:
            addStudent()
        elif choice == 2:
            studNumber = askStudentNumber()
            viewStudent(studNumber)
        elif choice == 3:
            viewStudent()
        elif choice == 4: # deletes a single student
            studNumber = askStudentNumber()
            deleteStudent(studNumber)
        elif choice == 5:
            deleteStudent() # deletes all students