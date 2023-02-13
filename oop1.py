'''
OOP Part 1
--> It is just a way to write a code.
--> Very helpful and importance for creating real world programs.
--> CLASS,OBJECT(instance), METHODS, Class-Variable and so on.

1) Create your first class
class, init method/constructor takes attributes, instance variable or 
creation of objects
'''


def add():
    return 2+3

class Calculate:
    def sum():
        return 2+3



class Person:
    #init method/constructor
    def __init__(self,nameA,age,adderess):  # it will take attributes
        print("This is init method")
        # instance/object variable
        self.name =nameA
        self.age=age
        self.address=adderess
    
    # creation of another method:
    def user_introduction(self):
        print(f"Your name is: {self.name} and age is: {self.age}")

# Now I will create a obj:
# obj_name - class_name()

p1 = Person("Sarthak",18,"Ktm")
p2 = Person("sita",19,"butwal")
p1.user_introduction()

print(p2.name)


class Circle:
    pi = 3.14
    def __init__(self,radius):
        self.radius = radius
    
    def calc_area(self):
        return self.pi * (self.radius**2)

    def calc_perimeter(self):
        return 2*self.pi * self.radius**2

# In conclusion: self is used only if class variable are mean to change

c1 = Circle(14)
c2 = Circle(7)
print(c1.calc_area())
print(c2.calc_perimeter())


class Laptop:
    count_total=0
    def __init__(self,brand):
        Laptop.count_total  += 1
        self.brand = brand
    
    @classmethod
    def count_obje(self):
        return f"You have {Laptop.count_total} created of laptop in your {self.__name__} Store"

dell = Laptop("dell")
hp = Laptop("hp")
print(dell.count_obje())
print(Laptop.count_obje())