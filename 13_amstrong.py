def armstrong(num):
    num2=str(num)
    n=len(num2)
    sum1=0
    for digit in num2:
        sum1+=int(digit)**n
    if sum1==num:
        return f"{num} is an armstrong number"
    else:
        return f"{num} is not an armstrong number"
    
print(armstrong(153))