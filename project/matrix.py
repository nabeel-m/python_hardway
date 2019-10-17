def matrix():
    mat=[[int(input()) for i in range(c)]for j in range(r)]
    return mat
    
def matrixadd(mat1,mat2):
    return [list(map(sum,zip(*rows))) for rows in zip(mat1,mat2)]
    

r=int(input("Enter the rows:"))
c=int(input("Enter the colums:"))
mat1=matrix()
print(mat1)

r=int(input("Enter the rows:"))
c=int(input("Enter the colums:"))
mat2=matrix()
print(mat2)

print("sum of two matrixes:")
sum=matrixadd(mat1, mat2)
print(sum)