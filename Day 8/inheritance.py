# Example 1
# class A:
#     def m1(self):
#         print("This is m1 method from class A")
#
# class B(A):
#     def m2(self):
#         print("This is m2 method from class B")
#
#
# bOBJ=B()
# bOBJ.m1() # This is m1 method from class A
# bOBJ.m2() #This is m2 method from class B

# Example 2 : Single Inheritance

# class A:
#     x,y=10,20
#     def m1(self):
#         print(self.x+self.y)
#
# class B(A):
#     a,b=200,100
#     def m2(self):
#         print(self.a-self.b)
#
# bobj=B()
# bobj.m1()
# bobj.m2()

# Example 3 : Multilevel Inheritance
# class A:
#     x,y=10,20
#     def m1(self):
#         print(self.x+self.y)
#
# class B(A):
#     a,b=200,100
#     def m2(self):
#         print(self.a-self.b)
#
# class C(B):
#     i,j=5,2
#     def m3(self):
#         print(self.i*self.j)
#
# cobj=C()
# cobj.m1()
# cobj.m2()
# cobj.m3()


# Example 4: Heirarchy Inheritance

# class A:
#     x,y=10,20
#     def m1(self):
#         print(self.x+self.y)
#
# class B(A):
#     a,b=200,100
#     def m2(self):
#         print(self.a-self.b)
#
# class C(A):
#     i,j=5,2
#     def m3(self):
#         print(self.i*self.j)
#
# bobj=B()
# bobj.m1()  #30
# bobj.m2()  #100
#
# cobj=C()
# cobj.m1()  #30
# cobj.m3()   #10

# Example 5: Multiple Inheritance

# class A:
#     x,y=10,20
#     def m1(self):
#         print(self.x+self.y)
#
# class B:
#     a,b=200,100
#     def m2(self):
#         print(self.a-self.b)
#
# class C(A,B):
#     i,j=5,2
#     def m3(self):
#         print(self.i*self.j)
#
#
#
# cobj=C()
# cobj.m1()  #30
# cobj.m3()  #10
# cobj.m2() # 100


# Example 6:
# class A:
#     def m1(self):
#         print("This is m1 method  from class A")
#
# class B(A):
#     def m1(self):
#         print("This is m1 method  from class B")
#         super().m1()
#
# bobj=B()
# bobj.m1()   # This is m1 method  from class B
#             #This is m1 method  from class A

# Example 7

# class A:
#     a,b=10,20
#
# class B(A):
#     i,j=100,200
#     def m(self,x,y):
#         print(x+y) #local variables  3000
#         print(self.i+self.j) # class variable 300
#         print(self.a+self.b) # class variable 30
#
#
# bobj=B()
# bobj.m(1000,2000)

# Example 8 : Overriding variables
# class Parent:
#     name="Scott"
#
# class Child(Parent):
#     name="John" # overriding the variable values
#
# cobj=Child()
# print(cobj.name)

# Example 9: Overrding methods- Heriach inherritance

# class Bank:
#     def rateOfIntrest(self):
#         return 0
#
# class XBank(Bank):
#     def rateOfIntrest(self):
#         return 10
#
# class YBank(Bank):
#     def rateOfIntrest(self):
#         return 12
#
# objx=XBank()
# print(objx.rateOfIntrest()) #10
#
# objy=YBank()
# print(objy.rateOfIntrest()) #12


# Example 10: Overloading concepts
#
# class Human:
#     def sayHello(Self,name=None):
#         if name is not None:
#             print("Hello" +name)
#         else:
#             print("Hello")
#
# h=Human()
# h.sayHello("scott")
# h.sayHello()

# Example 11

# class Calculation:
#     def add(self,a=0,b=0,c=0):
#         print(a+b+c)
#
#
# calobj=Calculation()
# calobj.add()
# calobj.add(10,20)
# calobj.add()

















