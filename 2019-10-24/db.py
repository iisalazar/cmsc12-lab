import json
class DB(object):
    def __init__(self, fileName=None):
        if fileName is None:
            self.fileName = 'users.json'
        else:
            self.fileName = fileName

    def get_queryset(self, studentNo = None):
        users = self.read()
        if studentNo is None:
            return users
        for user in users['users']:
            if user.get('studentNo') == studentNo:
                return user
        return None

    def read(self):
        with open(self.fileName, 'r') as f:
            users = json.loads(f.read())
        return users

    def write(self, users):
        with open(self.fileName, 'w') as f:
            json.dump(users, f)
        return users

    def writeOne(self, user):
        data = self.read()
        for index, student in enumerate(data.get('users')):
            if student.get('studentNo') == user.get('studentNo'):
                indexToUpdate = index
                break
        data['users'][indexToUpdate] = user
        self.write(data)