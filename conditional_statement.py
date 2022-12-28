# python--> if else  --> if elif elif else:

age = int(input("Please, enter your age: "))

if age>20:
    print("You can watch movie")
else:
    print("you cannot watch movie \n your age is less than 20 years")

fname = input("Please enter your name: ")

if "a" in fname:
    print("A is present in Fname")
    if "as" in fname:
        print("AS founded")
elif "s" in fname:
    print("S is present")
else:
    print("Your name is UNIQUE")
