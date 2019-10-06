row=int(input("Enter nos of rows:"))
col=int(input("Enter nos of colums"))
group=0

matrix = []
for i in range(0,col):
    a=[]
    for j in range(0,row):
        a.append(int(input()))
    matrix.append(a) 

for i in range(0,col):
    for j in range(0,row):
        print(matrix[i][j],end=" ")  
    print() 

for i in range(0,col):
    for j in range(0,row):
        if(matrix[i][j]==1 and matrix[i+1][j]==1):
            group=group+1
        elif(matrix[i][j]==1 and (matrix[i+1][j+1]==1 or matrix[i+1][j-1]==1)):
            group=group+1
print(f"group:{group}")