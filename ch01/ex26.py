i = 0
numbers =[]

while i < 6:
    print(f"At the top of i is{i}")
    numbers.append(i)
    i=i+1
    print("number is",numbers)
    print(f"At the bottom of i is {i}")

print("numbers")

for num in numbers:
    print(num)
