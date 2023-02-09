'''
Generators


--> They are iterator
--> And they are in the form of sequence structure like list = [1,2,3,4]
--> But we have list, then why we need generator? As we can loop in the list too.


#List
#memory --> a time is required in creation of list and after creation the memory
#is reserved by the list
#It is used for continuous case/ frequently.

# Generator
#memory --> in generator sequence, only one number is generated and stored at a time.
# It is used for only one time.

'''

# 0) create generator with generator function and  or generator comprehension
# with generator function:
def generate_num_upto(num):
    for i in range(1,num+1):
        yield(i) # yield is used for generator object

print(generate_num_upto(10))

# generator is called when we only demand it because it is a iterator 
# so it has a next() function
# And we can only loop once in generator because it is no longer availabe in
# memory anymore once it generated.

genereted_num = generate_num_upto(10)

for i in genereted_num:
    print(f"The I is:-->{i}")

for j in genereted_num:
    print(f"The J is:-->{j}")



def generate_num_upto1(num):
    for i in range(1,num+1):
        if i %2 ==0:
            yield(i) # yield is used for generator object

print(generate_num_upto1(20))

genereted_num1 = generate_num_upto1(20)

for m in genereted_num1:
    print(f"The ONE is:-->{m}")

sq1 = [i**2 for i in range(1,10+1)] # list comprehension
print(sq1)

sq2 = (i**2 for i in range(1,10+1))  # generator comprehension
print(sq2)

for k in sq2:
    print(f"The K is-->{k}")

for l in sq2:
    print(f"The L is-->{l}")


#1) Create generator vs creation of list with 10 
# million data:
'''import time as t
t1 = t.time()
sq_list = [i**2 for i in range(10000000)]
t2 = t.time()
print(f"Total time to create 10M list is:{t2-t1}")'''

import time as t
t3 = t.time()
sq_gen_obj = (i**2 for i in range(1000000000))
t4 = t.time()
print(f"Total time to create 100M gen obj is:{t4-t3}")
print(sq_gen_obj)