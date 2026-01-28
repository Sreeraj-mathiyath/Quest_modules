# def fact(n):
#     if n<1:
#         return 0
#     else:
#         factorial=1
#         for i in range(1,n+1):
#             factorial*=i
#     return factorial


# number=int(input("Enter a number: "))
# print(f"The factorial of the number is {fact(number)}")


list1 = ['a','b','c',1,2,334,4,4,4]
for i in list1:
    if isinstance(i,int):
        print(i)