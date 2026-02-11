# try:
#     print(10 / 0)
# except ZeroDivisionError:
#     print("Division by zero is not allowed")


# try:
#     x = int("abc")
# except ValueError:
#     print("Invalid value")


# try:
#     print(10 / 2)
# except ZeroDivisionError:
#     print("Error")
# else:
#     print("Execution successful")


# try:
#     f = open("data.txt")
# except FileNotFoundError:
#     print("File not found")
# finally:
#     print("Program ended")

"""Try with multiple exception block"""
# try:
#     x = int(input("Enter number: "))
#     y = int(input("Enter another number: "))
#     print(x / y)
# except ValueError:
#     print("Please enter only numbers")
# except ZeroDivisionError:
#     print("Division by zero is not allowed")


"""This will cause unreachable code, because Exception catches all exceptions."""
# try:
#     a = 10 / 0
# except Exception:
#     print("General exception")
# except ZeroDivisionError:
#     print("Division error")

"""Multiple Exceptions in One except"""
# try:
#     x = int("abc")
# except (ValueError, TypeError):
#     print("Value or Type error occurred")

"""Using else with Multiple except"""
# try:
#     num = int(input("Enter number: "))
#     print(100 / num)
# except ValueError:
#     print("Invalid input")
# except ZeroDivisionError:
#     print("Cannot divide by zero")
# else:
#     print("Execution successful")



"""raise in Python Exception Handling"""
#syntax : raise ExceptionType("error message")


#Example 1
# age = -5

# if age < 0:
#     raise ValueError("Age cannot be negative")

# print("Valid age")







# num = int(input("Enter a positive number: "))

# if num <= 0:
#     raise ValueError("Number must be positive")

# print("Square:", num*num)







# def divide(a, b):
#     if b == 0:
#         raise ZeroDivisionError("Cannot divide by zero")
#     return a / b

# print(divide(10, 0))






# class InvalidSalaryError(Exception):
#     pass

# class AgeError(Exception):
#     pass

# salary = 2000

# if salary < 5000:
#     raise InvalidSalaryError("Salary below minimum threshold")




# try:
#     marks = int(input("Enter marks: "))
    
#     if marks > 100:
#         raise ValueError("Marks cannot exceed 100")

# except ValueError as e:
#     print("Error:", e)

# print("checking..........")


# try:
#     x = int("abc")
# except ValueError:
#     print("Logging error...")
#     raise   # re-raises same exception


# try:
#     x = int("abc")
# except ValueError:
#     raise TypeError("Conversion failed — wrong type")


# def withdraw(balance, amount):
#     if amount > balance:
#         raise Exception("Insufficient funds")
#     return balance - amount

# withdraw(500,1000)



"""assertion"""
# x = 0
# assert x > 0


# x = -5
# assert x > 0, "x must be positive"


# age = -1
# assert age >= 0, "Age cannot be negative"



# def square_root(x):
#     assert x >= 0, "Input must be non-negative"
#     return x ** 0.5

# print(square_root(-4))



# try:
#     x = -1
#     assert x > 0, "Invalid value"
# except AssertionError as e:
#     print("Assertion failed:",e)

# print("Checking..........")



# items = []
# assert len(items) > 0, "List should not be empty"


for i in range(11):
    assert i < 10
    print(i)


raise ValueError ("Value error")