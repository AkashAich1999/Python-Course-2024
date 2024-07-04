# Requires 2 Players both have to select something from Snake or Water or Gun.

# Following are the rules of the game:
# Snake vs. Water: Snake drinks the water hence wins.
# Water vs. Gun: The gun will drown in water, hence a point for water
# Gun vs. Snake: Gun will kill the snake and win.
# If Both Players choose same thing, then it will be a Draw.

# Let's Mark:
# -1 for Water
#  0 for Snake
#  1 for Gun
import random

# computer = -1
computer = random.choice([-1, 0, 1])
youStr = input("Enter your choice: ")
youDict = {"w":-1, "s":0, "g":1}
reverseDict = {-1:"Water", 0:"Snake", 1:"Gun"}

you = youDict[youStr]

print(f"You choose {reverseDict[you]}\nComputer choose {reverseDict[computer]}")

if(computer == you):
    print("It's a Draw !")

else:
    if(computer == -1 and you == 0):
        print("You Win !")

    elif(computer == -1 and you == 1):
        print("You Lose !")

    elif(computer == 0 and you == -1):
        print("You Lose !")

    elif(computer == 0 and you == 1):
        print("You Win !")

    elif(computer == 1 and you == -1):
        print("You Win !")

    elif(computer == 1 and you == 0):
        print("You Lose !")

    else:
        print("Something went wrong !")