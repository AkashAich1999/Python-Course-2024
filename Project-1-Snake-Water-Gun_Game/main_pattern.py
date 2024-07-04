# -1 for Water
#  0 for Snake
#  1 for Gun

import random

computer = random.choice([-1, 0, 1])
youStr = input("Enter your choice: ")
youDict = {"w":-1, "s":0, "g":1}
reverseDict = {-1:"Water", 0:"Snake", 1:"Gun"}

you = youDict[youStr]

print(f"You choose {reverseDict[you]}\nComputer choose {reverseDict[computer]}")

if(computer == you):
    print("It's a Draw !")

else:
    '''
     if(computer == -1 and you == 1): (computer - you) = -2
        print("You Lose!")

    elif(computer == -1 and you == 0): (computer - you) = -1
        print("You Win!")

    elif(computer == 1 and you == -1): (computer - you) = 2
        print("You Win!")

    elif(computer == 1 and you == 0): (computer - you) = 1
        print("You Lose!")

    elif(computer == 0 and you == -1): (computer - you) = 1
        print("You Lose!")

    elif(computer == 0 and you == 1): computer - you) = -1
        print("You Win!") 

        The below logic is written on the basis of the value of computer - you
        You Win: -1, 2
        You Lose: -2, 1
    '''

if((computer - you) == -1 or (computer - you) == 2):
    print("You Win!")
else:
    print("You Lose!")        