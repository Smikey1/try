# define/ declare function: --> with parameter
def value_requirement(a, b):
    myString = f"1st value: {a} \n2nd value: {b}"
    return myString

# function calling with argument
function_le_returned_value = value_requirement(b=5,a=6)

print(function_le_returned_value)


def check_odd_even(num):
    return True if(num %2 == 0) else False

def check_odd_evens(num):
    return num %2 == 0

returned_value = check_odd_evens(5)
print(check_odd_evens(5))

def check_palindrome(num):
    return num == num[-1::-1]



def greater(num1,num2):
    # return num1 if num1>num2 else num2 
    if num1>num2:
        return num1
    else:
        return num2

first,second,third = input("please, enter three number:").split(",")
print(greater(int(first),int(second)))


def greatest():
    return greater(greater(int(first),int(second)),int(third))


# hw: --> 17,8,9 --> 17


# function inside function
def sum(a,b):
    return a + b

def product(a,b):
    return a*b


def main_function(any_function, num1,num2):
    return any_function(num1,num2)


print(main_function(product,5,6))
'''
ERROR XA --> but logic of reference

def sum() --> return a+b 
def multiply() --> return a*b

+   /     *

result = merofunction(multiply,2,3)

'''
