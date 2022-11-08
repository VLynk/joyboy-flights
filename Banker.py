import Ticket
import UAM
import random

def Card():
    cardNo = input("Enter your card no +> ")
    cvv = input("Enter CVV +> ")
    expDate = input("Enter expiry date +> ")

    if random.randrange(0, 100) < 55:
        print("Card accepted! Printing Reciept")
    else:
        print("Card Declined! Try Again")
        Ticket.Ticketer(UAM.userLoginName)
