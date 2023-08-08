# Create string variable
# Example 1
# ways of creating string variable
# s='welcome'
# s="welcoem"
# s=str('welcome')
# s=str("welcome")

#creating empty string variable
#
# name=str()
# name=''
# name=""

#Example 2

# Mutable- cannot change the value of the variable
# immutable- can  change the values of variable
# String is mutable or immutable ?? Ans - It's immutable

# str1='welcome'
# print(id(str1))
#
# str1=str1+'to phyton'
# print(id(str1))

# Example 3: + and * with string



#Example 4 : slicing []

#starting index 0
#ending index 1

#
# str="welcome"
# print(str[1:3])
# print(str[:6]) # welcom here strating inde is 0 by default

# print(str[2:]) # lcome
#
# print(str[1:-1]) #elcom last 1 char removed
# print(str[1:-2])  #elco last 2 char removed


#Example : ord() and chr()

# print(ord('A')) #65
# print(chr(65))  #A

# Exapmle 6 max() , min() and len()

# print(max("abc")) # c
# print(min("abc")) # a
#
# print(len("welcome")) # 7

#Example 7: in ..not in operators

# s='welcome'
# print('come' in s);
# print('bhu' in s);
#
# print('come' not in s);

# Example- String comparsion

# print('tim'=='tie') #False
# print('free' !='freedom') #True


#Example  : Testing string Ture/ False
# s='welcome to python'
# print(s.isalnum()) # Flase
#
# print('Welcome'.isalpha()) #true
#
# print('2022'.isdigit()) # true
#
# print('first number'.isidentifier()) #false
#
# print(s.islower()) #ture
#
# print('WELCOME'.isupper()) #ture
#
# print(s.isspace()) #Ture

# Example 10: Searching for Substring
# s='welcome to python'
#
# print(s.endswith('thon')) # ture
#
# print(s.startswith("welc")) # ture
#
# print(s.find('come'))  # 3
#
# print(s.find('become')) # -1
#
# print(s.count('t')) # retrun number of accurrences of substring the substring


#Example 11: Converting String
# s='Welcome to python'
#
# s1=s.capitalize()
# print(s1) # Welcome to python
#
# s2=s.title()
# print(s2) # Welcome To Python
#
#
# s3=s.lower()
# print(s3)  # welcome to python
#
# s4=s.upper()
# print(s4) # WELCOME TO PYTHON
#
# s5=s.swapcase()
# print(s5) #wELCOME TO PYTHON
#
#
# s6=s.replace('to','on')
# print(s6)

# Example : Reverse a string
# Method 1
# s='welcome'
# rev_str=''
# for i in s:
#     rev_str=i+rev_str # e+
#     print("Reverse string:",rev_str) #emoclew

#Method 2

s="welcome"
# rev_str=s[::-1] # s[start:end:-1]-> s[0:7:-1]
# print(rev_str)  #emoclew


#Write a program to print 0 to 100 using range function in python

for i in range(100):
    print(i)













