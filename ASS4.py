# QUESTION:Write a Python program to print a specified list after removing the 0th, 4th and 5th
# elements. Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']

# Initial list
fruits = ['Apple', 'Banana', 'Mango', 'PineApple', 'PawPaw', 'Orange', 'Watermelon', 'Grape']
print("OUR FAVOURITE FRUITS ARE:", fruits)

# Items to be removed
forbidden_fruits = {'Apple', 'PawPaw', 'Orange'}

new_fruits = [ele for ele in fruits if ele not in forbidden_fruits]

# Printing modified list
print("NEW LIST AFTER REMOVING FORBIDDEN FRUITS: ", new_fruits)
