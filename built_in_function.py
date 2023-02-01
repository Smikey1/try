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

'''
Iterable vs iterator
'''

num_list = [1,2,3,4]  # iterable 

# an iter() function can only be called in iterable which converts iterable into iterator
# so that next() function can be run in iterator

# how looping works: --> loop gara --> yo list lai iterate gara na
for i in num_list:
    print(i)

def mero_aafnai_loop():
    converted_iterator = iter(num_list)
    print(next(converted_iterator))
    print(next(converted_iterator))
    print(next(converted_iterator))
    print(next(converted_iterator))

mero_aafnai_loop()


"""
Advance Filter Function

#1: return the list of even num from the:
    --> normaly way coding
    --> list comprehension way
    --> def normal function way
    --> lambda function way
    --> map function way
"""

def filter_even(l1):
    even_list = []
    for element in l1:
        if element %2 ==0:
            even_list.append(element)
    return even_list

def even_fun(l1):
    return l1 %2 == 0

def even_list(l1):
    return [ i for i in l1 if i % 2==0]

print(filter(even_fun,num_list)) # filter object
print(tuple(filter(even_fun,num_list)))  # filter object converted into tuple

print(tuple(filter(lambda a: a%2==0,num_list)))  # filter object converted into tuple


'''
Zip function  --> converted to pair
must have equal length
'''
big_char = ["A","B","C","D"]
small_char = ["a","b","c","d"]

print(zip(small_char,big_char))
zipped_value = list(zip(small_char,big_char))
print(list(zip(small_char,big_char)))
print(tuple(zip(small_char,big_char)))


# for zip unpacking
item1,item2 = zip(*zipped_value)
print(f"The item1 is: -->{item1}")
print(f"The item2 is: -->{item2}")

#Que:
'''
1) Ask a num with user: loop till that num --> filter odd and even and store in different list --> zip it -->
and add max value into new list from the pairs of tuples --> and return that new list

2) 
def a fun which take a many numerical list: FYI (lambda fun)
given l1 = [1,2,3],[4,5,6],[7,8,9]
such as l1  --> return the avg of: (1+4+7)/3, (2+5+8)/3 ... SO ON
'''
avg_calculator = lambda *args: [sum(pair)//len(pair) for pair in zip(*args)]
print(avg_calculator([1,2,3],[4,5,6],[7,8,9]))

'''
Any and All function  --> converted to pair
'''

num_list1= [2,4,6,8,10]
num_list12=[1,3,5,7,9]

my_list = [True,False,True]

print(all(my_list))  #Ouput --> boolean {True}

print(any(my_list))  #Ouput --> boolean {True}

def check_even(any_list):
    even_list =[]
    for i in any_list:
        even_list.append(i%2==0)
    return even_list

print(check_even(num_list1))

print(all([i%2==0 for i in num_list1]))


# Practice of all and any (Level: Difficult)
def sum(*args):
    if(all( [(type(element)==int or type(element)==float) for element in args])):
        total_sum =0
        for i in args:
            total_sum += i
        return total_sum
    else:
        return "Int or float are only"

print(sum(1,2,3.5,4.5))