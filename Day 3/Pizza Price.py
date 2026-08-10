print("Welcome to Python Pizza")
size = input("What is the size of the pizza? S , M or L?")
pep = input("Do you want Pepperoni on it? Y or N?")
cheese = input("Do you want extra cheese? Y or N?")

bill= 0

if size == 'S':
    bill = 15
    if pep == 'Y':
        bill += 2
    if cheese == 'Y':
        bill += 1

elif size == 'M':
    bill = 20
    if pep == 'Y':
        bill += 3
    if cheese == 'Y':
        bill += 1

elif size == 'L':
    bill = 25
    if pep == 'Y':
        bill +=3
    if cheese == 'Y':
        bill += 1
        
else:
    print("Wrong Input")
        
print(f"Your Total Bill is {bill}")