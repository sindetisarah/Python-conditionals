numbers=[1,2,3,4,5,6]
for i in numbers:
    print(i)

# Looping through a nested list
num=[[1,2,3],[4,5,6],[7,8,9]]
new_num =[numbers for small in num for numbers in small]
print(new_num)

# Looping through a list and appending the elements in a new list
num_append=[]
for small in num:
    for numbers in small:
        num_append.append(numbers)
print(new_num)

# Range to loop through a huge list
for i in range(10):
    print(i)
    