# Tuples
'''

ordered collection of item can store any type of data like list
they are immutable means once created , cant be update
no any method like --> pop, append, insert remove...
it is super duper faster than list

It allows--> count() and index(), len(), min(), max() and slicing function
it is represented as ()
'''

days_tuple = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday')

print(len(days_tuple))
print(days_tuple.count("Tuesday"))
print(days_tuple.index("Wednesday"))
print(days_tuple[2])
print(days_tuple[1:5])

print(type(str(days_tuple)))
"('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday')"

# whenever func return two value, it will return in tuple
def fun1():
    return 2,3

print(type(fun1()))
# (2,3)
#(2)

a,b = fun1()
print(a)
print(type(a))
print("-------------------")

c,d = (6,7)  # tuple un-packing in python  --> (In JS: object de-structuring)
print(c)