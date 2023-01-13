'''
It is a unordered collection of items, stored in the form of --> key:value pair
key won't repeat in dict:
but why dict, due to limitation of list

user = ["Sharthak","Shrestha",20,["thor","ant man"],["song 1","song 2"],"apple",["a",1,"b",2]]

user = {"fname":"Sharthak","lname":"Shrestha","age":20, 
fav_movie:["thor","ant man"], fav_song:["song 1","song 2"],
"fav_food":"apple",
"mix_fav":["a",1,"b",2]
}

'''
# 1st way to create dict --> 98%
user = {"fname":"Sharthak","lname":"Shrestha","age":20, 
"fav_movie":["thor","ant man"], "fav_song":["song 1","song 2"],
"fav_food":"apple",
"mix_fav":["a",1,"b",2]
}

print(user)
print(type(user))

#2nd way to create dict:--> 2%
weekdays = dict(day1="Sunday",day2="Monday",day3="Tuesday")
print(weekdays)
print(type(weekdays))

# how to get data from dict:
user1 = ["Sharthak","Shrestha",20,["thor","ant man"],["song 1","song 2"],"apple",["a",1,"b",2]]

print(user["age"])
print(user1[3][1])
print(user["fav_song"][0])

# add value to dict:
emp_dict = {'key5': 5}
emp_dict["key1"] = 1  # dict ma key xaina bhane add garxa
emp_dict["key5"] = 1  # dict ma key xa bhane update garxa
print(emp_dict)


user11 = {"fname":"Sharthak","lname":"Shrestha","age":20, 
"fav_movie":["thor","ant man"], "fav_song":["song 1","song 2"],
"fav_food":"apple",
"mix_fav":["a",1,"b",2]
}

if "fname" in user11:
    print("present")
    if "Sharthak" == user11["fname"]:
        print("value present")
else:
    print("not present")

# print(user11["fav_player_name"])

users=[
    {"user_id":"random create","contact":"registred contact num","balance":"available","pp":"uploaded"},
    {"user_id":"random create","contact":"registred contact num","balance":"available","pp":"uploaded"},
    {"user_id":"random create","contact":"registred contact num","balance":"available","pp":"uploaded"}
]

particular_user = {"user_id":"random create","contact":"registred contact num","balance":"available","pp":"uploaded"}

# contact_num=input("num:")
# if particular_user.get("contact_num") ==None:


# various method of dict:
# keys(), values(), items(),copy(), clear(), get()

if "Sharthak" in user11.keys():
    print("present Sharthak")
else:
    print("not present")

# loop in dict
for k in user11.keys():
    print(k)

# items method return --> tuple(key,value)

for k in user11.items():
    print(f"The key is--> {k}")


for k,v in user11.items():
    print(f"The key is--> {k} & The value is--> {v}")

# copy method:
user12 = user11.copy()
print(user12)

print(user12.get("fav_boot"))
print(user12.get("fav_food"))
# print(user12["fav_boot"])

# user12.pop("fav_food")

print(user12["fav_song"].pop(0))

# clear method
user12.clear()
print(user12)


# Ex: 1
'''
Ask a num with user:
output must be: {1:1, 2:8, 3:27 ..... n:n^3}
'''

# Ex2: 
"""
Optimize the word counter of your name
"s":1
"h":2
"a":2
r
t
"h":2
"a":2
k:
"""

'''
Un optimized code:
full_name = input("please enter your full name:")
i = 0

while i < len(full_name):
    print(f"{full_name[i]}:{full_name.lower().count(full_name[i])}")
    i+=1
'''

def count_char(name):
    char_empty_dict={}
    for char in name:
        char_empty_dict[char]=name.lower().count(char)
    return char_empty_dict

'''
WORKING LOGIC OF COUNT CHAR 

# add value to dict:
emp_dict = {'key5': 5}
emp_dict["key1"] = 1  # dict ma key xaina bhane add garxa
emp_dict["key5"] = 1  # dict ma key xa bhane update garxa
print(emp_dict)
'''

full_name = input("please enter your full name:")
print(count_char(full_name))