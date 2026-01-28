def transpose(matrix):
    transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]

    return transposed

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
transposed_matrix = transpose(matrix)
print("Original Matrix:")   
for row in matrix:
    print(row) 
print("Transposed Matrix:")
for row in transposed_matrix:
    print(row)
    
    