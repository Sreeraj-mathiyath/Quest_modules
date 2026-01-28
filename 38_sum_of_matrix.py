def sum(m1,m2):
    total=0
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            total=m1[i][j]+m2[i][j]
            print(total,end=" ")   
        print()
m1=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
m2=[
    [9,8,7],
    [6,5,4],
    [3,2,1]
]
print("Sum of two matrices:")
sum(m1,m2)
