''' 
    Programmer: Anthony Flores-Alvarez
    Course: CS 119 - Section #24321
    Date: September 12, 2020
    Description: 
        This program collects the following data from 3 users:
        1) Name
        2) Amount of Lunch Menu item
        3) Amount of Drink
 
        Then it will calculate & output Name and the Amount 
        of each person's check including 15% tip.
'''

''' Attempt #1: '''

#Header of program to make it look nice
print(" ")
print("----------------------")
print("Total Price Calculator")
print("----------------------")
print(" ")

# Collecting user inputs

# Collecting user inputs for first person
userOneName = str(input("Enter the name of the first person: "))
userOneLunchPrice = float(input("Enter the total price of the first person's lunch item(s): $"))
userOneDrinkPrice = float(input("Enter the total price of the first person's drink item(s): $"))

# Collecting user inputs for second person
print(" ")
userTwoName = str(input("Enter the name of the second person: "))
userTwoLunchPrice = float(input("Enter the total price of the second person's lunch item(s): $"))
userTwoDrinkPrice = float(input("Enter the total price of the second person's drink item(s): $"))

# Collecting user inputs for third person
print(" ")
userThreeName = str(input("Enter the name of the third person: "))
userThreeLunchPrice = float(input("Enter the total price of the third person's lunch item(s): $"))
userThreeDrinkPrice = float(input("Enter the total price of the third person's drink item(s): $"))

# Calculating the tip and total price for user One
userOneTotal = ((userOneLunchPrice + userOneDrinkPrice) * 1.15)

# Calculating the tip and total price for user Two
userTwoTotal = ((userTwoLunchPrice + userTwoDrinkPrice) * 1.15)

# Calculating the tip and total price for user Three
userThreeTotal = ((userThreeLunchPrice + userThreeDrinkPrice) * 1.15)

# Outputting the results for each person
print(" ")
print("------------")
print("RESULTS: ")
print(" ")
print(userOneName, ":   ${:.2f}".format(userOneTotal))
print("")
print(userTwoName, ":   ${:.2f}".format(userTwoTotal))
print("")
print(userThreeName, ":   ${:.2f}".format(userThreeTotal))
print("")
print("------------")
print(" ")