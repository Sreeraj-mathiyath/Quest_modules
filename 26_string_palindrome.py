def palindrome(string):
    if string == string[::-1]:
        return f'"{string}" is a palindrome'
    else:
        return f'"{string}" is not a palindrome'
    

s=input("Enter a string: ")
print(palindrome(s))