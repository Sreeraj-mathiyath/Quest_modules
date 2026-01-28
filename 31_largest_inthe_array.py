def largest(arr):
    sorted_arr=sorted(arr,reverse=True)
    print(f"the inputed array is :{arr}")
    return f"Largest element in the array is :{sorted_arr[0]}"


array=[i for i in range(1,50,4)]
print(largest(array))