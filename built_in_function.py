"""
# Enumerate function
--> it is mainly used with loop to track the position of items
"""

list_of_fruit = ["apple","banana","orange","kiwi","papaya"]

position1 = 0
for fruit in list_of_fruit:
    print(f"The fruit name is: {fruit} is at position1: {position1}")
    position1 += 1


for position,fruit in enumerate(list_of_fruit):
    print(f"The fruit name is: {fruit} is at position: {position}")


'''
# ask a fruit name with user --> case in-sensitive
if that fruit exist in list_of_fruit then return its position else
return message -->"Fruit not found"

FIY: enumerate function
'''


"""
Map function
--> you can only loop once in map map object
--> it is a iterator
"""

'''
without lambda function

num_list = [1,2,3,4]

def square_function(num):
    return num**2

def cube_function(num):
    return num**3

def any_function(mero_function):
    return tuple(map(mero_function,num_list))

idk_k_dinxa = any_function(cube_function)

for i in idk_k_dinxa:
    print(f"value --> {i}")
'''

"""
With Lambda Function:
"""
num_list = [1,2,3,4]

idk_k_dinxa = tuple(map(lambda a: a**2,num_list))

for i in idk_k_dinxa:
    print(f"value --> {i}")