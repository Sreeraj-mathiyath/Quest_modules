from re import *

#==========================match()=====================================
"""
    used to check whether a regex pattern matches at the beginning of a string.
    syntax : re.match(pattern, string, flags=0)
"""
# text = "Python is powerful"
# Pattern1 = "Python"
# print(f"pattern1 matches text: {match(Pattern1,text)}")

# text2 = "I love Python"
# print(f"Pattern matches text:{match(Pattern1,text2)}")


#===========================search=====================================
"""It is used to locate the first occurrence of a character.Note:case sensitive
    syntax: search(pattern,string,flag)
    flag - modifies how a regex pattern works. """

# text1 = "i have been working as a Web Developer since 2023"
# Pattern1 = "Web Developer"
# Pattern2 = "web developer"
# s=search(Pattern1,text1)
# s2 = search(Pattern2,text1)
# s3 = search(Pattern2,text1,IGNORECASE)
# print(s)
# print(s.span())
# print(s.start())
# print(s.end())
# print(s.string)
# print(s.group())
# print(s2)
# s2 = search(Pattern2,text1)
# print(s3)
# s3 = search(Pattern2,text1,IGNORECASE)


#=======================findall()========================================
"""
    used to find all occurrences of a pattern in a string.
    syntax : findall(pattern, string, flags=0)
    """

# text = "My phone Number is 98765 and office number is 12345"
# Pattern1 = "number"
# print(f"Pattern1 matched text:{findall(Pattern1,text)}")
# print(f"Pattern1 matched text:{findall(Pattern1,text,IGNORECASE)}")


#=======================sub()============================================
"""
    used to replace occurrences of a pattern in a string with another string.
    Syntax : sub(pattern, replacement, string, count=0, flags=0)
    replacement : The text to replace the matched pattern with
    string  : The original input string
    count : Number of replacements to make (default 0 = replace all)
    """

# text = "cat bat rat"
# result = sub(r"at", "og", text)
# print(result)


# text = "apple apple apple"
# result = sub(r"apple", "mango", text, count=2)
# print(result)

#======================escape()==========================================
"""
    used to escape (protect) all special regex characters in a string, 
    so that the string is treated as literal text instead of a pattern.

    Regular expressions include special characters like: .  ^  $  *  +  ?  {  }  [  ]  |  (  )  \
    syntax :escape(pattern)
"""

# text = "a+b=c"
# print(search("a+b", text))

# text = "a+b=c"
# pattern = escape("a+b")      
# print(search(pattern, text))

# pattern = escape("Hello (World)!")
# print(pattern)

#=========================meta characters==============================
"""
    things beyond matching literal characters.
"""

"""1. . (Dot) – Match ANY single character - Except newline (\n)"""
# text = "cat cot cut c2t c#t caat"
# p = findall(r"c.t",text)
# p2 = findall(r"c..t",text)
# print(p)
# print(p2)

"""2. ^ = Start of string - Matches only if the pattern begins at the start."""
# text = "Hello world"
# text2 = "Hi world"
# p = match(r"^Hello",text)
# p2 = match(r"^Hello",text2)
# print(p)
# print(p2)

"""3. $ = End of string, Matches only if the pattern ends at the end."""
# text = "Hello world"
# text2 = "Hi world."
# p = search(r"world$",text)
# p2 = search(r"world$",text2)
# p3 = search(r"world.$",text2)
# print(p)
# print(p2)
# print(p3)


"""4. * - 0 or more repetitions"""
# print(findall(r"ab*", "a b ab abb abbb"))
