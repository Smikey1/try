#Hierarchial Inheritance
class Engine:
    def __init__(self,kg,qty):
        self.kg=kg
        self.qty= qty
    
    def createEngine(self):
        return f"Single engine created"

class Ford(Engine):
    def __init__(self,kg, qty,ford_design):
        super().__init__(kg, qty)
        self.ford_design=ford_design
    
    def createEngine(self):
        return f"Ford engine created"

class Nano(Engine):
    def __init__(self, kg, qty,nano_design):
        super().__init__(kg, qty)
        self.nano_design=nano_design


f = Ford(1,2,3)
print(f.createEngine())

# Multi-level Inheritance:
# for more visit here: https://simplesnippets.tech/wp-content/uploads/2018/04/java-types-of-inheritance.jpg
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


class FlagshipPhone(SmartPhone):
    def __init__(self,brand,model_name,price,ram,memory,camera,security):
        super().__init__(brand,model_name,price,ram,memory,camera)
        self.security=security

p1 = Phone("Dialer Phone","11",500)   
sp = SmartPhone("Apple","11",500,"2GB","64GB","10MP")    
fp = FlagshipPhone("Samsung","A11",200,"1GB","32GB","2MP","Khatra Xa") 

# print(help(FlagshipPhone))

# instance --> object pani ho
print(isinstance(sp,FlagshipPhone))  # bool output
print(issubclass(FlagshipPhone,SmartPhone))  # bool output
