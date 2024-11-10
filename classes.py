# class Person:
#     name= "Amina"
#     occupation="Student"
#     age=23
#     def info(self):
#         print(f"{self.name} is a {self.occupation}")
# a=Person()
# b=Person()
# a.name="Miral"
# a.occupation="BabyGirl"
# b.name="Musa"
# b.occupation="Frontend Developer"
# # print(a.name)
# # print(a.occupation)
# # print(a.age)
# a.info()
# b.info()

# class Animal:
#     attr1="Rabbit"
#     attr2="Giraffe"
#     def info(self):
#         print(f"{self.attr1} is a bestfreind of {self.attr2}")
# a=Animal()
# b=Animal()
# b.attr1="Golu"
# b.attr2="Motu"
# # print(a.attr1, a.attr2)
# a.info()
# b.info()


# class Person:
#     def __init__(self,name,occupation):
#         print("Hey I am a Person")
#         self.name=name
#         self.occupation=occupation
#     def info(self):
#         print(f"{self.name} is a {self.occupation}")
# a=Person("Amina","Student")
# b=Person("Buddy","Giraffe")
# a.info()
# b.info()

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    @staticmethod
    def Hello():
        print("Hello")
    def get_avg(self):
        sum=0
        for val in self.marks:
            sum += val
        print("Hi,",self.name,"Your avg score is:",sum/3)
s1=Student("Amina",[99,89,98])
s2=Student("Musa",[89,98,99])
s3=Student("Buddy",[89,78,68])
s1.get_avg()
s2.get_avg()
s3.get_avg()

s1.Hello()

