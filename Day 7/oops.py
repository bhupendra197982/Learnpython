# Example 1:


# class MyClass:
#     def myfun(self):
#         pass
#
#     def display(self, name):
#         print(name)
#
#
# mc1 = MyClass()
#
# mc1.myfun()
# mc1.display("scot")  # scot

# Example 2:


# Example3:

# class MyClass:
#     a,b=10,20 # class variables
#     def add(self):
#         print(self.a+self.b)
#     def mul(self):
#         print(self.a*self.b)
#
# mc=MyClass()
# mc.add() #30
# mc.mul() #200


# Example 4:

# i,j=15,25  # Global Variable
#
# class MyClass:
#     a,b=10,20  # Class variable
#     def add(self,x,y):
#         print(x+y)  # x,y are local variables
#         print(self.a+self.b)  # a ,b are class variables
#         print(i+j)  # i,j are global variables
#
# mc=MyClass()
# mc.add(100,200)

# Example 5:

# a,b=15,25 # global variable
# class MyClass:
#     a,b=10,20  # class variables
#     def add(self,a,b):
#         print(a+b) # local varibales
#         print(self.a+self.b)
#         print(globals()['a']+globals()['b']) # global variable
#
#
# mc=MyClass()
# mc.add(100,200)

# Example 6: One class can have multiple objects

# Example 7: constructor example

# class MyClass:
#     def __init__(self):
#         print("this is constructor")
#     def m1(self):
#         print("Hello..")
#     def m2(self,x,y):
#           return (x+y)
#
#
# mc=MyClass()  #invoke constructor automatically
# mc.m1() # method we have call explicitly by using object
# res=mc.m2(10,20)
# print(res)

# Example 8

# class MyClass:
#     name = 'jhon'
#
#     def __init__(self, name): #constructor expecting one argument
#         print(name)
#         print(self.name)
#
# mc=MyClass("David") # passing parameter to the constructor

# Example 8-

# class Emp:
#
#     def __init__ (self,eid,ename,sal):
#         self.eid=eid
#         self.ename=ename
#         self.sal=sal
#
#
#     def display(self):
#         print(self.eid,self.ename,self.sal)
#
# e1=Emp(101,"Jhon",50000)
# e1.display()
#
# e2=Emp(102,"Scoot",60000)
# e2.display()

# Example 10

class Emp:

    def __init__ (self,eid,ename,sal):
        self.eid=eid
        self.ename=ename
        self.sal=sal


    def __str__(self):
        return(self.ename,self.sal)

e1=Emp(101,"Jhon",50000)
print(e1)
