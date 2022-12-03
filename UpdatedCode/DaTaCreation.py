# Database and Table Creation

# Variables
_database = '''sekaisaikyounokuko'''
_table1 = '''flights'''
_table2 = '''customers'''
_exampleFlightNo = ['FL1252', 'GW3163', 'JE1474']
_exampleArrivalAirports = ['Dubai', 'Frankfurt', 'Heathrow']
_exampleCapacity = [129, 179, 189]
_exampleTicketPrice = [5510, 4957, 3500]
_exampleCustomerNo = [1, 2, 3]
_examplePurchaseDate = ["2015-03-24", "2019-03-21", "2022-01-08"] # BloodBorne release date , Sekiro release date , jojo pt 6 release
_exampleCustomerName = ['Hidetaka Miyazaki', 'Geniichiro Ashina', 'Giovanni Giorgio']

# Import
import mysql.connector as pyQL

# Server Connection
db = pyQL.connect(
    host = 'localhost',
    user = 'root',
    password = 'lynk' )

cur = db.cursor()

# Database Check and Creation
cur.execute('''show databases;''')
databases = list(cur.fetchall())
if _database not in databases:
    try :cur.execute(f'''create database {_database};''')
    except: pass

try: cur.execute(f'''use {_database};''')
except: pass

# Creating Tables
cur.execute('''show tables;''')
tables = list(cur.fetchall())
if _table1 not in tables:
    try: cur.execute(f'''create table {_table1} ( flightNo varchar(6) not null primary key, capacity int(3) not null, arrivalLoc varchar(32) not null, ticketPrice int(5) not null );''')
    except: pass

if _table2 not in tables:
    try: cur.execute(f'''create table {_table2} (customerNo int(6) not null primary key, customerName varchar(32) not null, customerFlightNo varchar(6) not null, purchaseDate date not null);''')
    except: pass

# Insert Example Values
for iCount in range(4):
    try: cur.execute(f'''insert into {_table1} values ('{_exampleFlightNo[iCount]}', {_exampleCapacity[iCount]}, '{_exampleArrivalAirports[iCount]}', {_exampleTicketPrice[iCount]});'''); db.commit()
    except: db.rollback; pass 

    try: cur.execute(f'''insert into {_table2} values ({_exampleCustomerNo[iCount]}, '{_exampleCustomerName[iCount]}', '{_exampleFlightNo[iCount]}', '{_examplePurchaseDate[iCount]}');'''); db.commit()
    except: db.rollback; pass 
