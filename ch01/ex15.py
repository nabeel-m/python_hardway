from sys import argv

script,filename = argv

print(f"We are going to erase {filename}")
print("If you don't want that hit CTR - C ()")
print("If you do want that,hit RETURN")

input("?")

print(f"opening the file {filename}")
target = open (filename,"w")

print(f"Truncate the file {filename}")
target.truncate()

print("Now I'm going to ask you 3 lines")

line1 = input("line1:")
line2 = input("line2:")
line3 = input("line3:")

print("Now I'm going to write this to the file")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("\n")
print(f"Read the file {filename}")
target = open(filename)
print(target.read())

print("finally we close it")
target.close()
