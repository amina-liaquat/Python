class Animal:
    def speak(self):
        print("This animal makes a sound")

class Dog(Animal):  # Dog inherits from Animal
    def speak(self):
        print("Woof! Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow! Meow!")

# Usage
dog = Dog()
cat = Cat()

dog.speak()  # Woof! Woof!
cat.speak()  # Meow! Meow!
