'''
Dbugging
1) --> set_tace() function execcute a program line by line.
important command in python debug --> n-c-l-q(next line, continue, line list, quit)
'''

import pdb as debug

debug.set_trace()  # it stops the exedution of program
name = input("Enter you name: ")
age = input("Enter your age: ")
debug.set_trace() 
print(f"Your name is: {name} and your age: {age}")
new_age = age + 5
print(f"The new age after 5 years: -->{new_age}")