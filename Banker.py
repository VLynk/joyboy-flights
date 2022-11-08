import Ticket
import UAM
import random

def Card():
    cardNo = input("Enter your card no, ie (1234 5678 9012 3456) \n +> ")
    cvv = input("Enter CVV, ie (123) \n +> ")
    expDate = input("Enter expiry date, ie (mm/yy) \n +> ")
    cardlist = []

    cvv = int(cvv)

    for i in cardNo.split():
        for j in i.split():
            cardlist.append(int(j))

    if CardVerification(cardlist, cvv, expDate) == "verification complete":
        return "Card is verified", cardNo, expDate
    else:
        return "Card is Invalid" 

def CardVerification(cardList, cvv : int, expDate : str):
    cardSum = 0
    dateValues = []
    cardState = False
    cvvState = False
    expdateState = False


    for k in cardList:
        cardSum += k

    if len(str(cvv).split()) == 3:
        cvvState = True
    else:
        cvvState = True

    for i in expDate.split("/"):
        dateValues.append(i)

    if int(dateValues[0]) in [1, 2, 3, 4, 5, 6, 7, 8 ,9 ,10, 11, 12]:
        if int(dateValues[1]) <= 27 and int(dateValues[1]) >= 23:
            expdateState = True
        else:
            expdateState = False 
    else:
        expdateState = False

    if cardSum % 10 == 0:
        cardState = True
    else:
        cardState = False

    if cardState == True and cvvState == True and expdateState == True:
        return "verification complete"
    else:
        return "verfication failed"