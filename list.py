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