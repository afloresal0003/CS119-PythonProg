'''
Programmer: Anthony Flores-Alvarez
Course: CS 119 Section #24321
Description: This program will mimic a coffee vending machine interface
It will allow users to select a menu item, tell them the price of the item,
and accept money for the item transaction. It will then perform a set of 
actions based on the money entered by the user. 
 Date: September 27, 2020
'''
print("---------------------------")
print("Welcome to Cole's Cafe! :)")

print("---------------------------")
print("Here's the menu: ")
print("- Espresso (Small: $1.00 | Medium: $2.00 | Large: $3.00")
print("- Americano (Small: $1.00 | Medium: $2.00 | Large: $3.00")
print("- Cappucino (Small: $1.00 | Medium: $2.00 | Large: $3.00")
print("- Latte (Small: $1.00 | Medium: $2.00 | Large: $3.00")
print("----------------------")

# Standard price of a coffee
coffePrice = 1.00
# The multipliers on the coffee price based on size
smallMultiplier = 1
mediumMultiplier = 2
largeMultiplier = 3
# Calculating new coffee prices based on multipliers
smallCoffeePrice = coffePrice * smallMultiplier
mediumCoffeePrice = coffePrice * mediumMultiplier
largeCoffeePrice = coffePrice * largeMultiplier

# Ask the user to input drink choice
coffeeChoice = input("What drink would you like?: ")

# Actions based on user input
'''
    ESPRESSO
'''
if coffeeChoice == "Espresso" or coffeeChoice == "espresso":
    # Asks the user for the drink size
    coffeeSize = input("What size would you like it?: ")
    
    # Actions based on size entered 
    '''
        SMALL ESPRESSO
    '''
    if coffeeSize == "small" or coffeeSize == "Small" or coffeeSize == "S" or coffeeSize == "s":
        print(" ")
        print("----------------------")
        print("You chose a small Espresso. Great choice!")
        print("----------------------")
        print("Your total will be: ${:.2f}".format(smallCoffeePrice))
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
    '''
        MEDIUM ESPRESSO
    '''
    if coffeeSize == "medium" or coffeeSize == "Medium" or coffeeSize == "M" or coffeeSize == "m":
        print(" ")
        print("----------------------")
        print("You chose a medium Espresso. Great choice!")
        print("----------------------")
        print("Your total will be: ${:.2f}".format(mediumCoffeePrice))
        # Asking them to enter the value they will pay
        userMoney = float(input("Enter how much you will be paying (ex: '2.00'): $"))
        # If they entered more or equal to than the price, then it will complete the transaction
        # and show them their change.
        if userMoney >= mediumCoffeePrice:
            print(" ")
            print("----------------------")
            print("You paid: ${:.2f}".format(userMoney))
            print(" ")
            print("Your change is: ${:.2f}".format(userMoney - mediumCoffeePrice))
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
    '''
        LARGE ESPRESSO
    '''
    if coffeeSize == "large" or coffeeSize == "Large" or coffeeSize == "L" or coffeeSize == "l":
        print(" ")
        print("----------------------")
        print("You chose a large Espresso. Great choice!")
        print("----------------------")
        print("Your total will be: ${:.2f}".format(largeCoffeePrice))
        # Asking them to enter the value they will pay
        userMoney = float(input("Enter how much you will be paying (ex: '3.00'): $"))
        # If they entered more or equal to than the price, then it will complete the transaction
        # and show them their change.
        if userMoney >= largeCoffeePrice:
            print(" ")
            print("----------------------")
            print("You paid: ${:.2f}".format(userMoney))
            print(" ")
            print("Your change is: ${:.2f}".format(userMoney - largeCoffeePrice))
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
    
    else:
        print("Invalid drink size. Restart the program and try again!")
        exit()

'''
    CAPPUCINO
'''
if coffeeChoice == "Cappucino" or coffeeChoice == "cappucino":
    # Asks the user for the drink size
    coffeeSize = input("What size would you like it?: ")
    
    #Actions based on size entered 
    '''
        SMALL CAPPUCINO
    '''
    if coffeeSize == "small" or coffeeSize == "Small" or coffeeSize == "S" or coffeeSize == "s":
        print(" ")
        print("----------------------")
        print("You chose a small Cappucino. Great choice!")
        print("----------------------")
        print("Your total will be: ${:.2f}".format(smallCoffeePrice))
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
            
    '''
        MEDIUM CAPPUCINO 
    '''
    if coffeeSize == "medium" or coffeeSize == "Medium" or coffeeSize == "M" or coffeeSize == "m":
        print(" ")
        print("----------------------")
        print("You chose a medium Cappucino. Great choice!")
        print("----------------------")
        print("Your total will be: ${:.2f}".format(mediumCoffeePrice))
        # Asking them to enter the value they will pay
        userMoney = float(input("Enter how much you will be paying (ex: '2.00'): $"))
        # If they entered more or equal to than the price, then it will complete the transaction
        # and show them their change.
        if userMoney >= mediumCoffeePrice:
            print(" ")
            print("----------------------")
            print("You paid: ${:.2f}".format(userMoney))
            print(" ")
            print("Your change is: ${:.2f}".format(userMoney - mediumCoffeePrice))
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
    '''
        LARGE CAPPUCINO 
    '''
    if coffeeSize == "large" or coffeeSize == "Large" or coffeeSize == "L" or coffeeSize == "l":
        print(" ")
        print("----------------------")
        print("You chose a large Cappucino. Great choice!")
        print("----------------------")
        print("Your total will be: ${:.2f}".format(largeCoffeePrice))
        # Asking them to enter the value they will pay
        userMoney = float(input("Enter how much you will be paying (ex: '3.00'): $"))
        # If they entered more or equal to than the price, then it will complete the transaction
        # and show them their change.
        if userMoney >= largeCoffeePrice:
            print(" ")
            print("----------------------")
            print("You paid: ${:.2f}".format(userMoney))
            print(" ")
            print("Your change is: ${:.2f}".format(userMoney - largeCoffeePrice))
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
    else:
        print("Invalid drink size. Restart the program and try again!")
        exit()

'''
    AMERICANO
'''
if coffeeChoice == "Americano" or coffeeChoice == "americano":
    # Asks the user for the drink size
    coffeeSize = input("What size would you like it?: ")
    
    #Actions based on size entered 
    '''
        SMALL AMERICANO
    '''
    if coffeeSize == "small" or coffeeSize == "Small" or coffeeSize == "S" or coffeeSize == "s":
        print(" ")
        print("----------------------")
        print("You chose a small Americano. Great choice!")
        print("----------------------")
        print("Your total will be: ${:.2f}".format(smallCoffeePrice))
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
    '''
        MEDIUM AMERICANO
    '''
    if coffeeSize == "medium" or coffeeSize == "Medium" or coffeeSize == "M" or coffeeSize == "m":
        print(" ")
        print("----------------------")
        print("You chose a medium Americano. Great choice!")
        print("----------------------")
        print("Your total will be: ${:.2f}".format(mediumCoffeePrice))
        # Asking them to enter the value they will pay
        userMoney = float(input("Enter how much you will be paying (ex: '2.00'): $"))
        # If they entered more or equal to than the price, then it will complete the transaction
        # and show them their change.
        if userMoney >= mediumCoffeePrice:
            print(" ")
            print("----------------------")
            print("You paid: ${:.2f}".format(userMoney))
            print(" ")
            print("Your change is: ${:.2f}".format(userMoney - mediumCoffeePrice))
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
    '''
        LARGE AMERICANO
    '''
    if coffeeSize == "large" or coffeeSize == "Large" or coffeeSize == "L" or coffeeSize == "l":
        print(" ")
        print("----------------------")
        print("You chose a large Americano. Great choice!")
        print("----------------------")
        print("Your total will be: ${:.2f}".format(largeCoffeePrice))
        # Asking them to enter the value they will pay
        userMoney = float(input("Enter how much you will be paying (ex: '3.00'): $"))
        # If they entered more or equal to than the price, then it will complete the transaction
        # and show them their change.
        if userMoney >= largeCoffeePrice:
            print(" ")
            print("----------------------")
            print("You paid: ${:.2f}".format(userMoney))
            print(" ")
            print("Your change is: ${:.2f}".format(userMoney - largeCoffeePrice))
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
    else:
        print("Invalid drink size. Restart the program and try again!")
        exit()
        
'''
    LATTE
'''
if coffeeChoice == "Latte" or coffeeChoice == "latte":
    # Asks the user for the drink size
    coffeeSize = input("What size would you like it?: ")
    
    #Actions based on size entered 
    '''
        SMALL LATTE
    '''
    if coffeeSize == "small" or coffeeSize == "Small" or coffeeSize == "S" or coffeeSize == "s":
        print(" ")
        print("----------------------")
        print("You chose a small Latte. Great choice!")
        print("----------------------")
        print("Your total will be: ${:.2f}".format(smallCoffeePrice))
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
    '''
        MEDIUM LATTE
    '''
    if coffeeSize == "medium" or coffeeSize == "Medium" or coffeeSize == "M" or coffeeSize == "m":
        print(" ")
        print("----------------------")
        print("You chose a medium Latte. Great choice!")
        print("----------------------")
        print("Your total will be: ${:.2f}".format(mediumCoffeePrice))
        # Asking them to enter the value they will pay
        userMoney = float(input("Enter how much you will be paying (ex: '2.00'): $"))
        # If they entered more or equal to than the price, then it will complete the transaction
        # and show them their change.
        if userMoney >= mediumCoffeePrice:
            print(" ")
            print("----------------------")
            print("You paid: ${:.2f}".format(userMoney))
            print(" ")
            print("Your change is: ${:.2f}".format(userMoney - mediumCoffeePrice))
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
    '''
        LARGE LATTE
    '''
    if coffeeSize == "large" or coffeeSize == "Large" or coffeeSize == "L" or coffeeSize == "l":
        print(" ")
        print("----------------------")
        print("You chose a large Latte. Great choice!")
        print("----------------------")
        print("Your total will be: ${:.2f}".format(largeCoffeePrice))
        # Asking them to enter the value they will pay
        userMoney = float(input("Enter how much you will be paying (ex: '3.00'): $"))
        # If they entered more or equal to than the price, then it will complete the transaction
        # and show them their change.
        if userMoney >= largeCoffeePrice:
            print(" ")
            print("----------------------")
            print("You paid: ${:.2f}".format(userMoney))
            print(" ")
            print("Your change is: ${:.2f}".format(userMoney - largeCoffeePrice))
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
    else:
        print("Invalid drink size. Restart the program and try again!")
        exit()

else:
    print("Sorry! Invalid drink choice. Restart the program, and try again!")
    exit()

