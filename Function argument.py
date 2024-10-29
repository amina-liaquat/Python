         # Default Arguments 
def name(fname, mname="Buddy", lname="Giraffe"):
    print("Hello",fname,mname,lname)
name("Golu")
         # Keywords Arguments
def name(fname,mname,lname):
    print("Hello",fname,mname,lname)
name(fname="Rabbit",mname="Buddy",lname="Motu")
         # Required Arguments
# def name(fname, mname, lname):
#     print("Hello,", fname, mname, lname)
# name("Peter", "Quill")
def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)
name("Peter", "Ego", "Quill")
        # Variable length Arguments
    # Arbitatery
def name(*name):
    print("Hello",name[0],name[1],name[2])
name("Rabbit","Giraffe","Buddy")
     # Keyword Arbitatery 
def name(**name):
    print("Hello,",name["fname"],name["mname"],name["lname"])
name(fname="Amina",mname="Buddy",lname="Giraffe")
        # Return Statement
def name(fname,mname,lname):
     return "Hello, " + fname + " " + mname + " " + lname
print(name("James", "Buchanan", "Barnes"))

