print("Welcome to my computer quiz!")

playing = input("Do you want to play?  Yes/No: >>>>     :")
playing = playing.lower()

if playing == "no":
    print("Good bye!")
    quit()

print("Okay, lets play!")

answer = input("What does CPU stand for")
answer = answer.lower()
if answer == "central procesing unit":
    print("Correct")
else:
    print("Shao Kahn: You suck!")