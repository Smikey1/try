'''
Closure, Decorator and Generator in python
--> It make python unique. 
--> They are consider as first class citizen/function in programming
'''
def squareMM(num):
    return num**2

s= squareMM # we are not calling fun, but we are referecening sq. function
# here, s became a function, which holds the square func.

print(s(8))
print(s.__name__)
print(squareMM.__name__)

#1 pass fuc as a argument
# --> for example: map function

# function inside function

my_list=[1,2,3,4]

print(list(map(lambda a:a**2,my_list)))

def my_map(func,list):
    num_list = []
    for i in list:
        num_list.append(func(i))
    return num_list

def cube(num):
    return num**3

print(list(my_map(cube,my_list)))

#2 function return function:

def out_func():
    def in_func():
        print("Hello I am")
    return in_func

my_var = out_func()
my_var() # calling second function

def out_func1(value1):
    def in_func1(value2):
        print(f"The Hello:{value1} and ok:{value2}")
    return in_func1

out_return = out_func1("Apple")
out_return("Ball")   # calling second function

# Practice Que:
def power_off(num):
    def cal_power(n):
        return num **n
    return cal_power

to_power = power_off(5)
print(to_power(2))


"""
Decorator in Python

"""

def decorator_funcion(any_fun):
    def wrapper_func():
        print("this is wrapper func")
        any_fun()  # fun2 execute here
    return wrapper_func

def fun1():
    print("function --->1")

# @ is considered as syntatic sugar --> used for decorator
@decorator_funcion
def fun2():
    print("function --> 2")


fun1()
fun2()

'''
working of fun2
new_fun = decorator_funcion(fun2)
new_func()
'''