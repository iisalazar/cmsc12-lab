#!/usr/bin/python3
'''
Ian I. Salazar
2019-04060
CMSC 12 B-4L
A student directory app that (should) follow the MVC approach..
This still needs refactoring, but I think the documentation is comprehensive :) 
'''

# imports all the views
from application.views import (CreateView, UpdateView, DeleteView, RetrieveView, ListView )
# import all custom exceptions
from application.custom_exceptions import UserExistsException, UserNotFoundException
import sys, time, os


# a function to handle in printing the menu
def printMenu():
	_ = '''
(1) List All Students
(2) Get One Student
(3) Add New Entry
(4) Update An Entry (requires student no.)
(5) Delete An Entry (requires student no.)
(6) Delete All Entries ( YOU SURE? )
(7) Exit
'''
	print(_)

# a function that prints all entries that the user wants to see
def printEntries(data):
	print('| Student No. | First Name | Middle Name | Last Name | Year | Age | Degree |')
	for user in data:
		print('| {no} | {f} | {m} | {l} | {y} | {age} | {degree}'.format(
			no = user.get('studentNo'),
			f = user.get('fName'),
			m = user.get('mName'),
			l = user.get('sName'),
			y = user.get('year'),
			age = user.get('age'),
			degree = user.get('degree')
		), end=''
		)

# a function that utilizes the ListView class
# prints the list of users
def handleList():
	view = ListView() # instantiate view
	entries = view.get() # get all entries
	printEntries(entries) # print all entries using printEntries function from line 23
	input("Press enter to continue... ")
	os.system('clear')

# a function that utilizes the GetView class
# prints a single user
def handleGet():	
	view = RetrieveView() #instantiate the view
	try:
		studentNo = input("Student no. : ")	
		entry = view.get(studentNo) # gets the student
	except UserNotFoundException as e:
		print(e) # prints "User with student no {studentNo} does not exist"
	else: # if the user does exist, print it
		printEntries([entry, ])
	input("Press enter to continue... ")
	os.system('clear')


# a function that utilizes the CreateView class
# asks the user information about the new entry
def handleCreate():
	exists = True
	view = RetrieveView()
	'''
		a loop that continues to execute if the student no. given
		by the user exists
	'''
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
	# the function continues when the student no. is not taken
	fName 	= input("First Name: ")
	mName 	= input("Middle Name: ")
	sName 	= input("Surname: ")
	age 	= input("Age: ")
	year 	= input("Year: ")
	degree 	= input("Degree / Course: ")
	# the input statements above asks for the firstname, 
	# middle name, last name, age and year

	createView = CreateView() # instantiate viewObject
	# now, add the new entry
	createView.create({
			"studentNo" : studentNo,
			"fName" : fName,
			"mName" : mName,
			"sName" : sName,
			"age" : age,
			"year" : year,
			"degree" : degree
		})
	# for GUI purposes
	# if you want your app to optimze, remove time.sleep()
	print("Creating... ")
	time.sleep(2)
	print("Created !!!")
	input("Press enter to continue... ")
	os.system('clear')	

# a function that utilizes the UpdateView class
# Updates a user's information
def handleUpdate():
	exists = False
	view = RetrieveView()
	# a loop that runs only if the student no. given by the user
	# does not exist in the database
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
	# if the student no. is taken, ask for the information to change
	fName 	= input("First Name: ")
	mName 	= input("Middle Name: ")
	sName 	= input("Surname: ")
	age 	= input("Age: ")
	year 	= input("Year: ")
	degree 	= input("Degree / Course: ")
	updateView = UpdateView() # instantiate the view
	# update the entry
	updateView.update({
			"studentNo" : studentNo,
			"fName" : fName,
			"mName" : mName,
			"sName" : sName,
			"age" : age,
			"year" : year,
			"degree" : degree
		})
	# for GUI purposes
	# if you want your app to optimze, remove time.sleep()
	print("Updating... ")
	time.sleep(2)
	print("Updated !!!")
	input("Press enter to continue... ")
	os.system('clear')	

def handleDelete():
	exists = False
	view = RetrieveView()
	# a loop that runs only if the student no. given by the user
	# does not exist in the database
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
	delete.delete(studentNo) # delete the entry
	# for GUI purposes
	# if you want your app to optimze, remove time.sleep()
	print("Deleting... ")
	time.sleep(2)
	print("Deleted !!!")
	input("Press enter to continue... ")
	os.system('clear')		

def handleClearDB():
	view = DeleteView()
	view.delete()
	print("Deleting all entries... ")
	time.sleep(2)
	print("Deleted !!!")
	input("Press enter to continue... ")
	os.system('clear')			

if __name__ == '__main__':
	choice = 1
	while choice != 7:
		try:
			printMenu() # prints the menu
			choice = int(input("Choice [1-6]: "))
		except ValueError: # catches if the input is not a number
			print("Please input a number...") 
			time.sleep(1.5)
			os.system('clear')
		else:
			# handles the choice
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
				handleClearDB()
			elif choice == 7:
				os.system('clear')
				continue
			else:
				print("Please input a number from 1 to 6")
				time.sleep(1.5)
				os.system('clear')
	print("Goodbye...")