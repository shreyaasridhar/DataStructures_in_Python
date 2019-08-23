#!/usr/bin/env python3
from DSfiles.stack import Stack

def revstring(mystr : str):
	newstr = Stack()
	for i in mystr:
		newstr.push(i)
	res = [i for i in newstr.peek()]
	return "".join(res)
print(revstring('apple') == 'elppa')
print(revstring('x') == 'x')
print(revstring('1234567890') == '0987654321')