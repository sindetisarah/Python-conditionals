#creating an empty set
numbers=set()
numbers.add(20)
numbers.add(30)
numbers.add(40)
numbers.add(50)
numbers.add(60)
print(numbers)

# expected output {40,50,20,60,30}
# Notice they dont have a particular order and they only appear once

# Removing an element from a set
numbers.remove(30)
print(numbers) 
# // thirty gets printed out

# Finding the length of the above numbers use  len()
print(f"The length of the above numbers is {len(numbers)}")






List1 = [12, 4, 56, 17, 8, 99]
print(max(List1),"\n")

def Mean(list2): 
    return sum(list2) / len(list2) 
list2 = [12, 4, 56, 17, 8, 99]
mean = Mean(list2)
print("Mean of list2 =", round(mean,2),"\n")



