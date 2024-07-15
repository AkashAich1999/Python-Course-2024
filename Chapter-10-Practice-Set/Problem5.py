# 5. Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) 
# and get fare information of train running under Indian Railways. 

from random import randint
# import random

class Train:

    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self, fro, to):
        print(f"Ticket is Booked for Train No: {self.trainNo} from {fro} to {to}")

    def getStatus(self):
        print(f"Train No: {self.trainNo} is running on time.")

    def getFare(self, fro, to):
        print(f"Ticket Fare for Train No: {self.trainNo} from {fro} to {to} is {randint(222, 5555)}")

t = Train(123599)
t.getFare("Jorhat", "Gandhinagar")
t.book("Jorhat", "Gandhinagar")
t.getStatus()