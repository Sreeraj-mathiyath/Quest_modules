def calculator(option,*values):
    if option == 1:
        return f"sum of {values} is = {sum(values)}"
    
    elif option==2:
        result=values[0]
        for num in values[1:]:
            result-=num
        return f"difference of {values} is {result}"

    elif option==3:
        result=1
        for num in values:
            result*=num
        return f"product of {values} is {result}"
    
    elif option==4:
        result=values[0]
        for i in values:
            result/=num
        return f"division of {values} is {result}"
    
    elif option==5:
        return None
    
    else:
        print("invalid option")




print("""<----------------Menu------------------->\n
            1.Addition(+)
            2.Substraction(-)
            3.Multiplication(*)
            4.Division(/)
            5.Exit""")
option = int(input("Enter your option: "))
count = int(input("Enter the number you want to pass :"))
values=[ ]

for i in range(1,count+1):
    values.append(int(input(f"Enter {i} value: ")))


print(calculator(option,*values))