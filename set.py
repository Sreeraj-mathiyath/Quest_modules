fruits={"apple", "banana", "cherry"}
print(fruits)
p=fruits.pop()
print(p)

# fruits.add("orange")
# print(fruits)

# # fruits.discard("banana")
# # print(fruits)

# # fruits.remove("banana")
# # print(fruits)

# print("apple"in fruits)

# print(len(fruits))

# a={1,2,3,4}
# b={3,4,5,6}
# print(a.union(b))

# print(a.intersection(b))

# print(a.difference(b))
# print(b-a)

# print(a^b)
# print(b^a)

# list1=[1,2,2,3,4,4,5]
# remove_duplicate=set(list1)
# print(remove_duplicate)
# print(set(list1))

# set1={10,20,30}
# set2={20,40,50}
# set1.update(set2)
# print(set1)

# print(set1.issubset(set2))

# set1.clear()
# print(set1)


# f=frozenset(list1)
# print(f)

# s={1,2,3,4,5,6,7,8,9}
# s1={4,5,6,7,8,9,10}
# result=s.symmetric_difference(s1)
# print(result)

# l=[1,2,3,4,5,6,2,3,1]
# s=set()
# d=set()
# for i in l:
#     if i in s:
#         d.add(i)
#     else:
#         s.add(i)

# print(s)
# print(d)

# s1={1,2,3}
# s2={3,4,5}
# if s1.isdisjoint(s2):
#     print("Disjoint")
# else:
#     print("Not Disjoint")


# s1={1,2}
# s2={3,4}
# s3={4,5}
# s1.update(s2,s3)
# print(s1)

# sentence="my name is quis and my team head is lijo"
# l1=sentence.lower().split()
# s=set(l1)
# print(len(s))


# set1 = {'a', 'b', 'c'}
# set2 = {'b', 'c', 'd'}
# print(set1.symmetric_difference(set2))

# s=set(i for i in range(1,11))
# s2=set([1,2,4,6,7,10])
# print(s-s2)

# sentence=input("enter a paragraph:")
# unique_words=set()
# vowel="aeiouAEIOU"
# for ch in sentence:
#     if ch in vowel:
#         unique_words.add(ch)
# print(unique_words)

# string1="silent"
# string2="listen"
# s=set(string1)
# s2=set(string2)
# if s==s2:
#     print(True)


# s={1,2,3,4,5,6}
# s1={4,5,6}
# subset=True
# for i in s1:
#     if i not in s:
#         subset=False
#         break

# if subset:
#     print("Subset")
# else:
#     print("not")

# set1 = {'a', 'b', 'c'}
# set2 = {'b', 'c', 'd'}
# print(set1.symmetric_difference(set2))

# s1={1,2,3,4,5}
# fs = frozenset(s1)
# print(fs)
# print(type(fs)) 

# set1={1,2,3}
# set1.update([4,5,6])
# print(set1)
# dict1 = {"name": "Alice", "age": 30, "city": "New York"}
# set1.update(dict1.items())
# print(set1)