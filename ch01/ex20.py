def add(a,b):
    print(f"adding {a} + {b}")
    return a + b

def substract(a,b):
     print(f"substract {a} - {b}")
     return a - b

def multiply(a,b):
     print(f"multiplying {a} * {b}")
     return a * b

def division(a,b):
     print(f"Division {a} / {b}")
     return a / b


print("let's do some math just functions")
age = add(30, 5)
height = substract(78, 4)
weight = multiply(90, 2)
iq = division(100, 2)

print(f"Age:{age}\nHeight:{height}\nweight:{weight}\niq:{iq}")