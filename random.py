import random
# random
random.seed(76)
number = random.randint(0, 10)
random.seed(73)
number2 = random.randint(0, 100)
print(number)
print(number2)

# rand-range

# random.random -- gives random numbers from 0 - 1
print(random.random())

# random.choice
choice = ["asdf", 1, 4, True, False, "what"]
print(random.choice(choice))

# random.shuffle
choice = ["asdf", 1, 4, True, False, "what"]
random.shuffle(choice)
print(choice)
