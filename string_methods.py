# s="string"
# a='sreeraj'
# print(type(s))
# print(type(a))

# b="my\n name is \n sreeraj"
# print(b)

# c="""my
# name
# is
# sreeraj"""
# print(c)
# print(type(c))

# # """immutability"""
# string="hello"
# string="world"
# print(string)

#ordering/ indexing
# name="sreeraj"
# print(name[0])
# print(len(name))
# # print(name[7])
# print(name[6])
# # name[0]="S"
# # print(name)
# "-7-6-5-4-3-2-1"
# " s r e e r a j"
# " 0 1 2 3 4 5 6"

# #iterable
# course="python"
# for i in course:
#     print(i)

# # a=123456
# # for i in a:
# #     print(a)

# x="SDWSAbuhlnjcsmkdlcbjks1213253645@!#$$%$%$(*())😊❤️"
# print(x)
# print(type(x))


# JAPANESE="こんにちは"
# print(JAPANESE)

# #slicing
# p='python'
# print(p[0:6])
# print(p[1:5])
# print(p[1:])
# print(p[:4])
# print(p[2::])
# print(p[1:-1])
# print(p[::-1])
# print(p[1::2])
# print(p[::2])
# print(p[::-2])
# print(p[::3])
# print(p[-6:-1])

#type conversion of string

greet="Hello World"
# a=greet*3
# print(a)
# # a=greet*3
# # print(a)
# b=14257
# s=str(b)
# print(s)
# print(type(s))
# b="hello"
# s=b+greet
# print(s)
# print("s" in greet)


#updating a string

# string="python"
# new_string="P"+string[1:]
# print(new_string)
# new_string2=string.replace("p","P")
# print(new_string2)

#deleting a string
# a="hello world"

# print(a)
# del a
# print(a)

# a="string" 
# print(dir(a))
"""'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 
'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 
'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower',
 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 
 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 
 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 
 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 
 'swapcase', 'title', 'translate', 'upper', 'zfill'"""

#case conversion methods
# string="hello world.welocome to python introduction."
# print(string.upper())
# s="PYTHON"
# print(s.lower())
# print(s)
# print(string.title())
# print(string.capitalize())
# print(string.swapcase())
# print(s.swapcase())

#serching and finding
# string="welcome to the world of python"
# print(string.find('l'))#case sensitive
# print(string.find('s'))#case sensitive
# print(string.rfind('o'))#case sensitive
# print(string.rfind('s'))#case sensitive
# print(string.index('l'))#raises error if not found
# print(string.rindex('o'))
# print(string.count('o'))
# print(string.count('s'))


# validation / checking
string='python'
u='HELLO WORLD'
s='python-3.14'
d='123456'
w="     "
print(ord('A'))
# print(string.isdigit())
# print(string.isalpha())
# print(s.isdigit())
# print(d.isdigit())
# print(string.isalnum())#only digits and alphabets. no splecial characters allowed
# print(s.isalnum())
# print(d.isalnum())
# print(w.isspace())
# print(string.islower())
# print(string.isalpha())
# print(s.islower())
# print(string.isupper())
# print(u.isupper())
# print(u.istitle())
# print(u.title().istitle())
# print(string.startswith('py'))
# print(string.startswith('t',0))
# print(string.startswith('t',0,5))
# print(string.endswith('on'))
# print(string.endswith('on',5))
# print(string.endswith('on',0,6))



#modification/replacement

# string="hello python"
# print(string.replace("hello","hi"))
# print(string.replace("world","hi"))
# text="hello world, world is beautiful"
# print(text.replace("world","python",1))
# s="  hello  "
# print(s.strip())
# t="!!!!hello!!!!"
# print(t.strip("!"))
# print(t.lstrip("!"))
# print(t.rstrip("!"))
# print(string.removeprefix("hello"))
# print(string.removesuffix("python"))

#formatting and alignment

# string="sreeraj"
# print(string.center(10))
# print(string.center(10,"*"))
# print(string.center(15,"*"))
# print(string.ljust(10,"-"))
# print(string.rjust(10,"-"))
# print(string.zfill(5))
# print(string.zfill(10))
# print(string.zfill(15))

# print("my name is {}".format("Sreeraj"))
# print("my name is {} and i'm a {}".format("sreeraj","python trainer"))
# print("my name is {1} and i'm a {0}".format("sreeraj","python trainer"))
# name="sreeraj"
# stack="python"
# place="kottayam"
# print(f"my name is {name}, stack is {stack} and lives in {place}")
# person_data={'name':'sreeraj','stack':'python','place':'kottayam'}
# template_string="my name is {name} , stack is {stack} and lives in {place}"
# formated_string=template_string.format_map(person_data)
# print(formated_string)

# #splitting and joining

# string="hello world"
# print(string.split())
# fruits="apple,banaba,orange,mango"
# print(fruits.split(','))
# print(fruits.split(',',2))
# print(fruits.rsplit(",",1))
# s="welcome to programming"
# print(s.partition("to"))
# print(s.partition("programming"))
# s="welcome to programming welcome"
# print(s.rpartition("welcome"))
# print(s.rpartition("programming"))

#encoding and decoding
# string.encode(encoding="utf-8",errors="strict")
# UTF stands for Unicode Transformation Format.

# s="hello"
# b=s.encode()
# print(b)

# text = "café"
# b = text.encode("utf-8")
# print(b)


# msg = "hello"
# print(msg.encode("utf-16"))

#miscellaneous

# string="sree\traj"
# print(string)
# print(string.expandtabs(0))
# print(string.expandtabs(1))
# print(string.expandtabs(2))
# print(string.expandtabs(3))
# print(string.expandtabs(4))
# print(string.expandtabs(5))
# print(string.expandtabs(6))
# print(string.expandtabs(7))
# print(string.expandtabs(8))
# print(string.expandtabs(9))
# print(string.expandtabs(10))



# a="ggx"
# a="6544"
# a=" "
# a="@#$$%$ "
# a="gfvghbj\ngfgvhnj"
# a="😞"
# print(a.isascii())
# tabel=str.maketrans("abc","123")
# text="abcabc"
# print(text.translate(tabel))


# \b 
# "''"
# '""'
# chr 