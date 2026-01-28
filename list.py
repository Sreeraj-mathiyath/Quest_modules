#1
# a=['m','na','i','ke']
# b=['y','me','s','lly']
# c=[]
# for i in range(len(b)):
#     c.append(a[i]+b[i])
# print(c)

#2
# a=['Hello','Hai']
# b=['Madam','Sir']
# c=[]
# for i in range(len(a)):
#     for j in range(len(b)):
#         c.append(a[i]+" " +b[j])

# print(c)

#3
# a = [0, 2, 4, 0, 6, 8]

# j = 0
# for i in range(len(a)):
#     if a[i] != 0:
#         a[i], a[j] = a[j], a[i]
#         j += 1

# print(a)


#4 
# user_list=[]
# n=int(input("Enter the size of the list:"))
# for i in range(1,n+1):
#     user_list.append(int(input(f"Enter {i} value to insert the list:")))
# print(user_list)

#5
# a=[10,20,30,[100,200,[5000,6000],300],40,50]
# a[3][2].append(7000)
# print(a)


# 1.Question: How do you append an element(example 4) to a list?
# my_list = [1, 2, 3]
# my_list = [1,2,3,4]
# my_list.append(4)
# print(my_list)
# my_list.remove(3)
# print(my_list)


# 3.Question: How do you sort a list in ascending order?
# my_list = [3, 1, 4, 2]
# my_list = [3, 1, 4, 2]
# my_list.sort()
# print(my_list)

# # 4.Question: How can you find the length of a list?
# my_list = [1, 2, 3, 4]
# print(len(my_list))

# 5.Question: How do you access an element in a list by index?
# my_list = [10, 20, 30, 40]
# print(my_list[2])

# # 6.Question: How can you reverse a list?
# my_list = [1, 2, 3, 4]
# print(my_list[::-1])


# 7.Question: How do you extend a list with another list?
# my_list = [1, 2]
# another_list = [3, 4]
# my_list.extend(another_list)
# print(my_list)


# 8.Question: How can you count the occurrences of an element in a list(count of 2)?
# my_list = [1, 2, 2, 2, 2, 3]
# print(my_list.count(2))

# 9.Question: How can you insert an element at a specific index in a list(Insert 2 at index 1)?
# my_list = [1, 3, 4]
# my_list.insert(1,2)
# print(my_list)

# 10.Question: How do you pop an element from a list by index(Remove element at index 2)?
# my_list = [1, 2, 3, 4]
# my_list.pop(2)
# print(my_list)

# # 11.Question: How can you clear all elements from a list?
# my_list = [1, 2, 3]
# my_list.clear()
# print(my_list)

# 12.Question: How do you find the maximum element in a list(using max function also you can find maximum value from a list)?
# my_list = [5, 3, 9, 1]
# max_value = max(my_list)
# print(max_value)  

# 14.Question: How can you slice a list to get a subset(Get elements from index 2 to 4)?
# my_list = [0, 1, 2, 3, 4, 5]

# new_list=my_list[2:4]
# if set(new_list).issubset(set(my_list)):
#     print(True)

# 15.Question: How do you concatenate two lists?
# list1=[1,4,7,8,5,2,5]
# list2=[3,6,9]
# print(list1+list2)


# # 16.Question: How can you check if an element exists in a list?
# my_list = [1, 2, 3, 4]
# print(True if 3 in my_list else False)'


# 17.Question: How do you find the index of the first occurrence of an element in a list?
# my_list = [1, 2, 3, 2]
# print(my_list.index(2))

# 18.Question: How can you replace an element at a specific index in a list(Replace element at index 1 by 5)?
# my_list = [1, 2, 3]
# my_list[1]=5
# print(my_list)

# 19.Question: How do you extend a list by adding another list's elements?
# my_list = [1, 2]
# another_list = [3, 4]

# print(my_list+another_list)

# 20.Question: How can you remove all occurrences of an element from a list?
# my_list = [1, 2, 2, 3, 2]
# new_list=[i for i in my_list if i!=2]
# print(new_list)

# my_list = [1, 2, 2, 3, 2]
# dic1 = {"name": "Alice", "age": 30, "city": "New York"}
# # my_list.extend(dic1)
# my_list.append(dic1)
# print(my_list)

# tuple1 = (4, 5)
# tuple1+= (6,)
# print(tuple1)
# tuple1 = (*tuple1, 7)
# print(tuple1)
# i=0
# while i<=5:
#     print("*"*i)
#     i+=1

