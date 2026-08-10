import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

X = random.choice(friends)
print(X,"is going to pay the bill")


#Alternative

Y = random.randint(0, len(friends)-1)
print(friends[Y],"is going to pay the bill")