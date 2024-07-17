# We are going to write a program that generates a Random Number and asks the user to Guess it. 
# If the player’s Guess is Higher than the actual number, the program displays “Lower number please”. 
# Similarly, if the user’s guess is too low, the program prints “higher number please”. 
# When the user guesses the correct number, the program displays the number of guesses the player used to arrive at the number. 
# Hint: Use the random module. 

import random
n = random.randint(1, 100)
a = -1
guessNo = 0

while(a != n):
    a = int(input("Guess The Number :"))
    guessNo += 1
    if(a > n):
        print("Lower Number Please !")
    elif(a < n):
        print("Higher Number Please !")
    else:
        print(f"{guessNo} is the Numbers of Guesses/Attempts Required by the Player to reach The Random Number {n}")        