# collection of key and values
# mapping a key with its value
houses={"Harry":"Griffimdor","Draco":"Slyther"}

# Changing or adding something new to The Dict
houses["Hermonie"]="Gryffindor"
houses["Sarai"]="sindet"

print(houses["Harry"])
print(houses["Hermonie"])
print(houses)

for name in houses:
    print(name)
for name in houses:
    print(houses[name])
"""
adding another dictionary
"""
student={"name":"sarah","age":21}
# accesing the value name using the key name
print(student["name"])
# changing the value of an item in a dictionary
student["name"]="sindet"
print(student)

# accesing all keys
for values in student.values():
    print(values)

# accesing all the keys
for key in student.keys():
    print(key)


