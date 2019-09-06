num1 = input("Enter 1st number:")
num2 = input("Enter the 2nd number:")
num3 = input("Enter the 3rd number:")

if num1 > num2:
    largest = num1

elif num2 > num3:
    largest = num2

else:
    largest = num3

print(f"{largest} is the largest numbers among three ")        
