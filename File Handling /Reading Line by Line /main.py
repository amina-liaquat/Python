file = open("example.txt", "r")

for line in file:
    print(line.strip())   # strip() removes extra newlines

file.close()

