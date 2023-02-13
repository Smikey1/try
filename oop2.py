'''
Encapsulation: Write all the methods and functions in one place which are going to perform in 
object data.

Abstraction --> For eg: lst.sort() #make function and method use for easy to user
-
Special naming convension: --> bydefault all public in python 
but to make private only use _ (underscore)

'''

class Laptop1:
    def __init__(self,brand,model_name,price):
        # left trimro value --> right parameter value
        self.brand=brand
        self.model_name=model_name
        self._price=max(price,0)
    
    @property
    def show_full_spec(self):
        return f"The brand is: {self.brand} and price is: {self._price}"
    
    @property
    def price(self):  #getter
        return self._price
    
    @price.setter
    def price(self,new_price):  #getter
        self._price = max(new_price,0)


new_laptop = Laptop1("dell","xps",-150)

print(new_laptop.__dict__)
print(new_laptop.show_full_spec)
print(new_laptop.price)


# Inheritance:
class Phone:  # base class/ parent class
    def __init__(self,brand,model_name,price):
        self.brand=brand
        self.model_name=model_name
        self._price=max(price,0)
    
    @property
    def show_full_spec(self):
        return f"The brand is: {self.brand} and price is: {self._price}"
    
    def dial(self,number):
        return f"dialing .... {number}"

p1 = Phone("Apple","11",500)    
p2 = Phone("Samsung","A11",200)   

print(p1.dial(100))
print(p2.show_full_spec)


class SmartPhone(Phone): # SmartPhone class is derived class and derived from Phone class
    def __init__(self,brand,model_name,price,ram,memory,camera):
        super().__init__(brand,model_name,price)
        self.ram=ram
        self.memory=memory
        self.camera=camera
        
    def open_browser(self,browser_name):
        return f"opening {browser_name} browser"
    
iphone = SmartPhone("Apple","11",500,"2GB","64GB","10MP")    
samsung = SmartPhone("Samsung","A11",200,"1GB","32GB","2MP") 

print(samsung.show_full_spec)
print(samsung.dial(100))
print(iphone.open_browser("Chrome"))


# Multiple Inheritnce

class A:
    def class_a_method(self):
        print("Hello! I am from Class A method")
    
    def my_method(self):
        print("This is my A method")


class B:
    def class_b_method(self):
        print("Hello! I am from Class B method")
    
    def my_method(self):
        print("This is my B method")


class C(B,A):  
    pass

object_a = A()
object_b = B()
object_c = C()

print(object_a.class_a_method())
print(object_a.my_method())
print(object_b.class_b_method())
print(object_b.my_method())

print(object_c.class_a_method())
print(object_c.class_b_method())
print(object_c.my_method()) #MRO --> Method Resoution Order

# print(help(C))
print(C.mro())