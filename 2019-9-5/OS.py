#!/usr/bin/python3

import os, sys, time

class Calculator(object):

	def add(self, x, y):
		return x + y

	def minus(self, x, y):
		return x - y

	def mult(self, x, y):
		return x * y

	def div(self, x, y):
		return x / y

	def modulo(self, x, y):
		return x % y

	def exponent(self, x, y):
		return x ** y

	def factorial(self, x):
		buff = 0
		while x >= 1:
			buff = x * x-1
			x -= 1
		return buff


class Menu(object):
	self.menu = '''
[1] Addition
[2] Subtraction
[3] Multiplication
[4] Division
[5] Modulo
[6] Exponential
[7] Factorial
[8] Exit
'''

	def __repr__(self):
		return self.menu

if __name__ == '__main__':
	calculator = Calculator()
	menu = Menu()
	while True:
		menu
		time.sleep(3)
