from datetime import datetime 
import TaFControl
import Banker
import csv
import time

def Ticketer(currentUser: str):
    print("+====+ Billing +====+")
    chosenFlight = input("Enter the flight number of your chosen flight +> ")
    paymentMethod = "CARD"
        
    Banker.Card()
    Receipt(paymentMethod, chosenFlight)

def Receipt(paymentMethod: str, chosenFlightNumber: str):
    print("#######################################################")
    currentTime = datetime.now()
    print(f'Time of Purchase : {currentTime} \nPayment Status : Paid \nPaymentMethod : {paymentMethod} \nChosen Flight : {chosenFlightNumber}')
    print("######################################################")
    time.sleep(7)
    TaFControl.Hub()
