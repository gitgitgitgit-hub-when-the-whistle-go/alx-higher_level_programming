#!/usr/bin/python3

Student = __import__('10-student').Student
std = Student(1,2,3)
le_json = std.to_json(["first_name"])
print(le_json)
