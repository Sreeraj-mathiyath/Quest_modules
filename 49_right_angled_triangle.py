row=int(input("Enter number of rows: "))
for i in range(1,row+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
print("upside down triangle:")
for i in range(1,row+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
for i in range(row-1,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
