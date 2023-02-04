# QUESTION10. Define a function in python that accepts 3 values and returns the maximum of three
# numbers.

value1 = eval(input("Please enter first number:"))
value2 = eval(input("Please enter second number:"))
value3 = eval(input("Please enter third number:"))


def maximum_number(value1, value2, value3):
    print(max(value1, value2, value3))


maximum_number(value1, value2, value3)
