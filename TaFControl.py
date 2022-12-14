###############################
# importing the required imports
# Required modules : csv, UAM, random, Ticket
###############################
try : import csv
except ModuleNotFoundError: print("csv Module Missing")
try : import UAM
except ModuleNotFoundError: print("UAM Module Missing")
try : import random
except ModuleNotFoundError: print("random Module Missing")
try : import Ticket
except ModuleNotFoundError: print("Ticket Module not found")

###############################
# Adding Flights
# Create a random flight number : User adds callsign, name, model, price, departure, arrvial of flight 
###############################
def AddFlights():
    with open("flights.csv", "a") as flights:
        flightsWriter = csv.writer(flights)
        print("+====+ Welcome to Joyboy's Flights +====+ \n +===+ Enter Journey Details +===+")
        flightDetails = [
            " Enter the aircraft callsign", 
            " Enter the company name of the aircraft", 
            " Enter the aircraft model", 
            " Enter the aircraft seating capacity", 
            " Enter the ticket price (in Rs)", 
            " Enter the flight's departure airport", 
            " Enter the flight's arrival airport"]
        addedFlightDetails = []
        randFlightnumber = random.randrange(100000, 999999)
        addedFlightDetails.append(randFlightnumber)

        for query in flightDetails:
            print(query)
            addedFlightDetails.append(input(" +> "))

        flightsWriter.writerow(addedFlightDetails)
    Hub()

###############################
# Checking Flights
# Prints all flights in tabular form 
# Known issue : Header appears in a offseted place
###############################
def CheckFlights():
    with open("flights.csv", 'r') as flights:
        flightsReader = csv.reader(flights)
        allFlightsDetails = []
        allFlights = []

        for flightDetails in flightsReader:
            allFlights.append(flightDetails)

        for currentFlightDetails in allFlights[1::]:
            allFlightsDetails.append(currentFlightDetails)
    print(" Details of Flights given belown")
    flightHeader = ["Flight Number", "Callsign", "Company", "Aircraft Model", "Seating capacity", "Ticket Cost", "Departure", "Arrival"]
    print(f'{flightHeader[0]} \t {flightHeader[1]} \t {flightHeader[2]} \t {flightHeader[3]} \t {flightHeader[4]} \t {flightHeader[5]} \t {flightHeader[6]} \t {flightHeader[7]}')
    for flight in allFlightsDetails:
        if flight != []:
            print(flight[0],"\t", flight[1], "\t", flight[2], "\t", flight[3], "\t", flight[4], "\t", flight[5], "\t", flight[6], "\t", flight[7])
    Hub()

###############################
# Buying ticket
# Calls another Module
###############################
def  BuyTicket():
    Ticket.Ticketer(UAM.userLoginName)

###############################
# Hub
# Main menu to call function
###############################
def Hub():
    print("+====+ Welcome to Joyboy's Flights Main Hub +====+ \n 1 : Check all current flights \n 2 : Buy a ticket")
    choice = int(input(" Enter the number of your choice \n +> "))
    options = {1 : CheckFlights, 2 : BuyTicket, 3 : AddFlights}
    action = options.get(choice, 1)
    action()

###############################