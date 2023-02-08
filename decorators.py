'''
Decorator:
It enhance the functionality of other function
'''

def my_decorator_func(any_func):
    # @wraps(any_func)
    def wrapper_func(*args,**kwargs):
        ''' This is wrapper function'''
        print("This is extra function")
        return any_func(*args,**kwargs)
    return wrapper_func


@my_decorator_func
def add(a,b):
    ''' this is a add function '''
    return a+b

add(2,3)
print(add(2,3))
print(add.__name__)

def sarthak():
    pass

def my_decorator_func1(any_func):
    def wrapper_func(*args,**kwargs):
        print("This is extra function")
        return any_func(*args,**kwargs)
    return wrapper_func


def my_decorator_func2(any_func):
    def wrapper_func(*args,**kwargs):
        print("This is red apple")
        return any_func(*args,**kwargs)
    return wrapper_func


@my_decorator_func1
def func1():
    print("This is fucn 1")

func1()

@my_decorator_func2
def func3(any_value):
    print(f"This function takes: {any_value}")

func3("Apple")

import time as t

t1 = t.time()
print(f"Start time -->{t1}")

for i in range(1,10):
    print("")

t2 = t.time()
print(f"End time -->{t2}")

print(f"Time Difference to run program:--> {t2-t1}")


def show_time(any_fuc):
    def wrapper_function(*args,**kwargs):
        ''' this is a wrapper function '''
        print(f"Exectuting function {any_fuc.__name__}")
        t3 = t.time()
        return_vale = any_fuc(*args,**kwargs)
        t4 = t.time()
        time_diff = t4-t3
        print(f"The time diff: -->{time_diff}")
        return return_vale
    return wrapper_function

@show_time
def calc_square(upto_number):
    return [i**2 for i in range(1,upto_number+1)]

user_given_num = int(input("Enter a num:"))


print(calc_square(user_given_num))


# decorator hard question:
'''
def only_int_allow(any_func):
    def wrapper_function(*args,**kwargs):
        stored_data_type=[]
        for i in args:
            stored_data_type.append(type(i)==int)
        if all(stored_data_type):
            return any_func(*args,**kwargs)
        else:
            print("only int is allowed")
    return wrapper_function    
'''

'''
def only_int_allow(any_func):
    def wrapper_function(*args,**kwargs):
        if all([type(i)==int for i in args]):
            return any_func(*args,**kwargs)
        else:
            print("only int is allowed")
    return wrapper_function  
'''

def only_int_allow(any_func):
    def wrapper_function(*args,**kwargs):
        return any_func(*args,**kwargs) if all([type(i)==int for i in args]) else print("only int is allowed")
    return wrapper_function
    
@only_int_allow
def sum_func(*args):
    total = 0
    for i in args:
        total += i
    return total

print(sum_func(1,2,3,4,5,6,7))

# decorator hard question part 4:
'''
def which_data_allow(data_type):
    def decorator_func(any_func):
        def wrapper_function(*args,**kwargs):
            if(all([type(arg)==data_type for arg in args])):
                return any_func(*args,**kwargs)
            else:
                print(f"Only {data_type} is allowed")
        return wrapper_function
    return decorator_func
'''

def which_data_allow(data_type):
    def decorator_func(any_func):
        def wrapper_function(*args,**kwargs):
            return any_func(*args,**kwargs) if(all([type(arg)==data_type for arg in args])) else print(f"Only {data_type} is allowed")
        return wrapper_function
    return decorator_func



@which_data_allow(str)
def join_strings(*args):
    joined_bhayeko_string = ""
    for i in args:
        joined_bhayeko_string += i
    return joined_bhayeko_string

print(join_strings("Sarthak"," Shrestha"))





class Bicycle:
    def __init__(self,gear=5):
        self.gear = gear
    
    def use_break(self):
        return "Break lagau"
    
bicycle1 = Bicycle(10)
print(f"The gear is: {type(Bicycle)}")
print(f"The gear is: {bicycle1.gear}")
print(f"The gear is: {bicycle1.use_break()}")

