import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors "))
computer = random.randint(0 , 2)
if player == 0:
    print("Player chose rock")
    print(rock)

elif player == 1:
    print("Player chose paper")
    print(paper)
    
elif player == 2 :
    print("Player chose scissors")
    print(scissors)

    1
if player > 2:
    print("Wrong input")
else:
    
    print("Computer Chose : ")
    if computer == 0:
        print(rock)

    elif computer == 1:
        print(paper)

    else:
        print(scissors)

if player == 0 and computer == 1:
    print("Computer Wins")
elif player == 1 and computer == 2:
    print("Computer Wins")
elif player == 2 and computer == 0:
    print("Computer Wins")
elif player == computer:
    print("Draw")
else:
    print("You Won")