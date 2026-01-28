def difference(num1,num2):
    try:
        return num1 - num2
    except Exception as e:
        print(e)


num1=int(input("enter the first number: "))
num2=int(input("enter the second number: "))
print(difference(num1,num2))