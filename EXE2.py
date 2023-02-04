# 2)Password Generator
# ● Ask user for their favorite color
# ● Ask user for their month of birth (The number)
# ● Ask user for their pet’s name
# ● Combine all these using string concatenation to form the password e.g. (Bruno12blue or
# yellowgrumpy5)

color = str(input("What is your favorite color:"))
birth_month = int(input("what is your birth month(1-12):"))
petName = str(input("What is your pet's name:"))
print("Your password is:" + petName + str(birth_month) + color)
