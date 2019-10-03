#!/usr/bin/python3

def f():
	global x
	x += 2
	y = 7
	print("x in f(x),", x)
	
	# return x

x = 3
f()
print("global x", x)


