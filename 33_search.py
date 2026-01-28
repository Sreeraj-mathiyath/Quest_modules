def search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return f"Element {target} found at index {i}"
    return f"Element {target} not found in the array"

array = [i for i in range(20)]
target = 15
print("Array elements:", array)
print(search(array, target))