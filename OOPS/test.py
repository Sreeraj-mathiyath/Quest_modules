#define a class
# class MyClass:
#     pass

# object1 = MyClass()
# print(object1)

#class with methods
# class Greet:
#     def greet(self):
#         print("Welcome to OOPs programming!")

# greet_object = Greet()
# greet_object.greet()

#class with attributes
class Employee:
    company_name = "Quest"

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def get_details(self):
        print(f"Company name : {self.company_name}\nName of the employee : {self.name}\nSalary : {self.salary}")


emp1 = Employee('sreeraj',15000)
emp1.get_details()
emp1.company_name = "qis"
emp1.get_details()
del emp1.company_name
print(hasattr(emp1,'company_name'))
del emp1.company_name
# print(Employee.company_name)
# print(emp1.company_name)

