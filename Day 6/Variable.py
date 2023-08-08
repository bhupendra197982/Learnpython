#Example 1

# global_var=20  # global variable
#
# def func():
#     local_var=10  # local variable
#     print(local_var)
#     print(global_var)
#
# func()
#
# #print(local_var)   # Invalid becoz local_var is local variable of func()
# print(global_var) # valid global_var is global variable

# Example 2:
# xy=100 # global variable
#
# def cool():
#     xy=200 # local variable
#     print(xy)
#
# cool() # 200

# Example 3'-
# xy=100 # global variable
#
# def cool():
#    # global xy=20  # Invalid syntax
#     global xy
#     xy=200 # local variable
#     print(xy)
#
# cool() # 200
#
# print(xy)

# Example 4:
# x=100
#
#
# def cool():
#     global x
#     x=500
#     print(x)
#
# #cool()  #500
# print(x)   #500

# Example 5 :
# There is no need to declare global variable outside the function
# You can declare them inside the function - global

# def cool():
#     global x
#     x=100
#     print(x)
#
#
# cool()
# print(x)

