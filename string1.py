# 1. Extract the substring "World" from s = "Hello, World!" using negative indexing only.
# s="Hello, World!"
# extract=s[-6:-1]
# print(extract)

# 2. For s = "1234567890", write slicing expressions to:

# Extract all odd digits ("13579").
# Extract all even digits ("24680").
# s="1234567890"
# odd=s[0:9:2]
# print(odd)
# even=s[1::2]
# print(even)

# Given s = "madam", check if the string is a palindrome using slicing.
# s="madam"
# print("palindrome" if s==s[::-1] else "Not a palindrome")

# 4. For s = "abcdefghijklmnopqrstuvwxyz", extract:
# Every 5th character starting from the beginning.
# Every 4th character in reverse order.
# s = "abcdefghijklmnopqrstuvwxyz"
# fifth_elements=s[::5]
# print(fifth_elements)
# fourth_element=(s[::-1][::4])
# print(fourth_element)

# s=[1,2,3,4,5,6,7]
# reversed(s)
# print(list(reversed(s)))


# 6. Split "MachineLearningIsFun" into separate words using slicing
# s="MachineLearningIsFun"
# w1=s[0:7]
# print(w1)
# w2=s[7:15]
# print(w2)
# w3=s[15:17]
# print(w3)
# w4=s[17:]
# print(w4)

# 7. Reverse only vowels in "Hello, World!"
# s="Hello, World"
# vowels = "aeiouAEIOU"
# vowel_list = [ch for ch in s if ch in vowels]
# vowel_list.reverse()
# result=""
# vowel_index=0
# for ch in s:
#     if ch in vowels:
#         result+=vowel_list[vowel_index]
#         vowel_index+=1
#     else:
#         result+=ch
# print(result)

# 8. Generate a string where every character of "Python" is repeated twice #output: ppyytthhoonn
# string="python"
# result=""
# for i in string:
#     result+=i*2

# print(result)

# 9. Extract all words from a string that start with a vowel

# s="athul and sreeraj are good friends"
# vowels = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
# list1=s.split()
# extract=[i for i in list1 if i.startswith(vowels)]
# print(extract)


# 10. Replace every second character in a string with *
# s="python"
# result=""
# for i in range(len(s)):
#     if i%2==0:
#         result+="*"
#     else:
#         result+=s[i]

# print(result)

# s="my name is sreeraj"
# result=""
# count=0
# for ch in s:
#     if ch.isalpha():
#         count+=1
#         if count%2==0:
#             result+="*"
#         else:
#             result+=ch
# print(result)


# 11. Extract alternating characters starting from the second character 
# string="alternative characters"
# print(string[1::2])


# 12. Shift vowels to the beginning and consonants to the end of the string:
# text = "HelloWorld"
# vowels = "aeiouAEIOU"
# # Output: eoHllWrld
# text = "HelloWorld"
# vowels = "aeiouAEIOU"
# v=""
# c=""
# for i in text:
#     if i in vowels:
#         v+=i
#     else:
#         c+=i
# result=v+c
# print(result)

# 13. Write a slicing expression to remove the first and last characters from s = "PythonRocks".
# s="PythonRocks"
# print(s[1:-1])

# 14. Given s = "ABCDEFGHIJKLM", write a slicing expression to rearrange the string as "ACEGIKMBDFHJL".
# s = "ABCDEFGHIJKLM"
# result=s[::2]+s[1::2]
# print(result)

# 15. For s = "racecar", use slicing to extract the string in reverse and check if it matches the original string (palindrome check).
# s="racecar"
# print("palindrome" if s==s[::-1] else "Not a palindrome")

# s = "The quick brown fox jumps over the lazy dog"
# print(s[4:9])


# 17. Given s = "PythonProgramming", extract the following:

# The substring "Python".
# The substring "Programming".
# The last 5 characters of the string.
# s="PythonProgramming"
# s1=s[:6]
# print(s1)
# s2=s[6:]
# print(s2)
# s3=s[-5:]
# print(s3)

# 18. For s = "HelloWorld", extract:

# The first 5 characters.
# The last 5 characters.
# The middle 3 characters ("loW").
# s="HelloWorld"
# print(s[:5])
# print(s[-5:])
# print(s[3:6])


# 19. Reverse the string s = "abcdefg" using slicing.
# s = "abcdefg"
# print(s[::-1])

# 20. Given s = "abcdefghijklm", extract:

# Every second character starting from the beginning.
# Every third character starting from index 2.
# The string in reverse order.
# s = "abcdefghijklm"
# print(s[::2])
# print(s[2::3])
# print(s[::-1])


# s="HeLlO"
# result=""
# for i in s:
#     if i.isupper():
#         result+=i.lower()
#     else:
#         result+=i.upper()
# print(result)

# 21. For s = "PythonRocks", extract:

# The substring "Rocks" in reverse order.
# All characters except the first and last.

# s="PythonRocks"
# print(s[6:][::-1])
# print(s[1:-1])

#1.
# string=input("Enter a string:")
# print(string[1:-1])

# #2.
# s="abcdef"
# print(s[::2])

#3.
# s=input("enter a string:")
# result=""
# for i in s:
#     result=i+result
# print(result)


#4.
# s=input("enter a string:")
# n=len(s)
# if n%2==1:
#     mid=s[n//2]
# else:
#     mid=s[n//2 -1 : n//2 + 1]

# print(mid)  
# 
# 
# 5.
# string=input("Enter a string:")
# swapped=string[-1]+string[1:-1]+string[0]
# print(swapped) 


#6.
# string=input("Enter a string:")
# s=string.split()
# result=[]
# for i in range(len(s)):
#     result.append(s[i][0].upper()+s[i][1:].lower())
# print(' '.join(result))

#7.
# string=input("Enter a string:")
# vowels='aeiouAEIOU'
# count=0
# for i in string:
#     if i in vowels:
#         count+=1
# print(count)

#8
# string=input("Enter a string:")
# result=""
# for i in string:
#     if i.isspace():
#         result+="-"
#     else:
#         result+=i

# print(result)
# list1=[1,2,3,4,5,6]
# for i in list1:
#     if i==3:
#         print(i)
#         break
# else:
#     print("completed")
# a="abcde"
# b="cdeab"
# result=a*2
# print(result)
# if b in result:
#     print(True)
fruits = ["apple","banana"]
print(dir(fruits))
" 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop',"
" 'remove', 'reverse', 'sort'"

