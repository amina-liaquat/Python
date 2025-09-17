file = open("example.txt", "r")

content = file.read()   # reads entire file
print("File content:\n", content)

file.close()
