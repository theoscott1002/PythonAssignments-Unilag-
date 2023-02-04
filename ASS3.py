# QUESTION3:Write a Python program to find the sum of two given integers. However, if the sum is
# between 15 and 20 it will return 20

# Getting first number from user
Num1 = float(input("Please input first Number:"))

# Getting second number from user
Num2 = float(input("Please input second number:"))
# Summation of both numbers
Sum = Num1 + Num2

# Printing 20 for summation between 15 and 20
if 15 <= Sum <= 20:
    print("The answer is: 20")

else:
    print("The sum is :" + str(Sum))
