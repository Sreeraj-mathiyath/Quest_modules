# # # # n=int(input("enter a number"))
# # # # # if n%2!=0:
# # # # #     n+=1
# # # # # for i in range(n,n+10,2):
# # # # #     print(i)
# # # # num=n
# # # # revese=0
# # # # while n>0:
# # # #     last=n%10
# # # #     revese=(revese*10)+last
# # # #     n=n//10
# # # # if num==revese:
# # # #     print("palindrome")
# # # # n = int(input("Enter a number: "))

# # # # def palindrome(n):
# # # #     num=n
# # # #     revrse=0
# # # #     while n>0:
# # # #         last=n%10
# # # #         revrse=(revrse*10)+last
# # # #         n=n//10
# # # #     return num==revrse

# # # # if palindrome(n):
# # # #     print("palindrome")
# # # # else:
# # # #     print("not a palindrome")
# # # #     next=n+1
# # # #     while not palindrome(next):
# # # #         next+=1
# # # #     print(f"the next palindrome number is {next}")


# # # # dict1={"sree":{"name":"sree","age":[23,25]},
# # # #        "unni":{"name":"unni","age":[25]}}

# # # # n=25

# # # # print(dict1["sree"]["age"])


# # # # with open("main.txt","w+") as file:
# # # #     file.write("welcome to python programming!")
# # # #     file.seek(0)
# # # #     print(file.read())
# # # #     print(type(file))
# # # #     print(dir(file))

# # # with open(r"C:\Users\HP\OneDrive\Documents\test\test.txt","r") as file:
# # #     print(file.read())
# # # #r - raw string

# # # words = ['eat','ten','tea','ate','bat','net']

# # # anagram_groups = {}

# # # for word in words:
# # #     key = "".join(sorted(word))
# # #     print(key)
# # #     if key not in anagram_groups:
# # #         anagram_groups[key] = []
# # #     anagram_groups[key].append(word)

# # # result = list(anagram_groups.values())

# # # print(result)

# # # a = [num for num in range(1,11)]
# # # sq_list = [i**2 for i in a]


# # # for i in range(len(a)):
# # #     for j in range(i+1,len(a)):
# # #         result = (a[i]**2)+(a[j]**2)
# # #         if result in sq_list:
# # #             print(f"{a[i]},{a[j]} = {sq_list.index(result)+1}")


# # from tkinter import *

# # # --- COLOR PALETTE ---
# # # Dark Theme Colors for a modern look
# # COLOR_BG_MAIN = "#2E2E2E"       # Main background (Dark Gray)
# # COLOR_ENTRY_BG = "#504444"      # Entry field background (Slightly Lighter Dark Gray/Brown)
# # COLOR_TEXT = "white"            # Text color
# # COLOR_NUM_BTN = "#424242"       # Number button background (Medium Dark Gray)
# # COLOR_OP_BTN = "#FF9500"        # Operator button background (Bright Orange)
# # COLOR_ACTION_BTN = "#A3A3A3"    # Action button background (Light Gray/Silver)
# # COLOR_EQ_BTN = "#FF9500"        # Equal button background (Orange, same as operators for consistency)
# # COLOR_BORDER_FOCUS = "#FFFFFF"  # White border highlight

# # root = Tk()
# # root.title("Calculator")

# # # Set the main background color
# # root.config(bg=COLOR_BG_MAIN) 

# # # Note: The path below is specific to your system. I'll keep it as is.
# # # img = PhotoImage(file=r"D:\Quest\Tkinter\calculator.png") 
# # # root.iconphoto(True,img)

# # root.geometry("300x400")
# # root.resizable(False, False)


# # # --- ENTRY WIDGET STYLING ---
# # e1 = Entry(
# #     root, 
# #     font=("Arial", 24),                      # Changed font to Arial, larger size
# #     fg=COLOR_TEXT, 
# #     bg=COLOR_ENTRY_BG, 
# #     bd=0,                                    # Removed default border for cleaner look
# #     relief="flat",                           # Flat relief
# #     justify="right",
# #     highlightthickness=3,
# #     highlightbackground=COLOR_ENTRY_BG,      # Matches BG for no border when unfocused
# #     highlightcolor=COLOR_BORDER_FOCUS        # White border when focused
# # )
# # # Added internal padding (ipady) to make the display taller
# # e1.grid(column=0, row=0, columnspan=4, padx=5, pady=10, ipady=10, sticky="nsew") 


# # # --- LOGIC FUNCTIONS (Unchanged) ---
# # first_number = None
# # operator = None

# # def btn_click(val):
# #     e1.insert(END, val)

# # def btn_clear():
# #     e1.delete(0, END)

# # def set_operator(op):
# #     global first_number, operator

# #     if op == 'x²':
# #         try:
# #             num = float(e1.get())
# #             e1.delete(0, END)
# #             # Use format string to display result cleanly, removing trailing .0 if integer
# #             result = num ** 2
# #             e1.insert(END, f'{result:g}') 
# #         except:
# #             e1.delete(0, END)
# #             e1.insert(END, "Error")
# #         return
    
# #     try:
# #         # Added check to prevent splitting if an operator is already present
# #         if any(op in e1.get() for op in "+-*/%"):
# #             # Evaluate the current expression before setting a new operator (Chaining)
# #             btn_equal() 

# #         first_number = float(e1.get())
# #         operator = op
# #         e1.insert(END, op)
# #     except ValueError:
# #         e1.delete(0, END)
# #         e1.insert(END, "Error")


# # def btn_equal():
# #     global first_number, operator
# #     try:
# #         expression = e1.get()
        
# #         # Check if the expression contains the operator before splitting
# #         if not operator or operator not in expression:
# #              return # Do nothing if no operator is set

# #         # Use the split result safely
# #         second_num_str = expression.split(operator, 1)[1] # Split only once
# #         second_num = float(second_num_str)

# #         result = None
# #         if operator == "+":
# #             result = first_number + second_num
# #         elif operator == "-":
# #             result = first_number - second_num
# #         elif operator == "*":
# #             result = first_number * second_num
# #         elif operator == "/":
# #             if second_num == 0:
# #                 e1.delete(0, END)
# #                 e1.insert(END, "Error")
# #                 return
# #             result = first_number / second_num
# #         elif operator == "%":
# #             result = first_number % second_num
        
# #         e1.delete(0, END)
# #         # Use format specifier 'g' to prevent displaying trailing zeros unnecessarily
# #         e1.insert(END, f'{result:g}')

# #     except Exception: # Catch any other calculation or parsing error
# #         e1.delete(0, END)
# #         e1.insert(END, "Error")
    
# #     # Reset globals after calculation
# #     first_number = None
# #     operator = None


# # # --- BUTTON LAYOUT AND STYLING ---
# # buttons = [
# #     # text, row, col, type ('num', 'op', 'clear', 'eq')
# #     ('%',   1, 0, 'op'), 
# #     ('x²',  1, 1, 'op'), 
# #     ('C',   1, 2, 'clear'), 
# #     ('/',   1, 3, 'op'), # Changed position of / for better flow
    
# #     ('7',   2, 0, 'num'), ('8',   2, 1, 'num'), ('9',   2, 2, 'num'), ('*',   2, 3, 'op'),
# #     ('4',   3, 0, 'num'), ('5',   3, 1, 'num'), ('6',   3, 2, 'num'), ('-',   3, 3, 'op'),
# #     ('1',   4, 0, 'num'), ('2',   4, 1, 'num'), ('3',   4, 2, 'num'), ('+',   4, 3, 'op'),
# #     ('0',   5, 0, 'num'), ('00',  5, 1, 'num'), ('.',   5, 2, 'num'), ('=',   5, 3, 'eq'),
# # ]

# # # Configure grid to make buttons expand nicely
# # root.grid_columnconfigure((0, 1, 2, 3), weight=1)
# # root.grid_rowconfigure((1, 2, 3, 4, 5), weight=1)

# # for (text, row, col, type) in buttons:
# #     # Base Button Styling
# #     style_args = {
# #         'width': 1, 'height': 1, # Set smaller size since we use grid weights
# #         'font': ("Arial", 16, "bold"),
# #         'fg': COLOR_TEXT,
# #         'bd': 0,
# #         'relief': 'flat',
# #         'activebackground': '#616161' # Darker hover effect
# #     }
    
# #     command_func = None

# #     if type == 'clear':
# #         style_args['bg'] = COLOR_ACTION_BTN
# #         style_args['fg'] = 'black' # Clear button text often stands out
# #         command_func = btn_clear
# #     elif type == 'eq':
# #         style_args['bg'] = COLOR_EQ_BTN
# #         command_func = btn_equal
# #     elif type == 'op':
# #         style_args['bg'] = COLOR_OP_BTN
# #         command_func = lambda t=text: set_operator(t)
# #     else: # type == 'num'
# #         style_args['bg'] = COLOR_NUM_BTN
# #         command_func = lambda t=text: btn_click(t)

# #     Button(root, text=text, command=command_func, **style_args).grid(
# #         row=row, 
# #         column=col, 
# #         padx=5, 
# #         pady=5, 
# #         sticky="nsew" # Important: makes the button fill the grid cell
# #     )

# # root.mainloop()


# # a=10
# # b=10
# # print(a==b)
# # print(a is b)



# # def greet():
# #     print("Hello world")

# # greet()


# # def sum1(*args):
# #     total = 0
# #     for values in args:
# #         total+=values
# #     print(total)

# # sum1(10,20,30,45,15)


# # Write a function power(base, exponent=2). If exponent not given, it should work as square.

# # def power(base,exponent=2):
# #     result = base**exponent
# #     print(result)

# # power(5)
# # power(5,3)

# # Write a function calculate_pay(hours, rate=100) that prints salary.

# # def calculate_pay(hours,rate=100):
# #     salary= hours*rate
# #     print(salary)


# # calculate_pay(8)#8*100
# # calculate_pay(8,120)


# #  Write a function multiply_all(*nums) that returns the product of all values.
# # def multiply_all(*nums):
# #     product = 1
# #     for n in nums:
# #         product*=n
# #     print(product)

# # multiply_all(2,4,1)
# # multiply_all(4,3,5,2)
# # multiply_all(8,8)

# # Write a function count_words(*words) that prints how many words were passed.
# # def count_words(*words):
# #     count=0
# #     for c in words:
# #         count+=1
# #     print(count)

# # count_words('Quest','calicut','python')
# # count_words('adharsh','adhil')



# # def details(**kwargs):
# #     for k,v in kwargs.items():
# #         print(k,v)


# # details(age=20,name='ammu',place='calicut')

# # def check(num):
# #     for i in range(num):
# #         return i
# #     else:
# #         return num

# # print(check(11))


# # set1 = {0,1,True,False}
# # print(set1)
# # #0=False
# # #1=True

# # name = 'quest'

# # def details():
# #     global name
# #     name='sree'
# #     print(name)

# # details()
# # print(name)


# # def factorial(n):
# # 	if n == 1:         # base case
# # 		return 1
# # 	return n * factorial(n - 1)   # recursive call


# # print(factorial(5))
# #5! = 1*2*3*4*5

# #5*factorial(5-1) = 5*factorial(4)
# #4*factorial(4-1) = 4*factorial(3)
# #3*factorial(3-1) = 3*factorial(2)
# #2*factorial(2-1) = 2*factorial(1)


# # def sample(num1,num2,num3):
# #     return num1+num2, num2+num3

# # print(sample(8,4,2))

# # def squ(num):
# #     return num**2


# # square = lambda x,y : x+y
# # print(type(square))

# # print(square(5,3))

# # # s=square(10)
# # # print(s)



# # sqrt = lambda number : number**0.5

# # print(sqrt(16))
# # print(sqrt(36))


# # total = lambda n1,n2,n3 : n1+n2+n3
# # print(total(4,2,7))

# # mark = lambda m : 'pass' if m>60 else 'fail'

# # print(mark(59))

# mark = lambda n1: "even" if n1%2==0 else "odd"

# print(mark(2))









# def my_decorator(fun):
#     def wrapper(name):
#         # print("function execution started")
#         result = fun(name).upper()
#         # print("function execution ended")
#         return result
#     return wrapper



# @my_decorator
# def greet(name):
#     return f"Hello {name}, Welcome!"

# print(greet('adhil'))

# def login_required(test):
#     def wrapper(name):
#         print("checking authentication. please wait.........")
#         print("authentication successfull....")
#         result = test(name)
#         return result

#     return wrapper




# @login_required
# def dashboard(name):
#     return f"welcome to dashboard {name}"

# print(dashboard('ashwathy'))

# def calculate(fun):
#     """this is doc string"""
#     def wrapper(*args):
#         return sum(args)
#     return wrapper

# @calculate
# def numbers(*args):
#     return args

# print(numbers(7,8,9,5,2,5,))

# print(calculate.__doc__)


# 13. Write a function reverse_string(text) that returns the reverse of a string.
#     → Example: "python" → "nohtyp"

# def reverse(text):
#     return text[::-1]

# print(reverse('python'))

# name= 'python'
# print(dir(name))


# def greet():
#     message = "Hello"

#     def show_message():
#         print(message)  # accessing outer variable

#     show_message()

# greet()


# test = 14785 #global scope
# def sample():
#     print(test)
#     num = 7485996 #local scope



# # sample()
# # print(num)


# # num=123
# # print(num)

# # print=456
# # print(print)


# # def calculate(a, b):
# #     return a + b, a * b

# # sum_val, product_val = calculate(4, 5)
# # print(sum_val)        # 9
# # print(product_val)    # 20


# # fruits=['apple','mango','banana','carrot']
# # a,*b, c = fruits
# # print(a)
# # print(b)
# # print(c)


# def before_after(func):
#     def wrapper():
#         print("Before function call")
#         func()
#         print("After function call")
#     return wrapper


# @before_after
# def show_message():
#     print("Function running")


# show_message()


# import mymodule

# mymodule.greet('sree')


# class Calculator:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b

#     def add(self):
#         return self.a + self.b
    
#     def product(self):
#         return self.a * self.b
    
#     def substract(self):
#         return self.a - self.b
    
#     def division(self):
#         return self.a / self.b
    
#     def exponent(self):
#         return self.a ** self.b
    

# num1 = int(input("Enter first number:"))
# num2 = int(input("Enter second number:"))
# operator = int(input("Please select the operation: \n1. + \n2. -\n3. *\n4. /\n5. **\n"))
# calc = Calculator(num1,num2)

# if operator == 1:
#     print(calc.add())
# elif operator == 2:
#     print(calc.substract())
# elif operator == 3:
#     print(calc.product())
# elif operator == 4:
#     print(calc.division())
# elif operator == 5:
#     print(calc.exponent())
# else:
#     print("invalid input")











# name = 'sanika'
# age = 20
# place = 'calicut'
# print("name :",name,"age:", age)
# # print(age)
# # print("name :" + name + " place: " + place + " age: "+age)
# print(f"name : {name}\n age: {age}\n place : {place}")

# phone_number = -74185296
# print(type(phone_number))

# name = "sanika123456@#@###@@💎"
# print(type(name))

# decimal = -10.000
# print(type(decimal))


# class Smartphone:
#     def call(self):
#         print('calling..........')

#     def message(self):
#         print('sending messages..........')

# iphone = Smartphone()#object

# iphone.call()
# iphone.message()

# s24 = Smartphone()
# s24.call()
# s24.message()


# class Animal:
  
#     def eat(self):
#         print('eating...')

#     def run(self):
#         print('running')
    
#     def sleep(self):
#         print('sleeping')

# cat = Animal()
# cat.eat()
# cat.sleep()
# cat.run()
# from datetime import datetime

# class Watch:
#     def check_time(self):
#         return datetime.now()
    
#     def alarm(self):
#         return 'remind me on 3.30PM'
    
#     def change_color(self):
#         return 'changing color to red'
    
# titan = Watch()

# print(titan.check_time())
# print(titan.alarm())
# print(titan.change_color())

# gshock = Watch()
# boat = Watch()
# casio = Watch()



# class car:
#     pass

# def car():
#     pass




# class Employee:
#     def __init__(self,company_name,id,name,position,salary):
#         self.my_company = company_name
#         self.e_id = id
#         self.e_name = name
#         self.post = position
#         self.salay = salary

#     def show_company_name(self):
#         return self.my_company
    
#     def show_details(self):
#         print(f'company name : {self.my_company}\n Employee id : {self.e_id}\n name : {self.e_name}\n Position : {self.post}\n salary: {self.salay}')
    

# adharsh = Employee('Quest',78564,'Adharsh','CEO','22LPA') 

# adharsh.show_details( )




# class Employee:
#     company_name = "quest"#class variable

#     def __init__(self,name,salary):
#         self.name = name#instance variables
#         self.salary = salary

#     def details(self):
#         print(f'{Employee.company_name},{self.name}, {self.salary}')

# adhil = Employee('adhil',150000)

# adhil.details()

# abhay = Employee('abhay',200000)
# abhay.details()
# print(adhil.salary)
# print(adhil.name)
# print(Employee.company_name)



# class Student:

#     college = 'Fathima arts and science' #class variable

#     def __init__(self,id,name,division):
#         self.id = id #instance variable
#         self.name = name #instance variable
#         self.division = division #instance varibale
#         print('created')

#     def details(self):
#         print(f'college : {self.college}\nid: {self.id}\nname: {self.name}\ndivision: {self.division}')

#     def study(self):
#         print('study......')

#     def play(self):
#         print('palying........')

#     def __del__(self):
#         print('deleted')

# sree = Student(123,'sree','a')

# ashwathy = Student(1234,'ashwathy','C')
# ashwathy.details()
# del ashwathy
# print(ashwathy.details())

# del Student.college
# print(Student.college)


# vishag = Student(7854,'vishag','A')
# print(vishag.college)
# print(vishag.name)

# vishag.college = 'Royal arts and science college'
# vishag.name = 'visakh'
# print(vishag.college)
# print(vishag.name)


# print(Student.college)
# Student.college = 'Royal arts and science college'
# print(Student.college)

# abhin = Student(7412,'Abhin','B') 
# print(abhin.details())
# del abhin.name
# print(abhin.name)

# print(abhin.id)
# del abhin.id
# print(abhin.id)
  
# print(abhin.college)
# abhin.college = 'jems arts and science'
# # print(abhin.college)
# del abhin.college
# print(abhin.college)


# class Aswathy:
#     def __init__(self,name,age,height):
#         self.name = name
#         self.age = age
#         self.height = height

#     def details(self):
#         print(self.name)
#         print(self.age)
#         print(self.height)
    
# a1 = Aswathy('aswathy',21,160)
# a1.details()




# class Bank:
#     bank_name = 'HDFC'

#     def __init__(self,name,account_number,address,phone,balance=0):
#         self.name = name
#         self.account_number = account_number
#         self.address = address
#         self.phone = phone
#         self.balance = balance

#     def get_details(self):
#         return f'bank: {self.bank_name} {Bank.bank_name}name : {self.name}\naccount_number : {self.account_number}\naddress : {self.address}\nphone :{self.phone}\nbalance :{self.balance}'
    
#     def deposit(self,amount):
#         self.balance += amount
#         print(f'deposit successful, current balance is {self.balance}')

#     def withdraw(self,amount):
#         if amount > self.balance:
#             print('insufficient balance!')
#         else:
#             self.balance -= amount #self.balance = self.balance - amount
#             print(f'Transaction successfull. current balance is {self.balance}')

#     def check_balance(self):
#         print(f'current balance is {self.balance}')

# sreeraj = Bank('sreeraj',1023648577,'mathiyath',6238967951,7500)

# print(getattr(sreeraj,'address'))
# print(getattr(sreeraj,'phone'))


# print(hasattr(sreeraj,'age'))
# print(hasattr(sreeraj,'phone'))

# print(setattr(sreeraj,'age',24))
# print(sreeraj.age)

# delattr(sreeraj,'age')
# sreeraj.age

# class GrandParent:
#     pass

# class Parent(GrandParent):
#     def __init__(self,name):
#         self.name = name
        
#     def job(self):
#         return 'software engineer'
    
# class Child(Parent):
#     def passion(self):
#         return 'Social media influencer'

# class GrandChild(Child):
#     pass

# GC = GrandChild('ammu')
# print(GC.passion())
# print(GC.job())



# class Father:
#     pass

# class Mother:
#     pass

# class Child(Father, Mother):
#     pass


# class Parent:
#     def residency(self):
#         return 'Kerala'

# class Child1(Parent):
#     def study(self):
#         return 'Canada'

# class Child2(Parent):
#     def job(self):
#         return 'Nurse'
    

# c1 = Child1()
# c2 = Child2()

# print(c1.residency())
# print(c2.residency())



# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def show_details(self):
#         print("Name:", self.name)
#         print("Age:", self.age)

#     def role(self):
#         print("Role: Person")


# class Student(Person):
#     def __init__(self, name, age, student_id):
#         # Calling parent class constructor
#         super().__init__(name, age)
#         self.student_id = student_id 

#     def show_student_details(self):
#         print("Student ID:", self.student_id)

#     # Method overriding
#     def role(self):
#         print("Role: Student")


# student1 = Student("Rahul", 20, "STU101")
# student1.show_details()       # Inherited from Person
# student1.show_student_details()
# student1.role()               # Overridden method




# class Animal:
#     def __init__(self, food):
#         self.food = food
#         print("Animal constructor called")

#     def eat(self):
#         print("Animal eats", self.food)

#     def type(self):
#         print("Type: Animal")


# class Pet(Animal):
#     def __init__(self, food, name):
#         super().__init__(food)   # Call Animal constructor
#         self.name = name
#         print("Pet constructor called")

#     def play(self):
#         print(self.name, "likes to play")

#     # Method overriding
#     def type(self):
#         print("Type: Pet")

# class Cat(Pet):
#     def __init__(self, food, name, color):
#         super().__init__(food, name)  # Call Pet constructor
#         self.color = color
#         print("Cat constructor called")

#     def sound(self):
#         print("Cat says Meow")

#     # Method overriding
#     def type(self):
#         return super().type()



# c = Cat("Fish", "Kitty", "White")
# c.eat()       # From Animal
# c.play()      # From Pet
# c.sound()     # From Cat
# c.type()      # Overridden method


# # Accessing Variables from Parent Classes
# print("Food:", c.food)     # From Animal
# print("Name:", c.name)     # From Pet
# print("Color:", c.color)   # From Cat

# # # Checking Object Relationship
# print(isinstance(c, Cat))     # True
# print(isinstance(c, Pet))     # True
# print(isinstance(c, Animal))  # True
 


# class Phone:
#     def call(self):
#         print("Making a phone call")

#     def message(self):
#         print("Sending a message")


# class Camera:
#     def take_photo(self):
#         print("Taking a photo")

#     def record_video(self):
#         print("Recording a video")


# class SmartPhone(Phone, Camera):   # Multiple Inheritance
#     def browse_internet(self):
#         print("Browsing the internet")


# # Object creation
# my_phone = SmartPhone()

# # Accessing methods from both parent classes
# my_phone.call()
# my_phone.message()
# my_phone.take_photo()
# my_phone.record_video()
# my_phone.browse_internet()






# class ElectricVehicle:
#     def __init__(self, battery_capacity):
#         self.battery_capacity = battery_capacity
#         print("ElectricVehicle initialized")

#     def charge(self):
#         print("Charging the electric vehicle")

#     def start(self):
#         print("Electric vehicle is starting")


# class AutonomousSystem:
#     def __init__(self, sensor_count):
#         self.sensor_count = sensor_count
#         print("AutonomousSystem initialized")

#     def self_drive(self):
#         print("Autonomous driving mode activated")

#     def start(self):
#         print("Autonomous system is starting")


# class SmartElectricCar(ElectricVehicle, AutonomousSystem): 
#     def __init__(self, battery_capacity, sensor_count, brand):
#         # Calling parent constructors explicitly
#         ElectricVehicle.__init__(self, battery_capacity)
#         AutonomousSystem.__init__(self, sensor_count)

#         self.brand = brand
#         print("SmartElectricCar initialized")

#     def start(self):
#         print(f"{self.brand} Smart Electric Car is starting with AI support")

# car = SmartElectricCar(75, 12, "Tesla")
# car.charge()         # from ElectricVehicle
# car.self_drive()     # from AutonomousSystem
# car.start()          # overridden method


# print(SmartElectricCar.mro())




# Parent Class
# class Vehicle:
#     def __init__(self, brand):
#         self.brand = brand

#     def start(self):
#         print(f"{self.brand} vehicle is starting")

#     def stop(self):
#         print("Vehicle stopped")


# # Child Class 1
# class Car(Vehicle):
#     def drive(self):
#         print("Car is driving on the road")


# # Child Class 2
# class Bike(Vehicle):
#     def ride(self):
#         print("Bike is riding on the road")


# # Child Class 3
# class Truck(Vehicle):
#     def load_goods(self):
#         print("Truck is loading goods")





# class Employee:
#     def __init__(self, name, emp_id, salary):
#         self.name = name
#         self.emp_id = emp_id
#         self.salary = salary

#     def work(self):
#         print("Employee is working")

#     def get_details(self):
#         print(f"Name: {self.name}")
#         print(f"ID: {self.emp_id}")
#         print(f"Salary: {self.salary}")


# class Developer(Employee):
#     def __init__(self, name, emp_id, salary, programming_language):
#         super().__init__(name, emp_id, salary)
#         self.programming_language = programming_language

#     def work(self):
#         print("Developer is writing code")

#     def show_skill(self):
#         print(f"Programming Language: {self.programming_language}")


# class Tester(Employee):
#     def __init__(self, name, emp_id, salary, testing_tool):
#         super().__init__(name, emp_id, salary)
#         self.testing_tool = testing_tool

#     def work(self):
#         print("Tester is testing the application")

#     def show_tool(self):
#         print(f"Testing Tool: {self.testing_tool}")


# class Manager(Employee):
#     def __init__(self, name, emp_id, salary, team_size):
#         super().__init__(name, emp_id, salary)
#         self.team_size = team_size

#     def work(self):
#         print("Manager is managing the team")

#     def show_team(self):
#         print(f"Team Size: {self.team_size}")


# dev = Developer("Alice", 101, 60000, "Python")
# tester = Tester("Bob", 102, 50000, "Selenium")
# manager = Manager("Charlie", 103, 80000, 10)



# dev.get_details()
# dev.work()
# dev.show_skill()

# print()

# tester.get_details()
# tester.work()
# tester.show_tool()

# print()

# manager.get_details()
# manager.work()
# manager.show_team()





   








# # Base Class (Single Inheritance Base)
# class User:
#     def __init__(self, name):
#         self.name = name

#     def login(self):
#         print(f"{self.name} logged in")

# # Hierarchical Inheritance (Multiple Children)
# class Student(User):
#     def __init__(self, name, course):
#         super().__init__(name)
#         self.course = course

#     def study(self):
#         print(f"{self.name} is studying {self.course}")

# class Instructor(User):
#     def __init__(self, name, subject):
#         super().__init__(name)
#         self.subject = subject

#     def teach(self):
#         print(f"{self.name} is teaching {self.subject}")

# # Multiple Inheritance (Hybrid Part)
# class TeachingAssistant(Student, Instructor):
#     def __init__(self, name, course, subject):
#         Student.__init__(self, name, course)
#         Instructor.__init__(self, name, subject)

#     def assist(self):
#         print(f"{self.name} is assisting students and instructors")


# ta = TeachingAssistant("Alex", "Python", "Programming")

# ta.login()      # from User
# ta.study()      # from Student
# ta.teach()      # from Instructor
# ta.assist()     # from TeachingAssistant




# # Method Overriding (Most Important)
# class Animal:
#     def sound(self):
#         print("Animal makes sound")

# class Dog(Animal):
#     def sound(self):
#         print("Dog barks")

# class Cat(Animal):
#     def sound(self):
#         print("Cat meows")

# # Objects
# a = Animal()
# d = Dog()
# c = Cat()

# a.sound()
# d.sound()
# c.sound()




# # # Operator Polymorphism (Operator Overloading)
# print(5 * 3)        # Addition
# print("Hello " + "World")   # String join
# print([1,2] * [3,4])   # List merge


# # # Function Polymorphism (Built-in Functions)
# print(len("Python"))
# print(len([1,2,3,4]))
# print(len({"a":1, "b":2}))


# # # Custom Function Polymorphism
# def add(a, b):
#     return a + b

# print(add(10, 20))
# print(add("Hi ", "There"))
# print(add([1,2], [3,4]))


"""Operator Overloading means giving additional meaning to an operator depending on the operands (data types).

Same operator
 Different behavior
Based on object or data type"""

# class Student:
#     def __init__(self, marks):
#         self.marks = marks

#     def __add__(self, other):
#         print(other.marks)
#         return self.marks + other.marks   

# s1 = Student(80)
# s2 = Student(90)
# print(s2+s1 )


"""In Python, true operator overloading is ONLY possible using magic methods (__add__, __sub__, etc).

Without magic methods, you cannot change how operators like +, -, * work for custom objects."""




# class Calc:
#     # def __init__(self,num1,num2,num3):
#     #     self.num1 = num1
#     #     self.num2 = num2
#     #     self.num3 = num3

#     def add(self,num1,num2):
#         return num1 + num2
    
#     def add(self,num1,num2,num3):
#         return num1 + num2 + num3


# c = Calc()
# print(c.add(2,5,5))




class Payment:
    def __init__(self, amount):
        self.amount = amount

    def process_payment(self):
        print("Processing generic payment")

    def payment_receipt(self):
        print(f"Payment of {self.amount} completed")


class UPI(Payment):
    def process_payment(self):
        print(f"Processing UPI payment of {self.amount}")

gpay = UPI(1000)
gpay.process_payment() 



class Card(Payment):
    def process_payment(self):
        super().process_payment()
        print(f"Processing Card payment of {self.amount}")


