# import Modules.math

# print("Addition:", Modules.math.add(10, 5))
# print("Subtraction:", Modules.math.subtract(10, 5))
# print("Multiplication:", Modules.math.multiply(10, 5))
# print("Division:", Modules.math.divide(10, 5))


# from Modules.math import add, subtract, multiply, divide

# print("Addition:", add(10, 5))
# print("Subtraction:", subtract(10, 5))
# print("Multiplication:", multiply(10, 5))
# print("Division:", divide(10, 5))

# import Modules.math as m

# print("Addition (using alias):", m.add(20, 10))
# print("Subtraction (using alias):", m.subtract(20, 10))
# print("Multiplication (using alias):", m.multiply(20, 10))
# print("Division (using alias):", m.divide(20, 10))


# from math import * 
# print(dir()) # Lists all names in the current local scope, including imported ones
# print("Square Root of 16 :", sqrt(16))  # Using sqrt from math module
# print("Value of Pi :", pi)  # Using pi from math module
# print("Value of e :", e)  # Using e from math module
# print("celling of 4.2 :", ceil(4.2))  # Using ceil from math module
# print("floor of 4.7 :", floor(4.7))  # Using floor from math module
# print("factorial of 5 :", factorial(5))  # Using factorial from math module
# print("remainder of 10/3 :", remainder(10, 3))  # Using fmod from math module
# print("cosine of 60 degrees :", cos(radians(60)))  # Using cos and radians from math module
# print("tangent of 45 degrees :", tan(radians(45)))  # Using tan and radians from math module
 
# from datetime import *
  
# print("Current Date and Time :", datetime.now())  # Current date and time
# print("Current Year :", datetime.now().year)  # Current year
# print("Current Month :", datetime.now().month)  # Current month
# print("Current Day :", datetime.now().day)  # Current day
# print("Current Time :", datetime.now().time())  # Current time
# print("Current Hour :", datetime.now().hour)  # Current hour
# print("Current Minute :", datetime.now().minute)  # Current minute
# print("Current Second :", datetime.now().second)  # Current second
# print("Current Microsecond :", datetime.now().microsecond)  # Current microsecond
# print("Today's Date :", date.today())  # Today's date


# dt = datetime.now()
# print(dt)


# print("%Y  ->", dt.strftime("%Y"))   # Year, full
# print("%y  ->", dt.strftime("%y"))   # Year, short
# print("%m  ->", dt.strftime("%m"))   # Month number
# print("%B  ->", dt.strftime("%B"))   # Month name (full)
# print("%b  ->", dt.strftime("%b"))   # Month name (abbr)
# print("%d  ->", dt.strftime("%d"))   # Day of month
# print("%A  ->", dt.strftime("%A"))   # Weekday name (full)
# print("%a  ->", dt.strftime("%a"))   # Weekday name (abbr)
# print("%H  ->", dt.strftime("%H"))   # Hour (24-hour)
# print("%I  ->", dt.strftime("%I"))   # Hour (12-hour)
# print("%p  ->", dt.strftime("%p"))   # AM/PM
# print("%M  ->", dt.strftime("%M"))   # Minute
# print("%S  ->", dt.strftime("%S"))   # Second
# print("%f  ->", dt.strftime("%f"))   # Microsecond
# print("%z  ->", dt.strftime("%z"))   # UTC offset
# print("%Z  ->", dt.strftime("%Z"))   # Timezone name
# print("%j  ->", dt.strftime("%j"))   # Day of year
# print("%U  ->", dt.strftime("%U"))   # Week number (Sunday first)
# print("%W  ->", dt.strftime("%W"))   # Week number (Monday first)
# print("%c  ->", dt.strftime("%c"))   # Locale’s date and time
# print("%x  ->", dt.strftime("%x"))   # Locale’s date
# print("%X  ->", dt.strftime("%X"))   # Locale’s time


# today = datetime.today()
# after_7days = today - timedelta(days=7)
# # print(after_7days)

# time_after_2 = today + timedelta(hours=2, minutes=15)
# # print(time_after_2)

# after = datetime.now()
# print(after)

# dob = date(2001, 9, 25)
# today = date.today()

# age_days = today - dob
# print("Age in days:", age_days.days)


# d1 = date(2025, 1, 1)
# d2 = date(2025, 1, 15)

# difference = d2 - d1
# print("Difference:", difference)
# print("Days:", difference.days)

# start_date = date.today()
# expiry_date = start_date + timedelta(days=30)

# print("Start Date:", start_date)
# print("Expiry Date:", expiry_date)





from random import *
# print(random())
# print(randint(1,10))

# print(uniform(1,100))
# print(randrange(2,100,6)) #2,8,14,20,26
# print(randrange(3,100,5)) #3,8,13,18,23
# fruits = ['apple','mango','banana','grapes','cherry','avacado','papaya']
# print(choice(fruits))

# sample_set = {1,2,3,4,5,6}
# print(choice(sample_set)) #error

# sample_tuple = (7,8,9,4,5,6,1)
# print(choice(sample_tuple))

# name = 'PYTHON'
# print(choice(name))

# num = range(1,100)
# print(choice(num))

# dict1 = {'name':'quest','phone':789965412}
# print(choice(dict1))#error

# fruits = ['apple','mango','banana','grapes','cherry','avacado','papaya']
# print(choices(fruits,k=4))

fruits = ['apple','jack fruits','mango','banana','grapes','cherry','avacado','papaya']
shuffle(fruits)
print(fruits)

  
   

# print("Random Float between 0 and 1 :", random())  # Random float between 0 and 1
# print("Random Float between 1 and 10 :", uniform(1, 10))  # Random float between 1 and 10
# print("Random Integer between 1 and 100 :", randint(1, 100))
# print("Random Choice from List :", choice(['apple', 'banana', 'cherry', 'date']))  # Random choice from a list
# print("Random Sample of 3 from List :", sample(['apple', 'banana', 'cherry', 'date', 'elderberry'], 3))  # Random sample of 3 from a list
# print("Shuffling List :", end=" ")
# my_list = ['apple', 'banana', 'cherry', 'date']
# shuffle(my_list)
# print(my_list)  # Shuffled list
# print("Random Randrange between 0 and 50 with step 5 :", randrange(0, 50, 5))  # Random number from range with step

#guess the number game
# 


import collections

# print(dir(collections))

# words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
# c = collections.Counter(words)
# print("Word Counts :", c)  # Count of each word
# print("Most Common Word :", c.most_common(1))  # Most common word
# print("most common 2 Words :", c.most_common(2))  # Most common 2 words
# print("Elements :", list(c.elements()))  # List of elements

# # d = {}
# # print(d["a"])  # This will raise a KeyError
# d = collections.defaultdict(int)
# print(d["a"])  # This will return 0 (default value for int)
# d["a"] += 1
# print(d)  # This will return 1

# counts=collections.defaultdict(int)

# for word in words:
#     counts[word] += 1
# print("Word Counts using defaultdict :", counts)  # Count of each word using defaultdict


# students = [ ("A","Math"), ("B","Science"), ("A","English"), ("C","Math"), ("B","English")]

# groups=collections.defaultdict(list)
# for student, subject in students:
#     groups[student].append(subject)

# print("Student Groups using defaultdict :", groups)  # Grouped subjects by student using defaultdict


# dq = collections.deque([1, 2, 3])
# dq.append(4)
# dq.appendleft(0)
# print("Deque after appends :", dq)  # Deque after appending elements
# dq.pop()
# print("Deque after pop  :", dq)  # Deque after popping element
# dq.popleft()
# print("Deque after pops :", dq)  # Deque after popping elements


# Employee = collections.namedtuple('Employee', ['name', 'age', 'department'])
# emp1 = Employee(name='Alice', age=30, department='HR')
# print("Employee 1 :", emp1)  # Employee namedtuple
# print("Employee 1 Name :", emp1.name)  # Accessing name
# print("Employee 1 Age :", emp1.age)  # Accessing age
# print("Employee 1 Department :", emp1.department)  # Accessing department
# print(emp1)
# emp2 = Employee(name='Bob', age=25, department='IT')
# print("Employee 2 :", emp2)  # Employee namedtuple
# print("Employee 2 Name :", emp2.name)  # Accessing name
# print("Employee 2 Age :", emp2.age)  # Accessing age
# print("Employee 2 Department :", emp2.department)  # Accessing department



# od = collections.OrderedDict()
# od['a'] = 1
# od['b'] = 2
# od['c'] = 3
# print("OrderedDict :", od)  # OrderedDict
# od.move_to_end('b')
# print("OrderedDict after moving 'b' to end :", od)  # OrderedDict after
# od.move_to_end('a', last=False)
# print("OrderedDict after moving 'a' to beginning :", od)  # OrderedDict after
# od.popitem(last=False)
# print("OrderedDict after popping last item :", od)  # OrderedDict after


# defaults = { "them": "light", "font":"Arial"}
# user = {"font": "times new roman"}
# settings = collections.ChainMap(user, defaults)
# print(settings)
# print("Settings Font :", settings['font'])  # User's font



# ✔ Use Cases of ChainMap()
# 1️⃣ Multiple Configuration Layers (Default + User + System)

# Useful when you have multiple config sources and want to search them in order.

# defaults = {"theme": "light", "font": "Arial"}
# user = {"font": "Roboto"}  # overrides default
# settings = ChainMap(user, defaults)

# print(settings["font"])  # Roboto

# 2️⃣ Variable Scope Resolution (like local → global)

# Python itself internally uses chain-like behavior for scope lookup.

# global_scope = {"x": 10}
# local_scope = {"x": 20}

# scope = ChainMap(local_scope, global_scope)
# print(scope["x"])  # 20 (local overrides global)

# 3️⃣ Temporary Context / Overriding Variables
# base = {"mode": "production"}
# override = {"mode": "debug"}

# env = ChainMap(override, base)
# print(env["mode"])  # debug

# class MyDict(collections.UserDict):
#     def popitem(self):
#         raise RuntimeError("popitem is disabled for MyDict")
    
