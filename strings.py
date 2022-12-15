#variable 
space_problem = "       Sarthak         Shrestha       "
stars = "************"
print(stars+space_problem+stars)

# strip() --> lstrip(), rstrip()--> remove space form left and right

print(stars+space_problem.lstrip()+stars)
print(stars+space_problem.rstrip()+stars)
print(stars+space_problem.strip()+stars)

solved_problem =space_problem.strip().replace(" ","")
print(solved_problem)

# ram prased Shah --> Ramprasadshah 

print(solved_problem.upper())

given_name = input("Please, Enter your full name: ")
print(given_name.strip().replace(" ","").upper()=="SONUKUMAR")
my_var = given_name.strip().replace(" ","").upper()=="SONUKUMAR"
if my_var==True:
    print("Bank Account validated successfully")
else:
    print("Invalid account number")