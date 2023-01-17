'''
List Comprehension
Syntax1: [append_item for loop]
Syntax2: [append_item for loop if condition]
Syntax3: [append_item if condition else condtion for loop]
'''

'''
SYNTAX 1

def give_me_list(num):
    my_list = []
    for i in range(0,num+1):
        my_list.append(i**2)
    return my_list

any_num = int(input("Enter a num up to square:"))
returned_sq_list = give_me_list(any_num)
print(returned_sq_list)

print([i**2 for i in range(0,10+1)])
'''

'''
# SYNTAX 2
def give_me_list(num):
    my_list = []
    for i in range(0,num+1):
        if i%2==0:
            my_list.append(i**2)
    return my_list

any_num = int(input("Enter a num up to square:"))
returned_sq_list = give_me_list(any_num)
print(returned_sq_list)

print([i**2 for i in range(0,10+1) if i%2==0])
'''

def give_me_list(num):
    my_list = []
    for i in range(0,num+1):
        if i%2==0:
            my_list.append(i**2)
        else:
            my_list.append(-i**2)
    return my_list

any_num = int(input("Enter a num up to square:"))
returned_sq_list = give_me_list(any_num)
print(returned_sq_list)


print([i**2 if i%2 == 0 else -i**2 for i in range(0,10+1)])

# Nested Loop:
# [[1,2,3],[1,2,3],[1,2,3]]

# print([[i for i in range(1,3+1)] for k in range(1,3+1)])
print([f"The value of k:{k}--> {[i for i in range(1,3+1)]}" for k in range(1,3+1)])
