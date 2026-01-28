number=int(input("enter a number:"))
if number%2==0:
    if number%5==0:
        print(number,"divsible by 5 and 2")
    else:
        print(number,"divisble by 2 but not by 5")
else:
    if number%5==0:
        print(number,"divisible by 5 but not by2")
    else:
        print(number,"not divisible by 2 and 5")