#!/usr/bin/python3

import sys, time

def factorial(x):
	buff = x
	while x > 1:
		print(buff, x)
		buff *= x - 1
		x -= 1
		print(buff)
		time.sleep(1)
	return buff


print( factorial( int(sys.argv[1])) )