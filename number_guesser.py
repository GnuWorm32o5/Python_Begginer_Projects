import random

random = random.randrange(11)

guess = int(input("Try and guess a random number from 1 to 10 >> :"))

if random == guess:
    print("Correct!")
else:
    print("Wrong!")

print(r"It was:", random)