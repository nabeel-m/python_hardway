A = set(['brazil','russia','india'])
print('india' in A)
print('usa' in A)

B = A.copy()
print("set B_________________________:",B)
B.add('china')
print("set B after altered___________:",B)
print("Is B superset of A____________:",B.issuperset(A))

A.remove('russia')
print("after removing russia_________:",A)

print("intersection of set A and B__ :",A & B)
print("Union of set A and B__________:",A.union(B))

print("sort B________________________:",sorted(B))