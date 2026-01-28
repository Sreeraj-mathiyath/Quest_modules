def matrix_2x2(a, b, c, d):
    return [[a, b],[c, d]]

print(matrix_2x2(1, 2, 3, 4))

num=0
for i in range(2):
    for j in range(2):
        num+=1
        print(num, end=" ")
    print()