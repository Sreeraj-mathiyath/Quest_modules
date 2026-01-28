row=int(input("enter the number of rows: "))
num=0
for i in range(1,row+1):
    for j in range(i):
        print(num,end=" ")
        num+=1
    print()

