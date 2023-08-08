# #Example - How to create a list
#
# mylist1=[10,20,30,40,50,]
# mylist2=['apple','banan','Mnago']
# mylist3=['apple',10,'banana',28]
# mylist=list() #Empty list
#
# print(mylist1)
# print(mylist2)
# print(mylist3)
# print(mylist)

# Example -Accessing items from the list
# mylist=['apple','banan','Mnago'] #index starts from 0
#
# print(mylist[0])
# print(mylist[1])
# print(mylist[2])
#
# print(mylist[-1]) #Mnago
# print(mylist[-2]) #banan

#Example - Range of Index

# mylist=['apple','banan','kiwi','Mnago','melon','cheery']
#
# print(mylist[2:5])  #['Mnago', 'kiwi', 'melon']
#
# print(mylist[-5:-1])  #['Mnago', 'kiwi', 'melon']

# Example - Change item values
# mylist=['apple','banan','kiwi','Mnago','melon','cheery']
# print(mylist) #['apple', 'banan', 'kiwi', 'Mnago', 'melon', 'cheery']
#
# mylist[0]='orange'  # Change the value based on Index we pass
#
# print(mylist)

# Example 5: Read the items using loop
# mylist=['apple','banan','Mnago']
#
# for i in mylist:
#     print(i)

# #Example 6: check if the item exist in the list or not
# mylist=['apple','banan','Mnago']
# if "apple21" in mylist:
#     print('yes apple is present')
# else:
#     print('No apple is not present')

#Example 7 : List Length (counting number of items in a list)
# mylist=['apple','banan','Mnago']
# print(len(mylist)) # 3

#Example : Add items append() insert()
# mylist=['apple','banan','Mnago']
# mylist.append("Orange") adding new item at the end of the list
# print(mylist)  #['apple', 'banan', 'Mnago', 'Orange']
#

# mylist=['apple','banan','Mnago']
# mylist.insert(1,'orange') # Add item some where in the middle of the list based on the index
#
# print(mylist)

# Example - Remove item from the list
# pop()

# mylist=['apple','banan','Mnago']
#
# mylist.pop(0) # here we should
# print(mylist)

#del
# mylist=['apple','banan','Mnago']
# del mylist[2] #Here del command removes single items based on the index
# print(mylist) #['apple', 'banan']

#clear()
# mylist=['apple','banan','Mnago']
# mylist.clear()
# print(mylist) #[]

# Example 10 - Copy list
#List()
# mylist1=['apple','banan','Mnago']
# mylist2=list(mylist1)
#
# print(mylist1) #['apple', 'banan', 'Mnago']
# print(mylist2) #['apple', 'banan', 'Mnago']
#Copy()
# mylist1=['apple','banan','Mnago']
# mylist2=mylist1.copy()
#
# print(mylist1) #['apple', 'banan', 'Mnago']
# print(mylist2) #['apple', 'banan', 'Mnago']

# Example : Combine / join two list

# Using + operator
# list1=['a','b','c']
# list2=[1,2,3]
# list3=list1+list2
# print(list3)

# Using looping statement

# list1=['a','b','c']
# list2=[1,2,3]
#
# for i in list2:
#     list1.append(i)
# print(list1) #['a', 'b', 'c', 1, 2, 3]

#using ectend()
# list1=['a','b','c']
# list2=[1,2,3]
# list1.extend(list2)
# print(list1)  #['a', 'b', 'c', 1, 2, 3]

mylist=['apple','banan','Mnago']
print('apple' in mylist)















