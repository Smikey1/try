'''
Lambda Expression --> Anonymous(no-name) Function

def sum(a,b):
    return a+b

Lambda syntax:
lambda p1,p2,p3: returning_value

lamda a,b : a+b  # lambda function of sum

Actually, we won't use/assign lambda function into variable.
We use it with advance builtin function like--> map,reducde,filter so on

'''

def sum(p1,p2,p3):
    return p1+p2+p3

mero_sum_func = sum(1,2,3)

mero_sum_func2 = lambda p1,p2,p3:p1+p2+p3

print(mero_sum_func)
print('-------------')

ok1 = sum
print(ok1(1,1,1))

print(mero_sum_func2(5,6,7))

print(type(mero_sum_func2))


# check even function

def check_even(num):
    return num% 2==0

# with lambda function:
a=lambda num: num%2==0
print(a(10))