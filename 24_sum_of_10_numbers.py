def Sum(number):
    sum=0
    for n in range(number,number+10):
        sum+=n
    return sum

# print(Sum(10))

s=0
for i in range(1,10+1):
    print(i,s)
    s+=i
print(s)