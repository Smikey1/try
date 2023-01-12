'''
list --> an ordered collection of items
list1 =  [1,2,3,4]
 index -->0,1,2,3
'''

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']

# days.append("Valentine day")
# days.insert(2,"father day")

# days.remove("Friday")
# days.pop()

nikalekoValue = days.pop(len(days)-2)
print(f"nikalekoValue-->{nikalekoValue}")

# print(days[2:5])
print(days)


numList1 = [0,2,4,6]
numList2 = [0,2,4,6]

# print(numList1 is numList2)
# print(numList1 == numList2)

print(f"The IS is: -->{numList1 is numList2}")
print(f"The == is: -->{numList1 == numList2}")

for i in numList1:
    print(i)

if 4 in numList1:
    print("Present")

if 5 in numList1:
    print("Not Present")

print(max(numList1))
print(min(numList1))
print(sum(numList1))

def give_me_list(num):
    my_list = []
    for i in range(0,num+1):
        my_list.append(i**2)
    return my_list

any_num = int(input("Enter a num up to square:"))
returned_sq_list = give_me_list(any_num)
print(returned_sq_list)

sq_list = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144]

def rev_list(req_list):
    rev_bhako_list = []
    for i in req_list:
        popped_item=req_list.pop()
        rev_bhako_list.append(popped_item)
    return rev_bhako_list

print(rev_list(sq_list))

def revs_list(req_list):
    req_list.reverse()
    return req_list


print(revs_list(sq_list))

any= ["apple","fruit","banana","grapes"]
# any2 = [1,2,3,4,5,6,7,8,9,10,............n] ==> [[odd_num],[even_num]]
