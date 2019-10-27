import json
from .helpers import convert_users_to_list, convert_obj_to_string

class DB(object):
    def __init__(self, fileName=None):
        if fileName is None:
            self.fileName = 'database'
        else:
            self.fileName = fileName

    def get_queryset(self, studentNo = None):
        users = self.read()
        if studentNo is None:
            return users
        for user in users:
            if user.get('studentNo') == studentNo:
                return user
        return None

    def read(self):
        with open(self.fileName, 'r') as f:
            users = f.readlines()
        modifiedList = []
        for user in users:
            userData = user.split(',')
            data = {
                "studentNo": userData[0],
                "fName" : userData[1],
                "mName" : userData[2],
                "sName": userData[3],
                "year" : userData[4],
                "age" : userData[5]
            }
            modifiedList.append(data)
        return modifiedList

    def append(self, user):
        user = convert_obj_to_string(user)
        with open(self.fileName, 'a') as f:
            f.write(user)
            f.write('\n')
        return user

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
        print(users)
        self.write(users)

if __name__ == '__main__':
    db = DB()
    print(db.read())


