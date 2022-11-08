# User Authentication Manager (U A M)
# This module deals with signing and registering a user

import TaFControl as TaF
import time

# Signing in a user
def SignIn():
    print("+====+ Welcome to Joyboy's Flights +====+ \n +===+ Account Registration +===+")
    userAccountName = input(" Enter your account name +> ")
    userAccountPassword = input(" Enter Password +> ")
    userAccountPasswordConfirm = input(" Re-enter your password +> ")

    if (userAccountPasswordConfirm == userAccountPassword):
        credentialsRecord = {}
        credentialsRecord[userAccountName] = userAccountPasswordConfirm
        
        with open("credentials.txt", "a") as credentials:
            credentials.write("%$" + userAccountName + "%$" + userAccountPasswordConfirm)
        credentials.close()
        print(" Account added!")
    else:
        print(" Passwords dont match!")

# Logging in a user
def Login():
    print("+====+ Welcome to Joyboy's Flights +====+ \n +===+ Account Login +===+")
    userLoginName = input(" Enter your account name +> ")
    userLoginPassword = input(" Enter your password +> ")

    with open("credentials.txt", "r") as credentials:
        allAccountsRecords = credentials.read()
        allAccounts = allAccountsRecords.split("%$")
        
        accountNames = []
        accountPasswords = []
        
        for account in allAccounts[1::2]:
            accountNames.append(account)
        
        for account in allAccounts[2::2]:
            accountPasswords.append(account)
            
        if userLoginName in accountNames:
            if userLoginPassword in accountPasswords:
                print(" Log in successfull!")
                TaF.Hub()
            else:
                print(" Entered password is wrong!")
        else:
            print(" No such account!")

# TicketModules
userLoginName = ''
userLoginPassword = ''

# Login/RegisterMenu
while True:
    print("+====+ Welcome to Joyboy's Flights +====+ \n 1 : Register account\n 2 : Login to existing account")
    logMenuChoice = int(input(" Enter your option number \n +>  "))
    logMenuOptions = {1 : SignIn, 2 : Login}
    func = logMenuOptions.get(logMenuChoice, 1)
    func()


