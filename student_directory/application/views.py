import json
from .db import DB

from .custom_exceptions import UserNotFoundException, MissingFieldException, UserExistsException
class CreateView(DB):
    def __init__(self):
        super().__init__()
    
    def create(self, data):
        studentNo = data.get('studentNo')
        #checks if user exists
        user = self.get_queryset(studentNo)
        if user is not None:
            raise UserExistsException("User with student number {} exists".format(studentNo))
        data['age'] = str(data.get('age'))
        data = self.append(data)
        return data

class RetrieveView(DB):
    def __init__(self):
        super().__init__()

    def get(self, studentNo = None):
        if studentNo is None:
            raise MissingFieldException("Student no. is required")
        student = self.get_queryset(studentNo)
        if student is None:
            raise UserNotFoundException("User with student no. {} not found".format(studentNo))
        return student

class UpdateView(DB):
    def __init__(self):
        super().__init__()

    def update(self, data):
        studentNo = data.get('studentNo')
        #checks if user exists
        student = self.get_queryset(studentNo)
        if student is None:
            raise UserNotFoundException("Student with student number {} does not exist".format(studentNo))
        student['age'] = str(student['age'])
        for key, value in data.items():
            if key == 'age':
                value = value + '\n'
            student[key] = value
        self.writeOne(student)
        return data

class DeleteView(DB):
    def __init__(self):
        super().__init__()

    def delete(self, studentNo):
        if studentNo is None:
            raise MissingFieldException("Student no. is required")
        student = self.get_queryset(studentNo)
        if student is None:
            raise UserNotFoundException("User with student no. {} not found".format(studentNo))
        users  = self.read()
        for index, user in enumerate(users):
            if user.get('studentNo') == studentNo:
                indexToPop = index
                break
        del users[indexToPop]
        self.write(users)
        return student

class ListView(DB):
    def __init__(self):
        super().__init__()

    def get(self):
        return self.get_queryset()
