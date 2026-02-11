# state = 'india'
# pincode = 686514
# distance = 10.5

# print(type(state))
# print(type(pincode))
# print(type(distance))



#arithmetic
"""arithmetic operators"""
# total = num1 + num2
# print("the sum is = ",total)
# print(f"the sum is = {total}")
# print(f"The first number is {num1} and second number is {num2} and their sum is = {total}")
# print(num1 + num2)

# num1 = 20
# num2 = 10
# # print(num2 - num1)
# # print(num1 / num2)
# # print(num1 * num2)
# # print(num1 % num2)
# # print(num1 ** num2)
# # print(num1 // num2)

# num1 = 20
# num2 = 10
# """assihnment operator"""
# # num1 += num2 # num1 = num1 + num2
# # num1 -= num2 # num1 = num1 - num2
# # num1 *= num2
# # num1 /= num2
# # num1 %= num2
# # num1 **= num2
# num1 //= num2
# print(num1)


# name = "ashique"
# # print( "ashique" in name)
# print( "q" not in name)

# num = 17882156
# print(88 in num)

# num1 = 10
# num2 = 10

# print(id(num1))
# print(id(num2))

# print(num1 == num2)
# print(num1 is num2)

# age = int(input("enter your age :"))
# if age >= 18:
#     print("you are eligible for voting")

# elif age <= 0:
#     print("invalid input! please enter a positive value for age")

# else:
#     print("you are not eligible")

# age = 17
# print("eligible for voting" if age >= 18 else "not eligible")

# for var_name in iterable:
#     #body of for loop

# name = "Abhiram"
# phone = 741852963
# for char in name:
#     print(char)

# range(start,stop,step)#50,49,48,47..........
# for i in range(50,0,-2):
#     print(i)


# def greet():
#     print("Hello, Welcome to python programming!")
    
# greet()

# def add(**kwargs):
#     print(kwargs)
#     # total = 0
#     # for i in args:
#     #     total += i
#     # return f"The sum of values is = {total}"

# print(add(num1 = 12,num2 = 18))




# def check_age(age):
#     if age <= 18:
#         return "You are not eligible"
#     return "you are eligible!"
    
# print(check_age(5))


# def get_details(name : str,age : int) -> str:
#     return f"Name :{name}\nage:{age}"

# print(get_details('sree',25))


# """5! = 1*2*3*4*5"""

# def fact(num : int)-> int:
#     if num == 1:
#         return 1
#     return num*fact(num-1)

# number = int(input("Enter a number:"))
# print(fact(number))


# def add(**kwargs):
#     for key,value in kwargs.items():
#         print(key,value)
    

# print(add(f_num = 12, s_num = 18, reminder = 2))


# add = lambda x,y : x+y 

# print(add(10,5))

# upper = lambda name : name.upper()
# print(upper('sreeraj'))


# def square(x):
# 	return x ** 2

# def apply_func(func, value):
# 	 return func(value)

# print(apply_func(square, 5))  




# numbers = [2,5,8,7,9,3,1,7,8,4,6,2,5,1,4]

# # def sq(num):
# #     return num **2

# find_sq = map(lambda x : x**2,numbers)

# print(list(find_sq))



# numbers = [2,5,8,7,9,3,1,7,8,4,6,2,5,1,4]
# even = filter(lambda x : x%2 == 0,numbers)
# print(list(even))













# from functools import reduce
# numbers = [2,5,8,7,9,3,1,7,8,4,6,2,5,1,4]

# total = reduce(lambda x,y: x+y, numbers)
# print(total)


# def Modifier(func):
#     def wrapper(*args, **kwargs):
#         print("Hello welcome to the world of python")
#         result =func(*args, **kwargs)
#         print("Let's enjoy🎲")
#         return result
#     return wrapper


# @Modifier
# def greet(name):
#     return f"Hello {name}"

# print(greet('rahul'))




# number = 123
# print(number + 3)
# print(number * 3)

# name = 'Richu'
# print(name + "S Raj")
# print(name * "3")
# print(name * 3)

# #str+int -> Error
# #str+str -> Concatination
# #str*int -> repatition
# #str*str -> error

name = input("Enter your name:")
age = 24
print("My name is "+ name+" and i'm"+str(age)+"year old")