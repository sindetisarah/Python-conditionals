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

define class flight
class Flight():
    # init always creates a new flight in this a case
    def __init__(self,capacity):
        self.capacity=capacity
        self.passengers=[]


    def add_passenger(self,name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity-len(self.passengers)

# instance of an object
wilson=Flight(4)

people=["Sarah","Juliet","Hermonie","Shadya","Sheilla","Wendy"]
for person in people:
    space=wilson.add_passenger(person)
    if space:
        print(f"Addded {person} to Board the flight")
    else:
        print(f"All seats have been booked {person}")

class ZoomCall():
    def __init__ (self, max_attendie):
        self.max_attendie = max_attendie
        self.attendants=[]

    def add_attendant(self,student):
        self.attendants.append(student)
       
        if self.space_available()==0:
            return False
        self.attendants.append(student)
        return True

    def space_available(self):
        return self.max_attendie-len(self.attendants)

# creating an instance of an Object
python_class=ZoomCall(5)
waiting_room=["Sarah","Sindet","Amina","Shadya","Juliet","Sharon","Veronicah","Nashipai"]
for student in waiting_room:
    join=python_class.add_attendant(student)
    if join:
        print(f"{student} has joined the meeting")
    else:
        print(f"We are sorry timeout{student}")



