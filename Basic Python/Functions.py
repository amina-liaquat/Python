import math

def CalculateGmean(a, b):
    gmean = math.sqrt(a * b)
    print("Geometric Mean:", gmean)

def isGreater(a, b):
    if a > b:
        print("First Number is Greater")
    else:
        print("Second Number is Greater")

def isLesser(a, b):
    if a < b:
        print("First Number is Lesser")
    else:
        print("Second Number is Lesser")

a = 5
b = 9
isGreater(a, b)
isLesser(a, b)
CalculateGmean(a, b)

c = 8
d = 4
isGreater(c, d)
isLesser(c, d)
CalculateGmean(c, d)
