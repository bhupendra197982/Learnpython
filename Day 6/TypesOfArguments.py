# Example 1:
# def func(i,j):
#     print(i,j)
#
#
# func(10,20) # positional arg
# func(j=20,i=10) # keyword arg

# Example 2: default valies assigned to positional argument

# def func(i,j=10):
#     print(i,j)
#
#
# func(100,200) #100 200
# func(100)  # 100 10

# Example 3: Keyword arg

# def greetings(name,greetmsg):
#     print(greetmsg+"  "+name)
#
#
# greetings(name="jhon",greetmsg="Hello")  #   Hello Jhon
# greetings(greetmsg="Hello",name="jhon")   #  Hello Jhon

# Example 4:

# def my_func(a,b,c):
#     print(a,b,c)
#
#
# my_func(10,20,30) # Positional arg
#
# my_func(a=10,b=20,c=30)  # keywork arg
#
# my_func(b=20,a=10,c=30) # keywork arg
#
#
# my_func(10,20,c=30)   #  10 20 30
# my_func(10,b=20,c=30) # 10 20 30

# my_func(10,b=20,30)  # This is wrong as positional argument must appear before any keyword argument
                     # SyntaxError: positional argument follows keyword argument
# my_func(10,30,b=20)  this is having logical error

# Example 5: Function can return multiple values
def largest(a,b):
    if a>b:
        return a,b
    else:
        return b,a

# print(largest(100,200))
# print(largest(20,10) )

res=largest(10,20)
print(res)

















