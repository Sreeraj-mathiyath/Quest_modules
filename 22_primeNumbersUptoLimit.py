def prime(limit):
    for num in range(2,limit+1):
        is_prime=True
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                is_prime=False
        if is_prime:
            print(num)
print(prime(20))