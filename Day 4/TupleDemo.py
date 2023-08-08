# Example: 1 Creating tuple
# mytuple=('apple','banana','cherry')
# print(mytuple)
#
# Example 2: access tuple items
# mytuple=() # empty tuple items
# mytuple=('apple','banana','cherry')
# print(mytuple[1]) # banana here index starts from 0
# print(mytuple[-1]) #cherry
#
# Example 3 : range of indexes
# mylist=('apple','banan','kiwi','Mnago','melon','cheery')
# print(mylist[2:5]) #['kiwi', 'Mnago', 'melon']
#
# print(mylist[-4:-1]) #['kiwi', 'Mnago', 'melon']
#
# Example  4 : change tuple item - Cannot
# by default tuple does not allow you to change becoz it's immutable
# but there is work around
# tuple--> list(modify)--> tuple
# mytuple=('apple','banana','cherry')
# mylist=list(mytuple)
# mylist[0]='orange'
# mytuple=tuple(mylist)
# print(mytuple) #('orange', 'banana', 'cherry')
#
# x = 1
# y = 35656222554887711
# z = -3255522
#
# print(type(x))
# print(type(y))
# print(type(z))
#
#
# x = 35e3
# y = 12E4
# z = -87.7e100
#
# print(type(x))
# print(type(y))
# print(type(z))