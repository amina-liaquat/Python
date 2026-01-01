class Bird:
    pass

class FlyingBird(Bird):
    def fly(self):
        print("This bird can fly")

class Eagle(FlyingBird):
    def fly(self):
        print("Eagles fly high")

class Penguin(Bird):
    pass
