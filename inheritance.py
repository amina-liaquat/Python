
'''class Car:
    color="Black"

    @staticmethod
    def start():
        print("Car Started")

    @staticmethod
    def stop():
        print("Car Stopped")
class Toyota(Car):
    def __init__(self,name):
        self.name=name
    
car1=Toyota("Fortuner")

print(car1.name)
print(car1.start())
print(car1.stop())'''

  # types of inheritance  (Multi level inheritance)

'''class Car:
    

    @staticmethod
    def start():
        print("Car Started")

    @staticmethod
    def stop():
        print("Car Stopped")

class Toyota(Car):
    def __init__(self,brand):
        self.brand=brand

class Fortuner(Toyota):
    def __init__(self,type):
        self.type=type

car1=Fortuner("Diesel")

print(car1.type)
print(car1.start())'''

       # Multiple inheritance

'''class CarA:
    varA= "Welcome to class A"

class CarB:
    varB="Welcome to class B"

class CarC(CarA,CarB):
    varC= "Welcome to class C"


c1= CarC()

print(c1.varA)
print(c1.varB)
print(c1.varC)
'''

    # super() method 

class Car:
    
    def __init__(self,type):
        self.type=type
    @staticmethod
    def start():
        print("Car Started")

    @staticmethod
    def stop():
        print("Car Stopped")

class Toyota(Car):
    def __init__(self,name,type):
        super().__init__(type)
        self.name=name

c1= Toyota("prius","electric")
print(c1.name)
print(c1.type)
