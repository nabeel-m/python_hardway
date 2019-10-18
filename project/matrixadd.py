def matrix(r,c):
    mat=[[int(input()) for i in range(c)]for j in range(r)]
    return mat
    
def matrixadd(mat1,mat2):
    result=[[0 for i in range(c)]for j in range(r)]
    for i in range(len(mat1)):
        for j in range(len(mat1[0])):
            result[i][j]=mat1[i][j]+mat2[i][j]
    return result  
    
r=int(input("Enter the rows:"))
c=int(input("Enter the colums:"))
mat1=matrix(r,c)
print(mat1)

r=int(input("Enter the rows:"))
c=int(input("Enter the colums:"))
mat2=matrix(r,c)
print(mat2)

print("sum of two matrixes:")
sum=matrixadd(mat1, mat2)
print(sum)