# n=153
# num=n
# l=len(str(n))
# armstrong=0
# while num>0:
#     digit = num%10
#     armstrong += (digit**l)
#     num//=10
# if armstrong==n:
#     print("armstrong")
# else:
#     print("not")

#reverse a string
# s = "sreeraj"
# revse=""
# for i in s:
#     revse=i+revse

# print(revse)

# r = ""
# i = len(s) -1
# print(len(s)-1)
# while i>=0:
#     r += s[i]
#     i-=1
# print(r)

#prime

# n=11
# i=2
# while i<=n:
#     if n%i==0:
#         print(False)
#         break
#     else:
#         print(True)
#     i+=1

#reverse a int
# n=123
# num=n
# r=0
# while n>0:
#     l=n%10
#     r=r*10+l
#     n//=10

# print(r)

# def fact(n):
#     if n==1:
#         return 1
#     else:
#         return n*fact(n-1)
    
# print(fact(5))

row=5
# for i in range(1,row+1):
#     for j in range(i):
#         print("* ",end="")
#     print()

# i=0
# while i<=row:
#     print("* "*i)
#     i+=1

# for i in range(row+1,0,-1):
#     for j in range(i):
#         print("* ",end="")
#     print()

# for i in range(row):
#     for j in range(i):
#         print(" ",end=" ")
#     for k in range(i,row):
#         print("* ",end=" ")
#     print()


# for i in range(row):
#     for j in range(i):
#         print(" ",end=" ")
#     for k in range(i,row):
#         print("*", end=" ")
#     print()