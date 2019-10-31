# A module that handles reading and writing to the database

import json
# imports the helpers to convert each entry of dictionary to a string
# of record
from .helpers import (convert_users_to_list, convert_obj_to_string,
                        convert_string_to_obj, convert_strings_to_obj
                    )

class DB(object):
    # sets the filename of the database
    # defaults to 'database' when nothing is provided
    def __init__(self, fileName=None):
        if fileName is None:
            self.fileName = 'database'
        else:
            self.fileName = fileName


    # a queryset method
    # returns the query
    # can pass in none, returns by default a list of all students
    def get_queryset(self, studentNo = None):
        users = self.read()
        if studentNo is None:
            return users
        for user in users:
            if user.get('studentNo') == studentNo:
                return user
        return None


    # a method that reads the entire file / database
    # returns a list of dictionaries containg all entries
    # from the database
    def read(self):
        with open(self.fileName, 'r') as f:
            users = f.readlines()
        modifiedList = convert_strings_to_obj(users)
        return modifiedList

    # a method that appends at the end of the database
    # I seperated this because append is different from write
    def append(self, user):
        user = convert_obj_to_string(user)
        with open(self.fileName, 'a') as f:
            f.write(user)
            f.write('\n')
        return user

    # a method that re-writes the entire database
    # this method should be used only when updating or deleting an entry
    def write(self, users):
        users = convert_users_to_list(users)
        with open(self.fileName, 'w') as f:
            f.writelines(users)
        return users

    def writeOne(self, user):
        users = self.read()
        for index, student in enumerate(users):
            if student.get('studentNo') == user.get('studentNo'):
                indexToUpdate = index
                break
        print("Calling from update")
        users[indexToUpdate] = user
        self.write(users)

    # a method to clear the entire database
    def clearDB(self):
        self.write([])

if __name__ == '__main__':
    db = DB()
    print(db.read())


