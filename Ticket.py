from datetime import datetime 
import TaFControl
import Banker
import csv
import UAM

cardStatus = 0

def Ticketer(currentUser: str):
    print("+====+ Billing +====+")
    chosenFlight = input("Enter the flight number of your chosen flight +> ")
    paymentMethod = input("Enter your payment method +> ")

    with open("flights.csv", 'r') as flights:
        flightsReader = csv.reader(flights)
        allFlightsDetails = []
        allFlights = []

        for flightDetails in flightsReader:
            allFlights.append(flightDetails)

        for currentFlightDetails in allFlights[1::]:
            allFlightsDetails.append(currentFlightDetails)
            
    for flight in allFlightsDetails:
        if flight != []:
            if flight[0] == chosenFlight:
                flightId = flight[0]
            payment = flight[5]

    if paymentMethod.upper() == "CARD":
        Banker.Card()
        Receipt(UAM.userLoginName, payment, paymentMethod.upper(), flightId)

def Receipt(currentuser: str, payment: int, paymentMethod: int, chosenFlightNumber: str):
    currentDateTime = datetime.now()
    print(payment)
    print(paymentMethod)
    print(currentuser)
    print(chosenFlightNumber)
    print(currentDateTime)
    TaFControl.TaFMenu()