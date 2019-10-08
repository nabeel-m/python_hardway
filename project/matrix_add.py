def create1matrix(r1,c1):
    matrix1,q=[],0
    for i in range(r1):
        a=[]
        for j in range(c1):
            q=int(input())
            a.append(q)
        matrix1.append(a)
    return matrix1   

def create2matrix(r2,c2):
    matrix2,q=[],0
    for i in range(r2):
        a=[]
        for j in range(c2):
            q=int(input())
            a.append(q)
        matrix2.append(a)
    return matrix2

def matrix_add(matrix1,matrix2):
    matrix3,a,q=[],0
    if (r1==r2 and c1==c2):
        for i in range(r2):
            a=[]
            for j in range(c2):
                q=matrix1[i][j]+matrix2[i][j]
                a.append(q)
            matrix3.append(a)    
        return matrix3  

r1=int(input("Enter nos of rows in 1st matrix:"))
c1=int(input("Enter nos of colums in 1st matrix"))  
print(create1matrix(r1,c1))

r2=int(input("Enter nos of rows in 1st matrix:"))
c2=int(input("Enter nos of colums in 1st matrix"))
print(create2matrix(r2,c2))

print("sum of two matrices:")
print(matrix_add(matrix1,matrix2))        




