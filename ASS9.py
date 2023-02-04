# QUESTION9. Write a program to create a function that takes two arguments, name and age, and print
# their value.

def person(name, age):
    print("Your name is" + " " + name + " " + "and you are" + " " + age + " " + "years old")


name = input("Please enter your name:")
age = input("Please enter your age:")
person(name, age)
