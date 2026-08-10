from posixpath import split
print("Welcome to the tip calculator.\n")

bill= float(input("How much was your total bill? "))
tip = int(input("What percentage do you want to tip? 10, 12, 15 or custom?"))
split = int(input("How many person are spliting the bill ?"))

tip_amount = bill *(tip/100)
amount_per_person = ((bill+tip_amount)/split)
print("Each Person will be paying : ",amount_per_person)
