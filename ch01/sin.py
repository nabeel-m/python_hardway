import math
def factorial(a):
        fact=1
        for i in range(1,a+1):
                fact=fact*i
        return fact

def sinval(x,n):
        sin=0
        for i in range(0,n):
                sign=(-1)**i
                pi=22/7
                radiant=x*(pi/180)
                sin=sin+((radiant**(2*i+1))/factorial(2*i+1))*sign
                #sine=round(sin,2)
        return sin
        
#x=int(input("Enter the values in degree."))
n=int(input("Enter the no.of terms:"))
for x in range(0,90):
        print(f"sin{x}degree :",sinval(x,n))  

