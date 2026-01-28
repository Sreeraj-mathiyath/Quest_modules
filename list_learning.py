# #============defining a list===========================
# list1 = [1,2,3,'sree','quest',3.14,2.5]
# list2 = [1]
# list3 = list()
# print(type(list1))
# print(type(list2))
# print(type(list3))
# print(len(list1))
# print(len(list2))
# print(len(list3))

#===================operators===========================

# a = [1,2,3,4,5,6]
# b = [7,8,9,10]
# c = a+b
# d = a*3
# print(c)
# print(d)

# print(1 in a)
# print(10 in a)

#=====================indexing============================
# list1 = [1,2,3,'sree','quest',3.14,2.5]
# print(list1[0])
# print(list1[2])
# print(list1[-1])
# print(list1[-2])
# print(list1[3][0])
# print(list1[3][2])
# print(list1[1:])
# print(list1[2:])
# print(list1[1:4])
# print(list1[2::])
# print(list1[-4:-1])
# print(list1[0:6:2])
# print(list1[::-1])

#===================adding values==========================
# a=[1,2,3,4,5]
# a.append(10)
# # a.append(12,13,14)
# a.insert(2,15)
# a+=['a','b']

# b=['a','b','c','d']
# a.extend(b)

# print(a)

#===================updating values=======================
# a=[1,2,3,4,5]
# a[0]='a'
# a[1]='b'
# a[2:5]=['c','d','e','f']
# print(a)

#==================deleting values===========================
# a=[1,2,3,4,5]
# p=a.pop()
# print(a)
# print(p)
# a.remove(2)
# print(a)
# a.clear()
# print(a)
# # del a
# # print(a)

#==================list methods=============================

# list1 = [1,'a',2,'b',3,'c',4,'d',5]
# list1.append('e')
# list1.insert(0,0)
# list1.remove(5)
# list1.pop()
# print(list1)

# num=[1,2,5,24,8,2,36,971,2,52,15,52,541,487,81,7,23]
# print(num.index(36))
# print(num.count(2))
# num.sort()
# print(num)

# num.reverse()
# print(num)

# n = num.copy()
# print(n)

# print(len(num))
# print(max(num))
# print(min(num))
# print(sum(num))

#=====================loops================================

# numbers = [8,5,4,72,6,12,4,85,7,1,52,4,12]
# # for i in numbers:
# #     print(i)

# # for i in range(len(numbers)):
# #     print(numbers[i])

# # for i in range(0,len(numbers),2):
# #     print(numbers[i])

# # i=0
# # while i<len(numbers):
# #     print(numbers[i])
# #     i+=1

# i=0
# while i<len(numbers):
#     print(numbers[i])
#     i+=2


#===================nested list============================

# matrix = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
# print(matrix[1])
# print(matrix[2])
# print(matrix[0][0])
# print(matrix[1][1:])

# for i in matrix:
#     for j in i:
#         print(j,end=" ")
#     print()

# i=0
# while i < len(matrix):
#     j=0 
#     while j <len(matrix[i]):
#         print(matrix[i][j],end=" ")
#         j+=1
#     print()
#     i+=1


#==================list comprehension=========================
# numbers  = [i for i in range(1,11)]
# print(numbers)

# even = [i for i in numbers if i%2==0]
# print(even)

# sq_cube = [i**2 if i %2==0 else i**3 for i in numbers]
# print(sq_cube)

#==================packing and unpacking=======================
# Packing: Creating a list containing three elements
# packed_list = [10, "Python", 3.14]
# print(packed_list)


# num, string, decimal = packed_list

# print(num)
# print(string)
# print(decimal)

# student_data = ["Alice", 90, 85, 92, 78, "A"]
# name, *marks, grade = student_data
# print(name)
# print(marks)
# print(grade)

# list_a = [1, 2, 3, 4, 5]

# # *rest at the end
# a, b, *rest = list_a
# print(a)
# print(b)
# print(rest)


# # *rest in the middle
# first, *middle, last = list_a
# print(first)
# print(middle)
# print(last)
