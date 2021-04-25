# define class point
class Point():
    """
    init is a methodal function/constructor

    """
    def __init__(self, input1,input2):
        """
        self rep the object in question
        storing the inputvalues in the point "class" in the properties we call x and y
        """
        self.x=input1 
        self.y=input2

    # instance of an object
northpole=Point(20,50)
print(northpole.x)
print(northpole.y)
print(northpole)

# define class flight
class Flight():
    def __init__(self,capacity):
        self.capacity=capacity
        self.passenger=[]


    def add_passenger(self,name):
        if not self.open_seats():
            return False
        self.passenger.append(name)
        return True

    def open_seats(self):
        return self.capacity-len(self.passengers)

# instance of an object
wilson=Flight(4)

people=["Sarah","Juliet","Hermonie","Shadya","Sheilla","Wendy"]
for person in people:
    space=wilson.add_passenger(sarah)
    if space:
        print(f"Addded {person} to Board the flight")
    else:
        print(f"All seats have been booked for{person}")


