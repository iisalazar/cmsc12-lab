#!/usr/bin/python3
from application.views import (CreateView, UpdateView, DeleteView, RetrieveView, ListView )
from application.custom_exceptions import UserExistsException, UserNotFoundException
import sys, time, os

def printMenu():
	_ = '''
(1) List All Students
(2) Get One Student
(3) Add New Entry
(4) Update An Entry (requires student no.)
(5) Delete An Entry (requires student no.)
(6) Exit
'''
	print(_)

def printEntries(data):
	print('| Student No. | First Name | Middle Name | Last Name | Age | Year |')
	for user in data:
		print('| {no} | {f} | {m} | {l} | {y} | {age}'.format(
			no = user.get('studentNo'),
			f = user.get('fName'),
			m = user.get('mName'),
			l = user.get('sName'),
			y = user.get('year'),
			age = user.get('age')
		), end=''
		)

def handleList():
	view = ListView()
	entries = view.get()
	printEntries(entries)
	input("Press enter to continue... ")
	os.system('clear')

def handleGet():
	
	view = RetrieveView()
	try:
		studentNo = input("Student no. : ")	
		entry = view.get(studentNo)
	except UserNotFoundException as e:
		print(e)
	else:
		printEntries([entry, ])
	input("Press enter to continue... ")
	os.system('clear')

def handleCreate():
	exists = True
	view = RetrieveView()
	while exists:
		try:
			studentNo = input("Student no: ")
			student = view.get_queryset(studentNo)
			if student is not None:
				raise UserExistsException("User with student number {} exists".format(studentNo))
		except UserExistsException as e:
			print(e)
			continue
		else:
			exists = False
	fName 	= input("First Name: ")
	mName 	= input("Middle Name: ")
	sName 	= input("Surname: ")
	age 	= input("Age: ")
	year 	= input("Year: ")
	createView = CreateView()
	createView.create({
			"studentNo" : studentNo,
			"fName" : fName,
			"mName" : mName,
			"sName" : sName,
			"age" : age,
			"year" : year
		})
	print("Creating... ")
	time.sleep(2)
	print("Created !!!")
	input("Press enter to continue... ")
	os.system('clear')	

def handleUpdate():
	exists = False
	view = RetrieveView()
	while not exists:
		try:
			studentNo = input("Student no: ")
			student = view.get_queryset(studentNo)
			if student is None:
				raise UserNotFoundException("User with student number {} does not exist".format(studentNo))
		except UserNotFoundException as e:
			print(e)
			continue
		else:
			exists = True
	fName 	= input("First Name: ")
	mName 	= input("Middle Name: ")
	sName 	= input("Surname: ")
	age 	= input("Age: ")
	year 	= input("Year: ")
	updateView = UpdateView()
	updateView.update({
			"studentNo" : studentNo,
			"fName" : fName,
			"mName" : mName,
			"sName" : sName,
			"age" : age,
			"year" : year
		})
	print("Updating... ")
	time.sleep(2)
	print("Updated !!!")
	input("Press enter to continue... ")
	os.system('clear')	

def handleDelete():
	exists = False
	view = RetrieveView()
	while not exists:
		try:
			studentNo = input("Student no: ")
			student = view.get_queryset(studentNo)
			if student is None:
				raise UserNotFoundException("User with student number {} does not exist".format(studentNo))
		except UserNotFoundException as e:
			print(e)
			continue
		else:
			exists = True
	delete = DeleteView()
	delete.delete(studentNo)
	print("Deleting... ")
	time.sleep(2)
	print("Deleted !!!")
	input("Press enter to continue... ")
	os.system('clear')		

if __name__ == '__main__':
	choice = 1
	while choice != 6:
		try:
			printMenu()
			choice = int(input("Choice [1-6]: "))
		except ValueError:
			print("Please input a number...")
			time.sleep(1.5)
			os.system('clear')
		else:
			if choice == 1:
				handleList()
			elif choice == 2:
				handleGet()
			elif choice == 3:
				handleCreate()
			elif choice == 4:
				handleUpdate()
			elif choice == 5:
				handleDelete()
			elif choice == 6:
				os.system('clear')
				continue
			else:
				print("Please input a number from 1 to 6")
				time.sleep(1.5)
				os.system('clear')
	print("Goodbye...")