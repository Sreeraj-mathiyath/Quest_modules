# # # # # class Student:
# # # # #     name = "sreeraj"
# # # # #     trainer = "shari"

# # # # #     def display_details(self):
# # # # #         print(f"Name is {self.name} and trainer is {self.trainer}")

# # # # # s1 = Student()
# # # # # s1.display_details()

# # # # class Humen:
# # # #     legs=2
# # # #     eyes=2

# # # #     def __init__(self,n):
# # # #         self.name=n

# # # #     def walk(self):
# # # #         print(self.name,'can walk',self.eyes)
    
# # # #     def talk(m):
# # # #         print(m.name,'can talk',m.eyes)   

# # # # anu=Humen("ANU THOMAS")
# # # # # ram=Humen()

# # # # print(id(anu))
# # # # # print(id(ram))
# # # # # print(anu.eyes)       
# # # # # ram=Humen()
# # # # # print(ram.eyes)  
# # # # # print("///////////////////////")
# # # # # anu.eyes=1
# # # # # print(anu.eyes)       
# # # # # print(ram.eyes)

# # # # anu.talk()
# # # # anu.walk()


# # # # class MyClass:
# # # #     pass

# # # class Student:
# # #     name = 'sreeraj'
# # #     mark = '100'

# # # sreeraj = Student
# # # print(sreeraj.name)
# # # print(sreeraj.mark)

# # # shari = Student
# # # print(shari.name)
# # # print(shari.mark)





















# # class Student:
# #     name='Shari'
# #     mark = 30

# #     def get_name():
# #         print(f"Student name is {Student.name}")

# # student1= Student
# # print(Student.name)


# # student1.get_name()

# # # student1.mark = 100
# # # print(student1.mark)

# # # student2 = Student
# # # print(student2.name)
# # # print(student2.mark)

# # # print(id(student1))
# # # print(id(student2))

# # student3 = Student()
# # print(student3.name)
# # print(student3.mark)
# # student3.mark=100
# # print(student3.mark)

# # student4 = Student()
# # print(student4.name)
# # print(student4.mark)

# # print(id(student3))
# # print(id(student4))


# class Human:
#     legs= 2
#     eyes = 2
#     name = 'sreeraj'

#     def __init__(self,name):
#         self.n = name

        
# class Employee:
#     def __init__(self):
#         print("Constructor activated")

# sree = Employee()
# shari = Employee()




# class Animal:
#     def eat(self):
#         print("Animal can eat")

# class Dog(Animal):
#     def bark(self):
#         print("Dog can bark")

# d = Dog()
# d.eat()    # inherited from Animal
# d.bark()   # own method


# class Vehicle:
#     def start(self):
#         print("vehicle is started")

# class Car(Vehicle):
#     def drive(self):
#         print("driving.....")

# toyota = Car()
# toyota.drive()
# toyota.start()


# class Grandfather:
#     def house(self):
#         print("Grandfather has a house")

# class Father(Grandfather):
#     def car(self):
#         print("Father has a car")

# class Son(Father):
#     def bike(self):
#         print("Son has a bike")

# s = Son()
# s.house()   # from Grandfather
# s.car()     # from Father  
# s.bike()    # own method



# class Device:
#     def power_on(self):
#         print("Device is powered on")

# class Mobile(Device):
#     def call(self):
#         print("Calling...")

# class SmartPhone(Mobile):
#     def internet(self):
#         print("Using internet...")

# sp = SmartPhone()
# sp.power_on()
# sp.call()
# sp.internet()


# class Person:
#     def __init__(self, name):
#         self.name = name

#     def show(self):
#         print("Name:", self.name)

# class Student(Person):
#     def __init__(self, name, roll):
#         super().__init__(name)   # call parent constructor
#         self.roll = roll

#     def display(self):
#         print("Name:", self.name)
#         print("Roll No:", self.roll)

# s = Student("Anu", 101)
# s.display()




# class Father:
#     def skills(self):
#         print("Gardening")

# class Mother:
#     def skills(self):
#         print("Cooking")

# class Child(Father, Mother):
#     pass

# c = Child()
# c.skills()

# #Method Overriding (Important Concept)
# class Animal:
#     def sound(self):
#         print("Animal makes a sound")

# class Dog(Animal):
#     def sound(self):
#         print("Dog barks")

# d = Dog()
# d.sound()

# #Using super() in Method Overriding
# class Animal:
#     def sound(self):
#         print("Animal sound")

# class Dog(Animal):
#     def sound(self):
#         super().sound()
#         print("Dog barks")

# d = Dog()
# d.sound()

# class Father:
#     def father_skill(self):
#         print("Father can drive")

# class Mother:
#     def mother_skill(self):
#         print("Mother can cook")

# class Child(Father, Mother):
#     def child_skill(self):
#         print("Child can study")



# c = Child()
# c.father_skill()
# c.mother_skill()
# c.child_skill()



# class Camera:
#     def take_photo(self):
#         print("Photo taken")

# class Phone:
#     def call(self):
#         print("Calling...")

# class SmartPhone(Camera, Phone):
#     passv   

# s = SmartPhone()
# s.take_photo()
# s.call()

# class Employee:
#     def work(self):
#         print("Employee works")

# class Developer(Employee):
#     def code(self):
#         print("Developer writes code")

# class Tester(Employee):
#     def test(self):
#         print("Tester tests software")

# dev = Developer()
# dev.work()
# dev.code()


# test = Tester()
# test.work()
# test.test()




# class A:
#     def showA(self):
#         print("Class A")

# class B(A):
#     def showB(self):
#         print("Class B")

# class C(A):
#     def showC(self):
#         print("Class C")

# class D(B, C):
#     def showD(self):
#         print("Class D")

# obj = D()
# obj.showA()
# obj.showB()
# obj.showC()
# obj.showD()









# class Device:
#     def power(self):
#         print("Device powered on")

# class Phone(Device):
#     def call(self):
#         print("Calling...")

# class Camera(Device):
#     def photo(self):
#         print("Taking photo")

# class SmartPhone(Phone, Camera):
#     def internet(self):
#         print("Using internet")

# sp = SmartPhone()
# sp.power()
# sp.call()
# sp.photo()
# sp.internet()


