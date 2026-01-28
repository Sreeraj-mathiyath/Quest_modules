# 1.Write a program to print first 10 Even Numbers
# i=0
# n=2
# while i<=10:
#     print(n)
#     n+=2
#     i+=1    

# 2.Write a program to print first 10 Odd Numbers
# i=0
# n=1
# while i<=10:
#     print(n)
#     n+=2
#     i+=1


# 3.Write a program to print first 10 integers and their squares using while loop
# n=1
# i=1
# while i<=10:
#     print(n,n**2)
#     n+=1
#     i+=1

# 4.Print the following series:10, 20, 30 … 50
# n=10
# while n<=50:
#     print(n)
#     n+=10

# 5.Print the following series:20, 18, 16 … 2
# n=20
# while n>1:
#     print(n)
#     n-=2

# 6.Write a program to print sum of first 10 numbers.
# n=1
# s=0
# while n<=10:
#     s+=n
#     n+=1
# print(s)


# 7.Write a program to print sum of first 10 Even numbers.
# s=0
# n=2
# i=1
# while i<=10:
#     s+=n
#     n+=2
#     i+=1
# print(s)


# 8.Write a program to print multiplication table of a number entered from the user.
# n=int(input("Enter the a number to view Multiplication  table:"))
# i=1
# while i<=10:
#     print(i,"*",n,"=",i*n)
#     i+=1

# 9.Write a program to print all even numbers between two intervals.
# n1=int(input("Enter first number:"))
# n2=int(input("Enter first number:"))
# if n1%2!=0:
#     n1+=1

# while n1<=n2:
#     print(n1)
#     n1+=2    


# 10.Write a program to check whether a number is prime or not using while loop
# n=int(input("enter a number:"))
# if n<1:
#     print("not a prime")
# else:
#     i=2
#     is_prime=True
#     while i<n//2:
#         if n%i==0:
#             is_prime=False
#             break
#         i+=1
#     if is_prime:
#         print("Prime")
#     else:
#         print("not a prime")
# 11.Factorial of a number
# n=int(input("Enter a number:"))
# fact=1
# i=1
# while i<=n:
#     fact*=i
#     i+=1
# print(fact)



# 12.Reverse a number
# n=int(input("Enter a number:"))
# reverse=0
# num=n
# while n>0:
#     last=n%10
#     reverse=(reverse*10)+last
#     n=n//10
# print(reverse)


# 13.check Palindrome or not
# n=int(input("Enter a number:"))
# reverse=0
# num=n
# while n>0:
#     last=n%10
#     reverse=(reverse*10)+last
#     n=n//10
# if num==reverse:
#     print("palindrome")
# else:
#     print("not a palindrome")


# 14. Check whether a number is armstrong or not
# n=int(input("Enter a number:"))
# num=n
# length=0
# temp=n

# while temp>0:
#     temp//=10
#     length+=1

# sum_of_power=0
# while n>0:
#     digit=n%10
#     sum_of_power+=digit**length
#     n//=10
# if sum_of_power==num:
#     print("armstrong")
# else:
#     print("not an armstrong")


# 15.Write a program to find the sum of digits of a number from the user.
# n=int(input("Enter a number:"))
# sum_of_digit=0
# while n>0:
#     digit=n%10
#     sum_of_digit+=digit
#     n//=10
# print(sum_of_digit)

# 16.Write a program to print fibonacci series using while loop
# a=0
# b=1
# while a<20:
#     print(a)
#     a,b=b,b+a

    
# 17.Write a program to accept 10 numbers from the user and display it’s average
# i=1
# sum_of_numbers=0
# while i<=10:
#     n=int(input(f"Enter {i} number:"))
#     sum_of_numbers+=n
#     i+=1
# avg=sum_of_numbers/10
# print(avg)
