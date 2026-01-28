# # def greet():
# #     print("Hello, World!")

# # greet()

# # def hello():
# #     return "Hello from the hello function!"

# # hello()
# # h = hello()
# # print(hello())
# # print(h)

# # #postional arguments
# # def details(name, age):
# #     print("Name:", name)
# #     print("Age:", age)

# # details("Alice", 30)
# # details(25, "Bob")

# # #keyword arguments
# # def details(name, age):
# #     print("Name:", name)
# #     print("Age:", age)

# # details(age=30, name="Alice")

# #default arguments
# def details(name, age=25):
#     print("Name:", name)
#     print("Age:", age)

# details("Alice")
# details("Bob", 30)

# #variable-length arguments
# def sum(a,b,c):
#     return a + b + c

# print(sum(1,2,3))
# # print(sum(10,20))
# # print(sum(4,5,6,7,8))  # This will raise an error


# def sum_all(*args):
#     total = 0
#     for num in args:
#         total += num
#     return total

# print(sum_all(1,2,3))
# print(sum_all(10,20))
# print(sum_all(4,5,6,7,8))


# #keyword variable-length arguments
# def print_info(**kwargs):
#     print(kwargs)

# print_info(name="Alice", age=30, city="New York")

# def print_info(**info):
#     for key, value in info.items():
#         print(f"{key}: {value}")

# print_info(name="Bob", age=25, country="USA")
# print_info(job="Engineer", company="TechCorp")



# x = 10
# def modify():
#     x=20
#     return x

# print(modify())
# print(x)

# x = 10
# def modify():
#     global x
#     x+=30
#     return x

# print(modify())
# print(x)

#FUNCTION SCOPE
#1. LOCAL SCOPE
# def my_func():
#     x = 100      # local variable
#     print(x)     # → 100

# my_func()
# print(x)         # NameError: name 'x' is not defined

#2. ENCLOSING SCOPE
# def outer():
#     y = 200                  # enclosing scope

#     def inner():
#         print(y)             # inner can see outer's y → 200

#     inner()

# outer()

#3. Global Scope
# z = 300                      # global

# def func():
#     print(z)               # can read global z → 300

# func()
# print(z)                     # → 300

# x = 10

# def change():
#     global x
#     x = 20
#     print(x)

# change()
# print(x)

# 5. Using nonlocal keyword

# Used inside nested functions to modify the variable of the outer function.

# def outer():
#     x = 10
#     def inner():
#         nonlocal x
#         x = 20
#     inner()
#     print(x)


# 4. Built-in Scope
# len = 999                    # shadows built-in len in global scope

# def my_func():
#     print(len([1,2,3]))      # NameError or uses global 999, not built-in

# NUMBERS : list[int]=[1,2,3,]
# print(NUMBERS)