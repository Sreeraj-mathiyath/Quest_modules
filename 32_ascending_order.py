def sort(arr):
    sorted_arr=sorted(arr)
    print(f"the inputed array is :{arr}")
    return f"Array in ascending order :{sorted_arr}"


array=[i for i in range(10,0,-1)]
print(sort(array)) 