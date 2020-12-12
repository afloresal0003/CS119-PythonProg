'''
Programmer: Anthony Flores-Alvarez
Course: CS 119 Section #24321
Description: This program will mimic a coffee vending machine interface
It will allow users to select a menu item, tell them the price of the item,
and accept money for the item transaction. It will then perform a set of 
actions based on the money entered by the user. 
Note for Professor: I simply copied my program 2 and modified it.
 Date: September 27, 2020
'''

#Header of program to make it look nice
print(" ")
print("----------------------")
print("Welcome to Cole's Cafe!")
print("----------------------")
print("Here's the menu: ")
print("- Espresso (Small: $1.00 | Medium: $2.00 | Large: $3.00")
print("- Americano (Small: $1.00 | Medium: $2.00 | Large: $3.00")
print("- Cappucino (Small: $1.00 | Medium: $2.00 | Large: $3.00")
print("- Latte (Small: $1.00 | Medium: $2.00 | Large: $3.00")
print("----------------------")

# Price of a small coffee
smallCoffeePrice = 1.00
# Asking for the user to make a choice
coffeeChoice = str(input(("What drink would you like? (case-sensitive): ")))

# Actions based on the users choice

if coffeeChoice == "Espresso" or coffeeChoice == "espresso":
    print(" ")
    print("----------------------")
    print("You chose a small Espresso. Great choice!")
    print("----------------------")
    print("Your total will be: $1.00")
    # Asking them to enter the value they will pay
    userMoney = float(input("Enter how much you will be paying (ex: '1.00'): $"))
    # If they entered more or equal to than the price, then it will complete the transaction
    # and show them their change.
    if userMoney >= smallCoffeePrice:
        print(" ")
        print("----------------------")
        print("You paid: ${:.2f}".format(userMoney))
        print(" ")
        print("Your change is: ${:.2f}".format(userMoney - smallCoffeePrice))
        print(" ")
        print("----------------------")
        print("Enjoy your Espresso! :)")
        print("----------------------")
        exit()
    # If not it will terminate the program
    else:
        print(" ")
        print("----------------------")
        print("Sorry! Insufficient funds. Restart the program, and try again!")
        print("----------------------")
        exit()
    
if coffeeChoice == "Cappucino" or coffeeChoice == "cappucino":
    print(" ")
    print("----------------------")
    print("You chose a small Cappucino. Great choice!")
    print("----------------------")
    print("Your total will be: $1.00")
    # Asking them to enter the value they will pay
    userMoney = float(input("Enter how much you will be paying (ex: '1.00'): $"))
    # If they entered more or equal to than the price, then it will complete the transaction
    # and show them their change.
    if userMoney >= smallCoffeePrice:
        print(" ")
        print("----------------------")
        print("You paid: ${:.2f}".format(userMoney))
        print(" ")
        print("Your change is: ${:.2f}".format(userMoney - smallCoffeePrice))
        print(" ")
        print("----------------------")
        print("Enjoy your Cappucino! :)")
        print("----------------------")
        exit()
    # If not it will terminate the program
    else:
        print(" ")
        print("----------------------")
        print("Sorry! Insufficient funds. Restart the program, and try again!")
        print("----------------------")
        exit()

if coffeeChoice == "Americano" or coffeeChoice == "americano":
    print(" ")
    print("----------------------")
    print("You chose a small Americano. Great choice!")
    print("----------------------")
    print("Your total will be: $1.00")
    # Asking them to enter the value they will pay
    userMoney = float(input("Enter how much you will be paying (ex: '1.00'): $"))
    # If they entered more or equal to than the price, then it will complete the transaction
    # and show them their change.
    if userMoney >= smallCoffeePrice:
        print(" ")
        print("----------------------")
        print("You paid: ${:.2f}".format(userMoney))
        print(" ")
        print("Your change is: $", (userMoney - smallCoffeePrice))
        print(" ")
        print("Price Multiplier: 3")
        print(" ")
        print("----------------------")
        print("Enjoy your Americano! :)")
        print("----------------------")
        exit()
    # If not it will terminate the program
    else:
        print(" ")
        print("----------------------")
        print("Sorry! Insufficient funds. Restart the program, and try again!")
        print("----------------------")
        exit()
if coffeeChoice == "Latte" or coffeeChoice == "latte":
    print(" ")
    print("----------------------")
    print("You chose a small Latte. Great choice!")
    print("----------------------")
    print("Your total will be: $1.00")
    # Asking them to enter the value they will pay
    userMoney = float(input("Enter how much you will be paying (ex: '1.00'): $"))
    # If they entered more or equal to than the price, then it will complete the transaction
    # and show them their change.
    if userMoney >= smallCoffeePrice:
        print(" ")
        print("----------------------")
        print("You paid: ${:.2f}".format(userMoney))
        print(" ")
        print("Your change is: $", (userMoney - smallCoffeePrice))
        print(" ")
        print("Price Multiplier: 3")
        print(" ")
        print("----------------------")
        print("Enjoy your Latte! :)")
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