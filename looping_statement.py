i = 0
while i <10:
    print(f"Hello World {i}")
    i += 1

for i in range(0,10,1):
    print(f"FOR LOOP {i}")

############################################
# 4371--> 4+3+7+1 = 15

# first


user_num = input("please enter any 4 digit:")
sum = 0
for i in range(len(user_num)):
    sum += int(user_num[i])
print(f"The final sum was: {sum}")

sum1 = 0
for i in user_num:  # "4573"
    sum1 += int(i)
print(f"The final sum was: {sum1}")

full_name = input("please enter your full name:")
i = 0
store =""
# full_name.replace(" ","")
while i < len(full_name):
    if full_name[i] not in store:
        store += full_name[i]
        print(f"{full_name[i]}:{full_name.lower().count(full_name[i])}")
    i+=1

# break and continue
for i in range(1,15):
    if i == 5:
        continue

    if i == 10:
        break

    print(f"The value of i is: -->{i}")