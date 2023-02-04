# QUESTION2:Write a Python program which iterates the integers from 1 to 50. For multiples of three
# print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers
# which are multiples of both three and five print "FizzBuzz".

# Creating an empty list
numList = []

# Iterating the integers from 1 to 50
for x in range(1, 50):
    # Fuzz for multiples of 3
    if (x % 3 == 0) and (x % 5 != 0):
        x = "Fizz"
        numList.append(str(x))
    # Buzz for multiples of 5
    elif (x % 5 == 0) and (x % 3 != 0):
        x = "Buzz"
        numList.append(str(x))
    # FizzBuzz for multiples of both 3 and 5
    elif (x % 3 == 0) and (x % 5 == 0):
        x = "FizzBuzz"
        numList.append(str(x))

print(','.join(numList))
