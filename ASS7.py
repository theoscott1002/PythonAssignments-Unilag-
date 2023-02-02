# QUESTION: Write a program to accept a number from 1 to 7 and display the name of the day like 1
# for Sunday , 2 for Monday and so on.

number = int(input("Please enter day number:"))

if number == 1:
    print("The day is: SUNDAY")

elif number == 2:
    print("The day is: MONDAY")

elif number == 3:
    print("The day is: TUESDAY")

elif number == 4:
    print("The day is: WEDNESDAY")

elif number == 5:
    print("The day is: THURSDAY")

elif number == 6:
    print("The day is: FRIDAY")

elif number == 7:
    print("The day is: SATURDAY")

else:
    print("INVALID OPERATION!!!")
