flames=["friend","love","affection","marriage","enemy","sister"]

p1=(input("Enter male name:"))
p2=(input("Enter female name:"))

m1=p1.lower()
m2=p2.lower()

for i in range(len(m1)):
    for j in range(len(m2)):
        if m1[i]==m2[j]:
            m2=m2.replace(m2[j],"*")
            break

temp=m2.count('*')*2
print(temp)

temp1=len(m1)+len(m2)-temp


while(len(flames)>1):
    count=-1
    while count<temp1:
        count+=1
        i=(i+1)%len(flames)
    flames.remove(flames[i-1])
relation=flames[0]
print(f"Relationship is:{relation}")

