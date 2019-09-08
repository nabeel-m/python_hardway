n=int(input("Enter a limit:"))   
count=0
num=0


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
            
        
print(f"""{n}th primeno. is {prime}""")    


               
