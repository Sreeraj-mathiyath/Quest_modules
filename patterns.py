row=int(input("Enter the number of rows:"))

# * * * * * 
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# for i in range(row):
#     for j in range(row):
#         print("*", end=" ")
#     print()

# for i in range(1,row+1):
#     for j in range(1,row+1):
#             if i==1 or i==row or j==1 or j==row:
#                 print("*", end=" ")
#             else:
#                  print(" ",end=" ")
#     print()


# 1 1 1 1 
# 2 2 2 2
# 3 3 3 3
# 4 4 4 4
# for i in range(1,row):
#     for j in range(1,row):
#         print(i,end=" ")
#     print()


# *
# * *
# * * * 
# * * * *
# * * * * *

# for i in range(row+1):
#     for j in range(i):
#         print("*",end=" ")
#     print()

# i=1
# while i<=row:
#     j=1
#     while j<=i:
#         print("*",end=" ")
#         j+=1
#     print()
#     i+=1

# * * * * *
# * * * *
# * * *
# * *
# *
# for i in range(row,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()

# i=row
# while i>0:
#     j=0
#     while j<i:
#         print("*",end=" ")
#         j+=1
#     print()
#     i-=1

# * * * * *
#   * * * *
#     * * *
#       * *
#         *
# row=5
# for i in range(row):
#     for j in range(i):
#         print(" ",end=" ")
#     for k in range(i,row):
#         print("*", end=" ")
#     print()

# i=0
# while i<row:
#     j=0
#     while j<i:
#         print(" ",end=" ")
#         j+=1
#     k=i
#     while k< row:
#         print("*",end=" ")
#         k+=1
#     print()
#     i+=1

#         *
#       * *
#     * * *
#   * * * *
# * * * * *
# for i in range(1,row+1):
#     for j in range(row-i):
#         print(" ",end=" ")
#     for k in range(i):
#         print("*",end=" ")
#     print()
# i=1
# while i<=row:
#     j=0
#     while j<row-i:
#         print(" ",end=" ")
#         j+=1
#     k=0
#     while k<i:
#         print("*",end=" ")
#         k+=1
#     print()
#     i+=1



