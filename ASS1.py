# QUESTION1: Write a Python program to find those numbers which are divisible by 7 and multiple of 5,
# between 1500 and 2700 (both included).


print("Numbers divisible by 7 and are multiple of 5 btw 1500 & 2700 are:")
# Creating an empty list
numList = []

# Iterating the integers from 1500 to 2700
for i in range(1500, 2701):
    # Checking for numbers divisible by 7 and are multiple of 5
    if (i % 7 == 0) and (i % 5 == 0):
        numList.append(str(i))

print(','.join(numList))
