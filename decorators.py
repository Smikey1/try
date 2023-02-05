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

