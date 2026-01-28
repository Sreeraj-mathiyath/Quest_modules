#==================defining===========================
# t1 = (1,2,3,4,'abc',1.78,[1,2,5,'quest',14.5],True)
# print(t1)
# t2 = (11,)
# print(t2)
# print(type(t1))
# print(len(t1))
# t3=tuple()
# print(type(t3))

# t4 = (("a", 1), ("b", 2))
# print(t4)

# t5 = 10, 20, 30
# print(type(t5))
# print(t5)


#===============accessing values======================

# my_tuple = ('apple', 'orange', 'banana', 'grape')
# print(my_tuple[0])   
# print(my_tuple[-2])  

# my_tuple = (10, 20, 30, 40, 50, 60)

# print(my_tuple[1:4])    

# print(my_tuple[:3])     

# print(my_tuple[::2])  

# full_name = ("John", "M", "Smith", "Jr.")
# first, *middle_names, last = full_name

# print(first)          
# print(middle_names)   
# print(last)


#========================adding values to tuple====================
# #1. Using the Concatenation Operator (+)
# original_tuple = (10, 20, 30)

# # 1. Adding a single element
# new_value = 40
# new_tuple_single = original_tuple + (new_value,) 
# print(new_tuple_single) 

# # 2. Adding multiple elements
# new_elements = (50, 60)
# new_tuple_multiple = original_tuple + new_elements
# print(new_tuple_multiple)

# #2. Using Repetition and Concatenation (For Repeating Values)

# original_tuple = ('A', 'B')
# new_tuple_repeat = original_tuple + ('C',) * 3
# print(new_tuple_repeat)

# #3. Converting to a List and Back (Flexibility)
# original_tuple = ('alpha', 'beta', 'gamma')

# # 1. Convert to a list
# temp_list = list(original_tuple) 
# print(f"List after conversion: {temp_list}")

# # 2. Add the new value using the list's .append() method
# temp_list.append('delta')

# # 3. Convert the list back to a tuple
# new_tuple_list_method = tuple(temp_list)
# print(f"New Tuple: {new_tuple_list_method}")



#=====================updating===========================
# #1. Using Conversion to List
# original_tuple = ('A', 'B', 'C', 'D')
# index_to_change = 1
# new_value = 'Z'

# # Step 1: Convert to list
# temp_list = list(original_tuple)

# # Step 2: Modify the element at index 1
# temp_list[index_to_change] = new_value  # 'B' is replaced by 'Z'

# # Step 3: Convert back to tuple
# new_tuple = tuple(temp_list)

# print(original_tuple)
# print(new_tuple)     

#==================deleting=================================
# my_tuple = (1, 2, 3)

# del my_tuple

# # Trying to access the tuple now will result in a NameError
# # print(my_tuple)

#==================methods==================================

# my_tuple = (1, 5, 2, 5, 3, 5, 4)
# count_fives = my_tuple.count(5)

# print(count_fives) 



# my_tuple = ('apple', 'banana', 'cherry', 'banana', 'date')

# first_index = my_tuple.index('banana')
# print(f"First index of 'banana': {first_index}")

# second_index = my_tuple.index('banana', 2)
# print(f"Index of 'banana' after index 2: {second_index}")



# Original Tuple
colors = ("Red", "Green", "Blue", "Yellow")

# We want to change "Green" (index 1) to "Purple"
i = 1

# 1. Take everything BEFORE index 1 ('Red')
# 2. Add ("Purple",)
# 3. Take everything AFTER index 1 ('Blue', 'Yellow')
# Note: We use i+1 to skip the old item we are replacing
new_colors = colors[:i] + ("Purple",) + colors[i+1:]

print(new_colors)
# Output: ('Red', 'Purple', 'Blue', 'Yellow')