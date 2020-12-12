'''
Programmer: Anthony Flores-Alvarez
Course: CS 119 Section #24321
Description: This program will calculate and print the bill 
for a cellular telephone company that offers 2 types of services
which makes the rates vary depending on the service type.
 Date: October 9, 2020
'''

# Function to ensure that user input is a float to not crash the program
def floatValidator(question):
    while True: 
        try: 
            userInput = float(input(question))
        except ValueError:
            print(" ")
            print("Error! Incorrect input. Please enter a valid integer.")
            continue
        else:
            return userInput
            break

# Heading
print("--------------------------------")
print("Welcome to AntCell Bill Calculator! ")
print("--------------------------------")
print("For regular members: ")
print("- Simply enter your total minutes.")
print(" ")
print("For premium members:")
print("- DAY minutes refers to calls made from 6:00 a.m. to 6:00 p.m")
print("- NIGHT minutes refers to calls made from 6:00 pm to 6:00 a.m.")
print("--------------------------------")
print(" ")

# Initializing our constants (rates and pricings)
regularAccountFee = 10.00
regularRate = 0.20
premiumAccountFee = 25.00
premiumDayRate = 0.10
premiumNightRate = 0.05

# Asking for account number and service code
accountNumber = input("Please enter your account number: ")
serviceCode = input("Please enter your service code ('R' for regular | 'P' for premium): ")

# IF the service code is regular
if serviceCode == 'r' or serviceCode == "R":
    print("--------------------------------")
    serviceType = "Regular"
    # Asking for minutes used
    regMinutes = floatValidator("Please enter the number of minutes you used: ")
    
    # If more than the free 50 given, calculating the total bill with the overminute rate
    if regMinutes > 50:
        totalBill = ((regMinutes - 50) * regularRate) + regularAccountFee
    else:
        totalBill = regularAccountFee
    
    # Printing the report of the sale
    print("--------------------------------")
    print("REPORT: ")
    print("--------------------------------")
    print("Account Number: ", accountNumber)
    print("Service Type: ", serviceType)
    print("Minutes Used: ", round(regMinutes))
    print("Total Bill: ${:.2f}".format(totalBill))
    print("--------------------------------")
    exit()

# IF the service code is premium
if serviceCode == 'p' or serviceCode == 'P':
    serviceType = "Premium"
    # Asking for the day and night minutes
    premDayMinutes = floatValidator("Please enter the number of DAY minutes you used: ")
    premDayFee = 0
    # If more than the free 70 given during day, calculating the fee with the overminute rate
    if premDayMinutes > 75:
        premDayFee = (premDayMinutes - 75) * premiumDayRate
        
    premNightMinutes = floatValidator("Please enter the number of NIGHT minutes you used: ")
    premNightFee = 0
    # If more than the free 100 given during night, calculating the fee with the overminute rate
    if premNightMinutes > 100:
        premNightFee = (premNightMinutes - 100) * premiumNightRate
    # Calculating the total bill
    totalBill = premiumAccountFee + premDayFee + premNightFee
    
    # Sales report
    print("--------------------------------")
    print("REPORT: ")
    print("--------------------------------")
    print("Account Number: ", accountNumber)
    print("Service Type: ", serviceType)
    print("Minutes Used: ")
    print(" - Day: ", round(premDayMinutes))
    print(" - Night: ", round(premNightMinutes))
    print(" - Total: ", round(premDayMinutes + premNightMinutes))
    print("Total Bill: ${:.2f}".format(totalBill))
    print("--------------------------------")
    exit()

# IF neither regular or premium was entered
else:
    print("Error! Invalid service code. Please try again!")


