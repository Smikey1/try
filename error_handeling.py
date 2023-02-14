'''
Error Handeling

'''
#1 syntax error
'''
def fun()):
    print("Done")
   
'''
#2 Indentation Error:
def fun():
    print("")

# Name Error
ok =1
print(ok)

#Type Error 
print("1"+"A")
# print(1+"A")

# index error
list1 = [1,2,3]
# print(list1[5])

a = "2"
b="M"

# print(int(b))

#Key Error
map1= {"name":"Sarthak"}
# print(map1["names"])

# -------> Raise Error
class SarthakError(TypeError):
    pass

def add(a,b):
    if(type(a)==int and type(b)==int):
        return a+b
    raise SarthakError("Not a int number")

# print(add("a",2))


# Example 1:

class ApplePhone:  # base class/ parent class
    def __init__(self,brand,model_name,price):
        self.brand=brand
        self.model_name=model_name
        self._price=max(price,0)
        self.weight = "123g"
    
    @property
    def show_full_spec(self):
        return f"The brand is: {self.brand} and price is: {self._price}"
    
    def dial(self,number):
        return f"dialing .... {number}"

ap = ApplePhone("Apple","11",500)    

print(ap.dial(100))
print(ap.show_full_spec)


class SamsungPhone: # SmartPhone class is derived class and derived from Phone class
    def __init__(self,brand,model_name,price,ram,memory,camera):
        self.ram=ram
        self.memory=memory
        self.camera=camera
        
    def open_browser(self,browser_name):
        return f"opening {browser_name} browser"
    
sp = SamsungPhone("Samsung","A11",200,"1GB","32GB","2MP") 
print(sp.open_browser("Chrome"))

class AddPhoneToStoreError(TypeError):
    pass

class AppleStoreHaru:
    def __init__(self):
        self.mobile_stores=[]  # instance variable
    
    def add_mobile(self,new_mbl):
        if (isinstance(new_mbl,ApplePhone)):
            self.mobile_stores.append(new_mbl)
            print(self.mobile_stores)
        else:
            raise AddPhoneToStoreError("New Mobile is a type of Apple Phone")
      
appleStore = AppleStoreHaru()
# appleStore.mobile_stores.append(ap)
appleStore.add_mobile(ap)
# appleStore.add_mobile(sp)


# ----> Exception Handeling

'''
while True:
    try:
        age= int(input("Please enter your age:"))
        if age>18:
            print("you can vote")
        else:
            print("you can not vote")
        break
    except ValueError:
        print("Age Must be integer num")
    except:
        print("unexpected error")
'''

# Better Version:
while True:
    try:
        age = int(input("Please enter your age:"))
    except ValueError:
        print("Age Must be integer num")
    except:
        print("unexpected error")
    else: # it runs only when try block run
        print(f"Your age is: -->{age}")
        break
    finally: #it always run
        print(f"No matter of error! It always runs0")
        break
    

# Example:
def divide(a,b):
    try:
        return a//b
    except ZeroDivisionError as zde_message:
        print(f"The message was-->{zde_message}")
        raise ZeroDivisionError("Can't divide by zero") 

    except TypeError as te_message:
        print(f"The message was-->{te_message}")
        raise TypeError("Int only") 
    
    except:
        return "Unexpected error"

print(divide(10,2))

