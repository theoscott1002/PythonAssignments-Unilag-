# QUESTION6:Write a program to accept percentage from the user and display the grade according to
# the following criteria:
# Marks Grade
# > 90 A
# > 80 and <= 90 B
# >= 60 and <= 80 C
# below 60 D

# Getting input from user
score = float(input("Please input percentage:"))

if score < 60:
    print("Grade: D")

elif 60 <= score <= 80:
    print("Grade: C")

elif 80 < score <= 90:
    print("Grade: B")

elif score > 90:
    print("Grade: A")
