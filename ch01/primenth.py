from sympy import prime
def primenth(n):
    nth_prime=prime(n)
    return nth_prime

n=int(input("Enter the limit:"))
print(f"{n}th prime is:",primenth(n))    

         



               
