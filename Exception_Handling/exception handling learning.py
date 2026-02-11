#=========================Error==============================

#SyntaxError
# print("hello"

# d1 ={'a':,'b':,'c'}


#indentationError
    # print("hello")

# for i in range(1,10):
# print(i)


#tab Error
# def add():
#     print("Start")   # 4 spaces before print
# \tprint("End")       # 1 tab before print

#===================Exceptions==============================

#zerodivision error
# a=10
# b=0
# print(a/b)

#Value error

num = int("Hello")
print(num)

#type error
# string ="quest"
# print(string+20)

#indexerror
# numbers=[1,2,3,4,5]
# print(numbers[10])

#KeyError
# student = {"name": "John", "age": 20}
# print(student["grade"])

# #FileNotFoundError
# open("abc.txt")

# #nameError
# print(x)

# #AttributeError
# text = "Hello"
# # print(text.uppercase())
# print(text.sort())

# #Importerror
# import quest_module




#=========================Exception Handling================================
# a=10
# b=0
# try:
#     print(a/b)
# except ZeroDivisionError:
#     print("Can't divisible a number by zero!")



# def check(age):
#     if age < 18:
#         raise ValueError("Not eligible")
# try:
#     check(15)
# except Exception as e:
#     print(e)

# try:
#     num = int(input("Enter a number: "))
# except ValueError:
#     print("Invalid input! Please enter a number.")
# else:
#     print("You entered:", num)
# finally:
#     print("Program finished.")


# def withdraw(amount):
#     balance = 450

#     if amount>balance:
#         raise ValueError("Insufficient balance!")
        
#     print(f"amount withdrwan {amount}")

# withdraw(500)

# def withdraw(amount):
#     if amount <= 0:
#         raise ValueError("Withdrawal amount must be greater than 0")
#     print("Amount withdrawn:", amount)

# withdraw(-100)


#======================assertion=================================
# marks = 110
# assert marks <= 100, "Marks cannot be more than 100"
# print("Result processed")

#Write an assertion to check that a number entered by a user must be positive.

# number = int(input("Enter a number : "))
# assert number>0,"Number must be positive!"
# print("input Successfully...")


#Add an assertion in the function to ensure that age is between 1 and 120.
# def validate(age):
#     assert 120>age>=1,"Invalid age input, age must between 1-120."
#     print("valid age")

# age = int(input("Enter your age:"))
# validate(age)

#Add an assertion to ensure that the list has at least one element.
# items = [1,2,3]
# assert len(items)>0,"list must contain atleast one element!"
# print("Validated")


# Q9

# Write a program that reads a number and asserts that it is even.

# Q10

# Write a program using a function to calculate factorial and assert that input should be an integer and non-negative.

# Q11

# Write a program to input username and assert that it should not be blank.

# Q12

# Write a program that asks for a password and uses assert to ensure it is at least 8 characters long.

# Real-Life Scenario
# Q13

# A shopping cart should never have a negative quantity.
# Write an assertion for this in code.


#===================custom exceptions======================================
# class AgeError(Exception):
#     pass

# age = -5
# if age <0 :
#     raise AgeError("age cannot be negative!")

# class AgeError(Exception):
#     pass

# try:
#     age = int(input("Enter age: "))
#     if age < 0:
#         raise AgeError("Age cannot be negative")
#     print("Valid age:", age)
# except AgeError as e:
#     print("Error:", e)


# class PasswordError(Exception):
#     def __init__(self, message, length):
#         self.message = message
#         self.length = length
#         super().__init__(message)


# password ="abc"
# try:
#     if len(password) < 8:
#         raise PasswordError("Password too short", len(password))
# except PasswordError as e:
#     print(e.message, "Length entered:", e.length)
