print(2+2)
print("Hello World!! ")

# String Formating
name = "Sarthak"

# ways to create variable

my_name = "Apple"  # snake_case_writing  --> for python
myName = "Apple"   # camelCaseWriting

print(my_name)

your_name = input("Please, enter your name: ")

print("Your given name is: -->"+your_name)

age = int(input("Please, enter your age"))

# str() --> convert int to string
# 15 --> int ;  "apple"+"15" --> apple15
# "sarthak " + "Shrestha" --> Sarthak Sthrstha
print("In next five year, your age will be: -->"+str(age+5))  # bad practice

print(f"Hello! {your_name}, In next five year, your age will be: --> {age+5}")  # good practice

name,age = input("Please, enter your name and age (comma separate)").split(",")

print(f"Hello! {name}, your age is: --> {age}")