'''
Flexible Functions


*operator --> ( *args, **kwargs)
'''

def sum(a,b):
    ''' it can do sum of two num only'''
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
