# Example 1: creating dictionary
mydic={100:'x',102:"y",103:'z'}
#print(mydic) #{100: 'x', 102: 'y', 103: 'z'}

#Example 2: access the items from dictionary
# mydic={
#     "brand":'hundai',
#     "model":"100",
#     'year': 2023
#}
# print(mydic['brand']) #hundai
# print(mydic['model'])  #100

# using get()
# x=mydic.get('brand')
# print(x)

# Example :change the values in dictionary
# print(mydic) #{'brand': 'hundai', 'model': '100', 'year': 2023}
# mydic['year']=2024 #{'brand': 'hundai', 'model': '100', 'year': 2024}
# print(mydic)

#Example: Reading items dictionary using loops

# for i in mydic:
#     print(i) # prints only keys from dictionary

# for i in mydic:
#     print(mydic[i])

# for i in mydic.values():
#     print(i) # Print only values from dictionary


#Example 5: check key exist in dectionary or not


# if "model" in mydic:
#     print("exist")  #true
# else:
#     print("not exist")
#
#
# print("model" in mydic)

# Example 6: find no of items in dictionary

#print(len(mydic)) # 3

# Example 7:  adding one more item into dic

# mydic = {
#     "brand": 'hundai',
#     "model": "100",
#     'year': 2023
# }
#
# mydic["color"]="red"
# print(mydic)

# Example 7:  To remove item from dic
# mydic = {
#     "brand": 'hundai',
#     "model": "100",
#     'year': 2023
# }

# mydic.pop("year")
# print(mydic)

# del mydic["year"]
# print(mydic)

# del mydic
# print(mydic) #NameError: name 'mydic' is not defined

# mydic.clear()
# print(mydic) #{}

# Example 9:  Copying dict
mydic1 = {
    "brand": 'hundai',
    "model": "100",
    'year': 2023
}
#without using copy()
# mydic2=mydic1
# print(mydic2) #{'brand': 'hundai', 'model': '100', 'year': 2023}

# Using copy()
mydic2=mydic1.copy()
print(mydic2)














