def check(m1,m2):
    if len(m1)!=len(m2) or len(m1[0])!=len(m2[0]):
        return "Matrices are not of same dimension"
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            if m1[i][j]!=m2[i][j]:
                return "Matrices are not equal"
            
    return "Matrices are equal"

m1=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
m2=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(check(m1,m2))
print(len(m1),len(m1[0]))