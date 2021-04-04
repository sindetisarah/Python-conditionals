number=int(input("Number:"))
if (number > 0):
    print("number is positive","\n")
elif (number < 0):
    print("number is negative","\n")  
else:
    print("number is zero","\n") 

    # Finding whether an year is a leap year     
year=int(input("Enter year:"))
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print(f"{year} is  a leap year")
       else:
           print(f"{year} is not a leap year")
   else:
       print(f"{year}is not a leap year")
else:
   print(f"{year}is not a leap year")

   