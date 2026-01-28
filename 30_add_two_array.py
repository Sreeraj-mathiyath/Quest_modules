def AddArray(arr1,arr2):
    result=[]
    for i in range(len(arr1)):
        result.append(arr1[i]+arr2[i])
    return result

array1=[i for i in range(5)]
array2=[i for i in range(5,10)]
print("First array:", array1)
print("Second array:", array2)
print("Sum of two arrays:", AddArray(array1,array2))