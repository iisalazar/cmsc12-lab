#!/usr/bin/python3
import sys, os

def larger(num1, num2):
	if num1 > num2:
		return num1
	return num2

large = lambda x, y: x if x > y else y



if __name__ == '__main__':
	num1 = 3
	num2 = 4
	if len(sys.argv) > 1:
		try:
			num1 = int(sys.argv[1])
			num2 = int(sys.argv[2])
		except ValueError:
			pass

	num = larger(num1, num2)
	print('Larger: {}'.format(num))
	print("Using lambda function: {}".format(large(num1, num2)))

	os.system('clear')