def order(arr1,arr2):
    if arr1==arr2:
        return "Both arrays are identical"
    elif arr1<arr2:
        return "First array is smaller than second array"
    else:
        return "First array is larger than second array"
    
array1=[i for i in range(5)]
array2=[i for i in range(5)]
print("First array:", array1)
print("Second array:", array2)
print(order(array1,array2))