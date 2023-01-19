'''
Flexible Functions


*operator --> ( *args, **kwargs)
'''

def sum(a,b):
    ''' it can do sum of two num only, reversed = false (default)'''
    return a+b

print(sum(3,5))

def another_sum(*args):
    ''' can add many num as poosible'''
    sum =0
    for i in args:
        sum += i
    return sum

my_tuple = (1,2,3,4)
my_list = [4,5,6,7]
print(another_sum(*my_tuple))  # tuple un-packing
print(another_sum(*my_list))  # list un-packing

# exapmle 2

def to_power(num,*args):
    if args:
        print(f"The args is: -->{args}")
        return [i**num for i in args]
    else:
        return "You didin't pass any args"

print(to_power(2,3,4,5))

'''
kwargs

'''

def sum_all_num(**kwargs):
    print(f"The type of kwargs is: --> {type(kwargs)}")
    print(f"The kwargs is: {kwargs}")
    for key,value in kwargs.items():
        print(f"The value is: {value}")
    return None

print(sum_all_num(a=5,b=6,c=7,d=8))

def user_details(**sarthak):
    for k,v in sarthak.items():
        print(f"{k}:{v}")

print(user_details(first_name = "Sarthak",last_name="Shrestha",age = 20, fav_book = "computer"))

my_dict = {'a': 5, 'b': 6, 'c': 7, 'd': 8}

def sum_dict_num(**any_dict):
    sum = 0
    for v in any_dict.values():
        sum += v
    return sum

print(sum_dict_num(**my_dict))  # unpacking of dictionary


# function will all type of parameter --> PADK

def fun_all_parameter(name_paramter,*args,abc="sth",**kwargs):
    print(name_paramter)
    print(args)
    print(abc)
    print(kwargs)

print(fun_all_parameter("Sarthak","Shrestha","19","Computer",abcd= "abcd", address="Ktm",p=1,q=2,r=3))

# given
list_of_fruit = ["apple","banana","orange","kiwi","papaya"]
'''
# Question:
make 1st letter of every items in list capital letter,
and if {reversed = true}--> yo default parameter haina yo **kwargs, output must be: ["Elppa","Ananab",......]
-->Q: How use know if a fun can take reversed parameter or not --> use doc string synaxt

# FYI --> you can try with list comprehension too
'''
