''' 
    Programmer: Anthony Flores-Alvarez
    Course: CS 119 - Section #24321
    Date: September 12, 2020
    Description: 
        This program collects the following data from the user:
        1) User last name
        2) User First Name
        3) Number of Hours worked.
        4) Hourly-wage
     
        Then, calculates the gross wage based on the formula:
         - Gross wage is number of hours worked multiplied by hourly-wage.
        
        Finally, it outputs the user name and gross wage.
 
'''

# Header of program to make it look nice
print("--------------------------")
print("Gross Wage Calculator!")
print("--------------------------")
print(" ")

# Asking for user inputs
userFirstName = str(input("Enter your First Name: "))
userLastName = str(input("Enter your Last Name: "))
hoursWorked = float(input("Enter the number of hours you worked: "))
hourlyWage = float(input("Enter your hourly wage: $"))

# Concatenating the user's first and last name to get their full name
userFullName = userFirstName + " " + userLastName

# Calculating the gross wage
grossWage = hoursWorked * hourlyWage

# Outputting the results
print(" ")
print("--------------------------")
print("Hey, {}!".format(userFullName))
print(" ")
print("Your Gross Wage is: ${:.2f}".format(grossWage))
print("--------------------------")
