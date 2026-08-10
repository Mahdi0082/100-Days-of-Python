print("Welcome to Tressure Island")
first = input("You are at a crossroad, Do you want to go left or right? (use l or r)")

if first == 'r':
    print("You fell into a hole, Game Over")
elif first =='l':
    second = input("You've reached to a lake, Do you want to swim or wait?")
    if second == 'swim':
        print("There was a shark waiting, Game Over")
    elif second == 'wait':
        third= input("You have arrived to the island unharmed. There is a house with 3 doors, red, yellow and blue. Which one do you choose?")
        if third =='red' or third =='blue':
            print("There was fire in it, Game over")
        elif third == 'yellow':
            print("Congratulations, You have found the tressure!")
        else:
            print("Wrong Input")
    else:
        print("Wrong Input")
else:
    print("Wrong Input")