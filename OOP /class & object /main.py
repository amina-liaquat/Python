# Defining a class
class Car:
    # Constructor
    def __init__(self, brand, model):
        self.brand = brand   # attribute
        self.model = model   # attribute

    # Method
    def display_info(self):
        print(f"Car: {self.brand} {self.model}")

# Creating objects
car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

car1.display_info()  # Car: Toyota Corolla
car2.display_info()  # Car: Honda Civic
