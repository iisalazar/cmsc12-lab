#!/usr/bin/python3
'''
Ian I. Salazar
2019-04060
Calculator Problem
September 5, 2019
CMSC12 B-4L
'''
import os, sys, time

class Calculate(object):
	def add(self, Xs):
		return sum(Xs)

	def minus(self, Xs):
		diff = Xs.pop(0)
		for x in Xs:
			diff -= x
		return diff

	def mult(self, Xs):
		prod = Xs.pop(0)
		for x in Xs:
			prod *= x
		return prod

	def div(self, Xs):
		quo = Xs.pop(0)
		for x in Xs:
			quo *= x
		return quo

	def modulo(self, x, y):
		return x % y

	def exponent(self, x, y):
		return x ** y

	def factorial(self, x):
		buff = x
		while x > 1:
			buff *= x - 1
			x -= 1
		return buff
'''
5
5 * 4 * 3 * 2 * 1
'''

menu = '''
[1] Addition
[2] Subtraction
[3] Multiplication
[4] Division
[5] Modulo
[6] Exponential
[7] Factorial
[8] Exit
'''


if __name__ == '__main__':
	use = True
	calculate = Calculate()
	while use:
		print(menu)
		choice = int(input("Enter option: "))
		if choice > 8 or choice < 1:
			print("The number you entered is not in the options.")
			continue
		if choice == 8:
			os.system('clear')
			print("Thank you.")
			use = False
			continue
		if choice >= 1 and choice < 7:
			xs = input("Enter x: ")

			XS = [ int(x) for x in xs.split(' ')] 
			if choice == 1:
				print( calculate.add(XS))
			elif choice == 2:
				print( calculate.minus(XS) )
			elif choice == 3:
				print( calculate.mult(XS) )
			elif choice == 4:
				print( calculate.div(XS) )
			elif choice == 5:
				y = input("Enter y: ")
				print( calculate.modulo(int(xs), int(y)) )
			elif choice == 6:
				y = input("Enter y: ")
				print( calculate.exponent(float(xs), float(y)) )
			continue
		# since options 1 through 6 and 8 are caught by the statements above
		# the only remaining option is 7, which is a factorial
		x = int(input("Enter your x: "))
		print( calculate.factorial(x) )
