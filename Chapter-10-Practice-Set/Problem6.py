# 6. Can you change the self-parameter inside a class to something else (say “harry”). 
# Try changing self to “slf” or “akash” and see the effects.

from random import randint
# import random

class Train:

    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(slf, fro, to):
        print(f"Ticket is Booked for Train No: {slf.trainNo} from {fro} to {to}")

    def getStatus(self):
        print(f"Train No: {self.trainNo} is running on time.")

    def getFare(akash, fro, to):
        print(f"Ticket Fare for Train No: {akash.trainNo} from {fro} to {to} is {randint(222, 5555)}")

t = Train(123599)
t.getFare("Jorhat", "Gandhinagar")
t.book("Jorhat", "Gandhinagar")
t.getStatus()