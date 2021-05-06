"""
nested dictionary in a list
"""
people=[
   {"name":"Barah","room":36} ,
   {"name":"Alicia","room":20} ,
   {"name":"Catie","room":32}
]

"""
we can define a function as sort of alook up to help the interpreter to knoew what to specifically sort
sort by running the function ,the function basicallty returns the key we want to sort
"""

def sort(people): 
   return people["name"]



people.sort(key=sort)
print(people)

def sort_room(people):
   return people["room"]
people.sort(key=sort_room)
print(people)

"""
This is asimpler way of writing the above function
lambda in this case is a function
takes a person as inputs and finally returns a sorted list of people
"""

people.sort(key=lambda person:person["name"])
print(people)

"""
sorting the dictionaries now using a different key
"""

# def room_sort(people):
#    return people["room"]
# people.sort(key=room_sort)
# print(people)
# """
# using a lambda expression to make a function more simpler and easier
# """
# people.sort(key=lambda people:people["name"])
# print(people)
