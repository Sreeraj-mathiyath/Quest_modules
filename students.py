# number = 500

# def largest(*nums):
#     global number
#     number +=500
#     v=nums[0]
#     for i in nums:
#         if v<i:
#             v=i
#     return v
# fun = largest(-5,-50,-100,-110,15)
# print(type(fun))







# def square(x):
# 	return x * x

# print(square(5))

# def apply_func(func, value):
# 	 return func(value) #square(5)

# print(apply_func(square, 5))   

# def upper(word):
#     return word.upper()

# def to_upper(fun, w):
#     return fun(w) # upper(quest)

# print(to_upper(upper,'quest'))

# s = 'sample test'
# for i in s:
#     print(i)

#syntax map(fun, iterable)

# numbers = [1,2,3,4,5,6,7,8,9,10]
# even = [x for x in numbers if x%2==0]
# print(even)

# def square(number):
#     if number%2==0:
#         return number**2
#     else:
#         return number

# result = map(square, numbers)
# print(list(result))

# list1 = [11,12,13]
# list2 = [22,33,44]
# total = map(lambda x,y:x+y, list1,list2)
# print(list(total))

# numbers = [1,2,3,4,5,6,7,8,9,10]
# # even = filter(lambda x:x%2==0, numbers)
# # print(list(even))

# result = list(filter(lambda x: 3<x<9, numbers))
# print(result)

#multiple of 3 and find the cube of those numbers
# nums = [1,3,6,5,4,2]
# result = map(lambda x : x**3,list(filter(lambda x : x%3==0,nums))) #map(fun,itr) #[3,6] -> [27,216]
# print(list(result))

#

# def prime(number):
#     if number<2:
#         return "Not prime"
    
#     for i in range(2,number):
#         if number%i==0:
#             return "Not prime"
#         else:
#             return "prime"
        
# print(prime(50))


def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

print(fact(5))



from functools import reduce
numbers = [4,78,578,5]
result = reduce(lambda x, y : x*y,numbers)

print(result)

#4+78=82
#82+578= 660
#660+5=665