birthdays = {'Theo': 'November 2', 'Samuel': 'August 20', 'Christiana': 'April 25', 'Peace': 'September 22', 'Emmanuel': 'March  13'}
name = input("Please input name:").title()
if name in birthdays:
    print(f"{birthdays[name]} is the the birthday of {name}")
else:
    print(f"I do not have birthday information for {name}")
