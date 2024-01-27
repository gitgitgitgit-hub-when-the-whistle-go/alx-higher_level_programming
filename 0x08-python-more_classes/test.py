#!/usr/bin/python3

class User:

	salary = 1000
	def __init__(self, id):
		self.id = 10

	def not_class_but_called_as_one(self):
		print("able to call it even without initiating instance")
		# no surprise it didn't work xD
		# User.not...

