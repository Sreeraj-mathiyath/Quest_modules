def largest(num1,num2,num3):
    if num1> num2 and num1>num3:
        return f"the largest number is {num1}"
    elif num1<num2 and num2>num3:
        return f"the largest number is {num2}"
    else:
        return f"the largest nuber is {num3}"
    

print(largest(120,25,180))