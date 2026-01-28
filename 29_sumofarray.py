def sum(array):
    total=0
    for num in array:
        total+=num
    return total

array=[i for i in range(1,20,3)]
print("Array elements:", array)
print("Sum of array elements:", sum(array))