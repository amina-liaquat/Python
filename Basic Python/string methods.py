# Strings are immutable
a = "!!!Amina!! !!!!!!!!! Amina"
print(len(a))
print(a)
print(a.upper())    #Converts a string into upper case
print(a.lower())     #Converts a string into lower case
print(a.rstrip("!"))  #	Returns a right trim version of the string
print(a.replace("Harry", "John"))  
print(a.split(" "))    #split string from left /The split() method splits a string into a list.
blogHeading = "introduction tO jS"
print(blogHeading.capitalize())

str1 = "Welcome to the Console!!!"
print(len(str1))
print(len(str1.center(50)))
print(a.count("Amina"))

str1 = "Welcome to the Console !!!"
print(str1.endswith("!!!"))

str1 = "Welcome to the Console !!!"
print(str1.endswith("to", 4, 10))

str1 = "He's name is Dan. He is an honest man."
print(str1.find("ishh"))
# print(str1.index("ishh"))

str1 = "WelcomeToTheConsole"
print(str1.isalnum())
str1 = "Welcome"
print(str1.isalpha())

str1 = "hello world"
print(str1.islower())

str1 = "We wish you a Merry Christmas\n"
print(str1.isprintable())
str1 = "         "       #using Spacebar
print(str1.isspace())
str2 = "  "       #using Tab
print(str2.isspace())

str1 = "World Health Organization" 
print(str1.istitle())

str2 = "To kill a Mocking bird"
print(str2.istitle())

str1 = "Python is a Interpreted Language" 
print(str1.startswith("Python"))

str1 = "Python is a Interpreted Language" 
print(str1.swapcase())  #Convert uppercase characters to lowercase and lowercase characters to uppercase.

str1 = "His name is Dan. Dan is an honest man."
print(str1.title())  #words start with uppercased characters and all remaining
                     # cased characters have lower case.
