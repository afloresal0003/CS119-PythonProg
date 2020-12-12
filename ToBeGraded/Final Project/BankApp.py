'''
Programmer: Anthony Flores-Alvarez
Course: CS 119 Section #24321
Description: This program will simulate a banking application. Users must 
enter a username and password to begin program and then a menu will pop 
up with options for the user to choose from: deposity money, withdraw money, 
display balance, change user, add new client, and exit. Program will loop 
until the user enters the exit option. It receives the required usernames, 
passwords, and balances from a text file called UserInformation.txt
This file is updated when the user exits.
Date: December 8, 2020
'''

# To help find path to userInformation.txt file
from pathlib import Path

# READ & POPULATE FUNCTION
# Reads a passed file name and uses the info to 
# populate the usernames, passwords, and balances
def ReadFile(fileName):
    
    # Creating path to file
    path = Path(__file__).parent / fileName
    # Opening the file as userFile
    with path.open("r") as userFile:
        
        # Storing the info in the user's file
        # Starts reading after line 2 to skip the header lines
        lines = userFile.readlines()[2:]
        
        #Initializing lists to store user info
        userName = []
        passWord = []
        balances = []
        
        # Populating lists
        for l in lines:
            as_list = l.split(" ")
            userName.append(as_list[0])
            passWord.append(as_list[1].replace("\n", ""))
            balances.append(float(as_list[2].replace("\n", "")))
        
        # Returning populated lists
        return userName, passWord, balances
        
# DEPOSIT FUNCTION
# Deposits user-defined quantity of money
# into the current user's account and updates
# the user's account balance
def Deposit(amount, balanceList, index):
    
    # Depositing
    balance = float(balanceList[index])
    newBalance = amount + balance
    # Updating the balance
    balanceList[index] = newBalance

# WITHDRAW FUNCTION
# Withdraws user-defined quantity of money
# from the current user's account and updates
# the user's account balance
def Withdraw(amount, balanceList, index):
    
    # Withdrawing
    balance = float(balanceList[index])
    newBalance = balance - amount
    # Updating the balance
    balanceList[index] = newBalance

# SHOW BALANCE FUNCTION
# Displays the current client's balance
def ShowBalance(userNameList, balanceList, index):
    
    print(userNameList[index],"'s Balance: ${:.2f}".format(float(balanceList[index])))

# CHANGE USER FUNCTION
# Changes the client by asking for new client credentials
def ChangeUser(userNameList, passwordList, balanceList):
    
    # Loop until they enter valid credentials
    while True:
        # Ask for credentials (user name & password)
        userName = input("Enter user name: ")
        passWord = input("Enter password: ")
        
        if userName in userNameList:
            
            index = userNameList.index(userName)
            
            if passWord == passwordList[index]:
                # Giving back the index to help maintain client throughout
                # program or until changed to a new one
                return index
      # Error Messages          
            else:
                print("\n-------------------------------------------------")
                print("Invalid user name and password. Please try again.")
                print("-------------------------------------------------\n")
                
        else:
            print("\n-------------------------------------------------")
            print("Invalid user name and password. Please try again.")
            print("-------------------------------------------------\n")

# ADD NEW USER FUNCTION
# Adds a new client to the list
def AddNewUser(newUsername, newPassword, newBalance, userNameList, passwordList, balanceList):
    
    userNameList.append(newUsername)
    passwordList.append(newPassword)
    balanceList.append(newBalance)

# UPDATE FILE FUNCTION 
# Updates the input file "UserInformation.txt" with updated balances
# and/or clients
def UpdateFile(fileName, userNameList, passwordList, balanceList):
    
    # Creating path to file
    path = Path(__file__).parent / fileName
    
    # Opening the file as userFile
    with path.open("w") as userFile:
        
        # Updating the file
        for i in range(0, (len(userNameList) + 2)):
            # RE-do the header lines
            if(i == 0):
                updatedLine = "userName passWord Balance\n"
                userFile.writelines(updatedLine)
            elif(i == 1):
                updatedLine = "=========================\n"
                userFile.writelines(updatedLine)
            # Update file with new balances
            elif(i >= 2):
                updatedLine = str(userNameList[i-2]) + " " + str(passwordList[i-2]) + " " + str("{:.2f}".format(balanceList[i-2])) + "\n"
                userFile.writelines(updatedLine)

# NUMBER VALIDATOR
# Ensures the user enters a valid number
def numValidator(question):
    
    # Loops enter user enters valid input
    while True:
        try:
            userInput = float(input(question))
        # For values and types other than float 
        except ValueError:
            print("\nError! Please enter a valid number!")
            continue
        # For negative values
        if (userInput < 0):
            print("\nError! Please enter a positive number!")
            continue
        # When VALID
        else:
            return userInput
            break

# Beginning of program
if __name__ == "__main__":
    
    print("-------------------------------------------------")
    print("Welcome to Anthony's Bank App!")
    print("-------------------------------------------------")
    print("Entry is CASE-SENSITIVE!")
    print("-------------------------------------------------")
    
    # Reading the input file and storing the populated lists with user's info
    userNameList, passwordList, balanceList = ReadFile("UserInformation.txt")
    # Storing the index to know which client we are on
    index = ChangeUser(userNameList, passwordList, balanceList)
    
    # Continously displays the menu until user types the 
    # option E or e, to exit the program
    while True:
        
        # HEADING
        print("-------------------------------------------------")
        print("Anthony's Bank App!")
        # To let the user know which client they are on
        print("-------------------------------------------------")
        print("Hello, ", userNameList[index], "! :)")
        print("-------------------------------------------------\n")
        # MENU
        print("MENU: \n")
        print("Type D to deposit money")
        print("Type W to withdraw money")
        print("Type B to display Balance")
        print("Type C to change user, display user name")
        print("Type A to add new client")
        print("Type E to exit")
        print("\n-------------------------------------------------\n")
        
        # Asking for menu choice
        userInput = input("Enter your menu selection: ")
        
        # DEPOSIT
        if(userInput == 'D' or userInput == 'd'):
            
            print("\n-------------------------------------------------")
            print("Pre-Balance: ")
            ShowBalance(userNameList, balanceList, index)
            print("-------------------------------------------------\n")
            # Asking user to enter the amount to deposit
            amount = numValidator("Enter amount to deposit: $")
            # Calling Deposit function, passing amount as a parameter
            Deposit(amount, balanceList, index)
            # Displaying the new balance by calling ShowBalance function
            print("\n-------------------------------------------------")
            print("Post-Balance: ")
            ShowBalance(userNameList, balanceList, index)
            print("-------------------------------------------------\n")
            input("Press ENTER to continue: ")
            print("\n")
            
        # WITHDRAW
        elif(userInput == 'W' or userInput == 'w'):
            
            # Calling ShowBalance function before Withdraw function
            print("\n-------------------------------------------------")
            print("Pre-Balance: ")
            ShowBalance(userNameList, balanceList, index)
            print("-------------------------------------------------\n")
            amount = numValidator("Enter amount to withdraw: $")
            balance = float(balanceList[index])
            
            if (amount > balance):
                print("\n-------------------------------------------------")
                print("Sorry! Insufficient funds. Please try again!")
                print("-------------------------------------------------\n")
                input("Press ENTER to continue: ")
                print("\n")
                
            else:
                # Calling Withdraw function, passing the withdraw
                # amount as a parameter
                Withdraw(amount, balanceList, index)
                # Displaying the new balance to the user
                print("\n-------------------------------------------------")
                print("Post-Balance: ")
                ShowBalance(userNameList, balanceList, index)
                print("-------------------------------------------------\n")
                input("Press ENTER to continue: ")
                print("\n")
        
        # SHOW BALANCE
        elif(userInput == 'B' or userInput == 'b'):
            
            # Calling ShowBalance function to display the balance
            print("\n-------------------------------------------------")
            ShowBalance(userNameList, balanceList, index)
            print("-------------------------------------------------\n")
            input("Press ENTER to continue: ")
            print("\n")
        
        # CHANGE USER/CLIENT
        elif(userInput == 'C' or userInput == 'c'):
            
            print("\n-------------------------------------------------")
            print("Current User: ", userNameList[index])
            print("-------------------------------------------------")
            # Calling ChangeUser function to ask the user name and change
            # to a different customer
            index = ChangeUser(userNameList, passwordList, balanceList)
            print("\n-------------------------------------------------")
            print("User changed to: ", userNameList[index])
            print("-------------------------------------------------\n")
            input("Press ENTER to continue: ")
            print("\n")
        
        # ADD NEW USER/CLIENT
        elif(userInput == 'A' or userInput == 'a'):
            
            print("\n-------------------------------------------------")
            print("Current clients: ", userNameList)
            print("-------------------------------------------------\n")
            # Asking for username
            newUsername = input("Enter new client username: ")
            # Asking for password
            newPassword = input("Enter new client password: ")
            # Asking for balance
            newBalance = numValidator("Enter new client starting balance: $")
            # Calling AddNewUser function to add this info to the
            # appropiate lists which later on will be tranferred
            # to the UserInformation.txt file
            AddNewUser(newUsername, newPassword, newBalance, userNameList, passwordList, balanceList)
            print("\n-------------------------------------------------")
            print(newUsername," added!")
            print("\n")
            print("Updated clients:", userNameList)
            print("-------------------------------------------------\n")
            input("Press ENTER to continue: ")
            print("\n")
        
        # EXIT
        elif(userInput == 'E' or userInput == 'e'):
            
            # Terminating the program
            print("\n-------------------------------------------------")
            print("Thank you for using Anthony's Bank App! Have a nice day!")
            print("-------------------------------------------------\n")
            # Updating the UserInformation.txt file with the
            # correct updated balances and/or users if they were added
            UpdateFile("UserInformation.txt", userNameList, passwordList, balanceList)
            break
        
        # If the user types any other option:
        # Prompting the user that option is invalid
        else:
            print("\n-------------------------------------------------")
            print("Error! Invalid option. Please try again!")
            print("-------------------------------------------------\n")
            input("Press ENTER to continue: ")
            print("\n")
            
    