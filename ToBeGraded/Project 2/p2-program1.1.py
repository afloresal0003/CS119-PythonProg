'''
Programmer: Anthony Flores-Alvarez
Course: CS 119 Section #24321
Description: This program will mimic a coffee vending machine interface
It will allow users to select a menu item, tell them the price of the item,
and accept money for the item transaction. It will then perform a set of 
actions based on the money entered by the user. 
 Date: September 27, 2020
'''

#Header of program to make it look nice
print(" ")
print("----------------------")
print("Welcome to Cole's Coffee!")
print("----------------------")
print("Here's the menu: ")
print("- Small Coffee (S)         $1.00")
print("- Medium Coffee (M)       $1.50")
print("- Large Coffee (L)        $2.00")
print("----------------------")

# Asking for the user to make a choice
coffeeChoice = str(input(("What coffee size would you like? (case-sensitive): ")))

# Actions based on the users choice

if coffeeChoice == "S" or coffeeChoice == "s" or coffeeChoice == "small" or coffeeChoice == "Small":
    print(" ")
    print("----------------------")
    print("You chose a Small. Great choice!")
    print("----------------------")
    print("Your total will be: $1.00")
    # Asking them to enter the value they will pay
    userMoney = float(input("Enter how much you will be paying (ex: '1.00'): $"))
    # If they entered more or equal to than the price, then it will complete the transaction
    # and show them their change.
    if userMoney >= 1.00:
        print(" ")
        print("----------------------")
        print("You paid: ${:.2f}".format(userMoney))
        print(" ")
        print("Your change is: ${:.2f}".format(userMoney - 1.00))
        print(" ")
        print("----------------------")
        print("Enjoy your Coffee! :)")
        print("----------------------")
        exit()
    # If not it will terminate the program
    else:
        print(" ")
        print("----------------------")
        print("Sorry! Insufficient funds. Restart the program, and try again!")
        print("----------------------")
        exit()
    
if coffeeChoice == "M" or coffeeChoice == "m" or coffeeChoice == "medium" or coffeeChoice == "Medium":
    print(" ")
    print("----------------------")
    print("You chose a Medium. Great choice!")
    print("----------------------")
    print("Your total will be: $1.50")
    # Asking them to enter the value they will pay
    userMoney = float(input("Enter how much you will be paying (ex: '1.50'): $"))
    # If they entered more or equal to than the price, then it will complete the transaction
    # and show them their change.
    if userMoney >= 1.50:
        print(" ")
        print("----------------------")
        print("You paid: ${:.2f}".format(userMoney))
        print(" ")
        print("Your change is: ${:.2f}".format(userMoney-1.50))
        print(" ")
        print("----------------------")
        print("Enjoy your Coffee! :)")
        print("----------------------")
        exit()
    # If not it will terminate the program
    else:
        print(" ")
        print("----------------------")
        print("Sorry! Insufficient funds. Restart the program, and try again!")
        print("----------------------")
        exit()

if coffeeChoice == "L" or coffeeChoice == "l" or coffeeChoice == "large" or coffeeChoice == "Large":
    print(" ")
    print("----------------------")
    print("You chose a Large. Great choice!")
    print("----------------------")
    print("Your total will be: $2.00")
    # Asking them to enter the value they will pay
    userMoney = float(input("Enter how much you will be paying (ex: '2.00'): $"))
    # If they entered more or equal to than the price, then it will complete the transaction
    # and show them their change.
    if userMoney >= 2.00:
        print(" ")
        print("----------------------")
        print("You paid: ${:.2f}".format(userMoney))
        print(" ")
        print("Your change is: $", (userMoney - 2.00))
        print(" ")
        print("----------------------")
        print("Enjoy your Coffee! :)")
        print("----------------------")
        exit()
    # If not it will terminate the program
    else:
        print(" ")
        print("----------------------")
        print("Sorry! Insufficient funds. Restart the program, and try again!")
        print("----------------------")
        exit()
#If any other choice was inputted, it'll terminate the program.
else:
    print("Sorry! Invalid choice. Restart the program, and try again!")
    exit()