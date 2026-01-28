def prime(num):
    if num<=2:
        return "NOT A PRIME"
    for i in range(2,num-1):
        if num%i==0:
            return "NOT A PRIME"
        else:
            return "The number is a prime"
        
print(prime(8))