# A couple of values thata are not likely to  change but you indeen need to store 
coordinateX=10.0
coordinateY=20.0
# note these are just two variables but they all represent one unit
# values are not likely to change but a pair is made

coordinate=(10.0,20.0)
print(coordinate)


tuple1=tuple(input("Enter the tuple elements"))
print(tuple1)
count=0
for i in tuple1:
    print(i)

tuple2=(1,3,4,5,6)
tuple2[2:4]
print(tuple2[2:4])

numbers=(1,2,3,4,5,6)
numbers[0]
numbers[1]
numbers[2]
#  deleting an item in a tuple
del numbers[4]
