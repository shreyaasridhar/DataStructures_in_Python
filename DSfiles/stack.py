#!/usr/bin/env python3 
class Stack:
	def __init__(self):
		self.elements = []

	def isEmpty(self):
		return self.elements == []

	def push(self, val : int):
		return self.elements.insert(0, val)

	def pop(self):
		return self.elements.pop(0)

	def peek(self):
		return self.elements

	def size(self):
		return len(self.elements)
