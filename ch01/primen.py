def primen(n):
    num=1
    if n == 1:
        prime=2
        return prime

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
            return prime    

n=int(input("Enter the limit:"))
print(f"{n}th primeno is:",primen(n))
        