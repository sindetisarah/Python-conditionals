import sys
try:
    x=int(input("x:"))
except ValueError:
    print("Please input an integer")
    sys.exit(1)

y=int(input("y:"))


try:
    operation=x/y

except ZeroDivisionError:
    print("Error: Cannot divide by zero")
    sys.exit(1)
print("The result of {} divided by{} is{}".format(x,y,operation))
print(f"{x} divided by {y} is {operation}")


# handling the exeception in a more graceful  way

