from datetime import datetime 
import TaFControl
import Banker
import csv
import time

def Ticketer(currentUser: str):
    print("+====+ Billing +====+")
    chosenFlight = input("Enter the flight number of your chosen flight +> ")
    cardDetails = Banker.Card()
    Receipt(cardDetails[1], cardDetails[2], chosenFlight)

def Receipt(cardNo : str, cardExpdate : str, chosenFlightNumber: str):
    print("#######################################################")
    currentTime = datetime.today()
    print(f'Time of Purchase : {currentTime} \nPayment Status : Paid \nPaymentMethod : Card \nCard Number : {cardNo} \nCard Expiry date : {cardExpdate} \nChosen Flight : {chosenFlightNumber}')
    print("######################################################")
    time.sleep(7)
    TaFControl.Hub()
