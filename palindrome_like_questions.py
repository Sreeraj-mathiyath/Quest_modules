# while loop questions(palindrome like questions)
  
# neon number ---9----9*9=81-----8+1=9----------
# n=int(input("enter a number:"))
# sq=n*n
# sum_of_digit=0
# while sq>0:
#     digit=sq%10
#     sum_of_digit+=digit
#     sq//=10
# if sum_of_digit==n:
#     print("neon")
# else:
#     print("not")

# niven number ------156------1+5+6=12------156/12==0--------
# n=int(input("enter a number:"))
# num=n
# sum_of_digit=0
# while n>0:
#     digit=n%10
#     sum_of_digit+=digit
#     n//=10
# if num%sum_of_digit==0:
#     print("niven number")
# else:
#     print("not")


# automorphic number  ----25-----25**2=625-----25 ends at 625---------
# n=int(input("enter a number:"))
# num=n
# sq=n**2
# length=0
# while n>0:
#     digit=n%10
#     length+=1
#     n//=10

# last_digit=sq%(10**length)
# if last_digit==num:
#     print("automorphic")
# else:
#     print("not")


# special number --------59------5+9+5*9=59---------


# spy number ------123------1+2+3=1*2*3*--------