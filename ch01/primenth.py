n=int(input("Enter a limit:"))   

num=1
if n == 1:
    print("1th prime number is 2")

else:
    count =1
    while count <= n:
        num+=1
        for i in range(2,num):
            if num%i ==0:
                break
            else:
                continue
        else:
            prime=num
            count+=1  
    else:
        print(f"""{n}th prime no. is {prime}""")            
         



               
