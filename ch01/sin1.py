import math
def sin(x):
        rad=math.radians(x)
        sine=math.sin(rad)
        return sine

x=int(input("Enter an angle:")) 
print(f"sin{x}",sin(x))               