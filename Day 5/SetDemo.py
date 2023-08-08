#Example 1 : Creating set
# myset={'apple',"banana","cherry"}
# print(myset) #{'apple', 'cherry', 'banana'}

#Example 2 : Accessing items from set
# myset={'apple',"banana","cherry"}
# for i in myset:
#     print(i)


#Example 3: Values exists in set or not
# myset={'apple',"banana","cherry"}
# print('banana' in myset)

#Example : adding items to set
# add()- add single item at a time
# update()- add Multiple items
# myset={'apple',"banana","cherry"}
# myset.add('orange')
# print(myset)

# myset={'apple',"banana","cherry"}
# myset.update(['mango','graps']) #{'cherry', 'banana', 'graps', 'mango', 'apple'}
# print(myset)

#Example 5: find no of item in set
# myset={'apple',"banana","cherry"}
# print(len(myset))

#Example 6: remove item from set- remove() ,discard()
myset={'apple',"banana","cherry"}
# myset.remove("apple")
# print(myset)
#
# myset.remove('xyz') #KeyError: 'xyz'
# print(myset)

# myset.discard('banana')
# print(myset) #{'apple', 'cherry'}
#
# myset.discard('xyz') # will not throw any error

# Example 7: Clear all the items from set
# myset={'apple',"banana","cherry"}
# myset.clear()
# print(myset)
#
# del myset
# print(myset) #NameError: name 'myset' is not defined






