class Bird:
    def fly(self):
        print("Some birds can fly")

class Eagle(Bird):
    def fly(self):
        print("Eagles fly high")

class Penguin(Bird):
    def fly(self):
        print("Penguins cannot fly")

# Usage
birds = [Eagle(), Penguin()]
for b in birds:
    b.fly()
