#!/usr/bin/python3
from application.views import (CreateView, UpdateView, DeleteView, RetrieveView, ListView )
import time
class TestCreate(CreateView):
	def __init__(self, userObj = None):
		self.data = userObj
		super().__init__()

	def run(self):
		user = self.create(self.data)
		return user

class TestUpdate(UpdateView):
	def __init__(self, userObj = None):
		self.data = userObj
		super().__init__()

	def run(self):
		user = self.update(self.data)
		return user	

class TestDelete(DeleteView):
	def __init__(self, userObj = None):
		self.data = userObj
		super().__init__()

	def run(self):
		user = self.delete(self.data.get('studentNo'))
		return user	


if __name__ == '__main__':
	userObj = {
        "studentNo" : "2019-00000",
        "year" : 1,
        "fName" : "Isabela Anne",
        "mName" : "Ventura",
        "sName" : "Magtira",
        "age" : 21,
        "degree": "BS Industrial Engineering"
	}
	# test create view
	testCreate = TestCreate(userObj)
	res = testCreate.run()
	time.sleep(5)
	# Test Update View
	'''
	userObj["fName"] = "Not Ian"
	userObj["mName"] = "Not Ilapan"
	userObj["sName"] = "Not Salazar"

	testUpdate = TestUpdate(userObj)
	res = testUpdate.run()
	print(res)

	time.sleep(5)
	
	# test delete view
	testDelete = TestDelete(userObj)
	res = testDelete.run()
	print(res)
	time.sleep(5)
	'''