def palidrome(num):
    n=str(num)
    n2=n[::-1]
    if n==n2:
        return f"{num} is a palindrome"
    else:
        return f"{num} is not a palindrome"

print(palidrome(555))
print(palidrome(741))