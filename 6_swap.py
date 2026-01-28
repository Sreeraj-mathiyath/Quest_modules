def swap(num1,num2):
    num1,num2=num2,num1
    return f" After swapping First number is {num1} and second number is {num2}"

num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
print(swap(num1,num2))

a=10
b=20
temp=a
a=b
b=temp
print(f" After swapping First number is {a} and second number is {b}")

