# Import
try:from tabulate import tabulate
except: print("TabulateNotFoundError(Error:1750)")
try:import mysql.connector as pyQL;
except: print("MySQLConnectorNotFoundError(Error:1750)")
try: from datetime import date
except: print("DateTimeNotFoundError(Error:1750)")

#Connect to SQL server
db = pyQL.connect(
    host= 'localhost',
    user= 'root',
    password= 'lynk',
    database= 'sekaisaikyounokuko' )
cur = db.cursor()

# Main Menu 
def MainMenu():
    _options = [["1 : Show all Flights"], ["2 : Show all Customers"], ["3 : Add a Flight"], ["4 : Buy a Ticket"], ["5 : Exit"]]
    print(tabulate(tabular_data= _options, headers= ["Yokoso kono sekai saikyou no kuko"], tablefmt= 'fancy_outline'))
    _choice = int(input(("+> ")))
    _choiceOptions = {1: ShowFlightsMenu, 2: ShowRecentCustomerMenu, 3: AddFlightsMenu, 4: BuyTicketMenu, 5: ExitMenu}
    action = _choiceOptions.get(_choice)
    action()

def ShowFlightsMenu():
    _options = [["1 : Sort by Flight No"], ["2 : Sort by Flight Capacity"], ["3 : Sort by Destination"], ["4 : Sort by Ticket Price"], ["5 : Back to Main Menu"]]
    print(tabulate(tabular_data= _options, headers= ["Sorting Options"], tablefmt= 'fancy_outline'))
    _choice = int(input(("+> ")))

    if _choice == 1:
        try: cur.execute('''select * from flights order by flightNo asc;''')
        except: ShowFlightsMenu()
        flights = cur.fetchall()
        print(tabulate(tabular_data= flights, headers=["Flight No", "Flight Capacity", "To", "Ticket Price"], tablefmt='fancy_outline'))
    elif _choice == 2:
        try: cur.execute('''select * from flights order by capacity asc;''')
        except: ShowFlightsMenu()
        flights = cur.fetchall()
        print(tabulate(tabular_data= flights, headers=["Flight No", "Flight Capacity", "To", "Ticket Price"], tablefmt='fancy_outline'))
    elif _choice == 3:
        try: cur.execute('''select * from flights order by arrivalLoc asc;''')
        except: ShowFlightsMenu()
        flights = cur.fetchall()
        print(tabulate(tabular_data= flights, headers=["Flight No", "Flight Capacity", "To", "Ticket Price"], tablefmt='fancy_outline'))
    elif _choice == 4:
        try: cur.execute('''select * from flights order by ticketPrice asc;''')
        except: ShowFlightsMenu()
        flights = cur.fetchall()
        print(tabulate(tabular_data= flights, headers=["Flight No", "Flight Capacity", "To", "Ticket Price"], tablefmt='fancy_outline'))
    elif _choice == 5:
        MainMenu()
    
    ShowFlightsMenu()

def ShowRecentCustomerMenu():
    try: cur.execute('''select * from customers order by customerNo desc ;''')
    except: ShowRecentCustomerMenu()
    customers = cur.fetchall()
    print(tabulate(tabular_data= customers, headers=["Customer No", "Customer Name", "Customer Flight No", "Purchase Date"], tablefmt='fancy_outline'))
    MainMenu()

def AddFlightsMenu():
    _flightDetails = ["Flight No", "Flight Capacity", "Flight Destination", "Ticket Price"]
    flightDetails = []
    for _detail in range(4):
        flightDetails.append(input(f"Enter {_flightDetails[_detail]} +> "))
    try: cur.execute(f'''insert into flights values ('{flightDetails[0]}', {flightDetails[1]}, '{flightDetails[2]}', {flightDetails[3]});'''); db.commit(); print("Given Flight has been added!")
    except: db.rollback(); AddFlightsMenu()

def BuyTicketMenu():
    _userDetails = ["Customer Name", "Customer Flight No"]
    userDetails = []
    cur.execute('''select max(customerNo) from customers;''')
    customerNo = int(cur.fetchone()[0]) + 1
    currentDT = date.today()
    for _detail in range(2):
        userDetails.append(input(f"Enter {_userDetails[_detail]} +> " ))
    try:
        cur.execute(f'''insert into customers values ({customerNo}, '{userDetails[0]}', '{userDetails[1]}', '{currentDT}');'''); db.commit(); print("Ticket Bought!")
    except: db.rollback(); BuyTicketMenu()
    MainMenu()
    
def ExitMenu():
    exit()

while True:
    MainMenu()