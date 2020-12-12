'''
Programmer: Anthony Flores-Alvarez
Course: CS 119 Section #24321
Description: This program will calculate the net salary of 6 employees after they
input their name,gross salary, and state. 
 Date: October 9, 2020
'''
# Function to validate the user input and ensure it is a float
def floatValidator(question):
    while True:
        try:
            userInput = float(input(question))
        except ValueError:
            print(" ")
            print("Not a valid number! Try again.")
            continue
        if userInput < 0:
            print(" ")
            print("Not a valid number! Try again.")
            continue
        else:
            return userInput
            break

# Function to validate the user entered a proper state input        
def stateValidator(question):
    while True:
        try:
            userState = str(input(question))
        except ValueError:
            print(" ")
            print("Not a valid state! Try again.")
            continue
        if (len(userState) != 2):
            print(" ")
            print("Not a valid state! Try again.")
            continue
        else:
            return userState
            break

print(" ")
print("---------------------------")
print("Welcome to Net Salary Calculator! :)")
print("---------------------------")
print(" ")

# Looping to get 6 employees' inputs
for i in range(6):
    print(" ")
    # Asking for name of employee
    empName = str(input("Enter the name of the Employee: "))
    # Asking for the salary of the employee
    empSalary = float(floatValidator("Enter the salary of the Employee: $"))
    # Asking for the state of the employee
    empState = str(stateValidator("Enter the state of residence for the Employee (Abbreviated as: CA, NV, AZ, etc.): "))
    # Case for employees making over $100,000
    if empSalary > 100000:
        # Fed Tax is 20% for these employees
        federalTax = empSalary * 0.20
        
        # If the employee is in any of these states, State Tax is 10%
        if empState == "CA" or empState == "NV" or empState == "AZ" or empState == "TX":
            stateTax = empSalary * 0.10
        # If not, State Tax is 12%
        else:
            stateTax = empSalary * 0.12
            
        empSalary = (empSalary - (federalTax + stateTax))
        print("This employee's net salary is", round(empSalary, 2))
    # Case for employees making under $100,000
    elif empSalary <= 100000 and empSalary >= 0:
        # Fed Tax is 15% for these employees
        federalTax = empSalary * 0.15
        
        # If the employee is in any of these states, State Tax is 10%
        if empState == "CA" or empState == "NV" or empState == "AZ" or empState == "TX":
            stateTax = empSalary * 0.10
        
        # If not, State Tax is 12%
        else:
            stateTax = empSalary * 0.12
        
        # Updating the employee salaries with their net salaries
        empSalary = (empSalary - (federalTax + stateTax))
        print("This employee's net salary is", round(empSalary, 2))
    else:
        print("Sorry! Invalid inputs. Restart the program. ")
        exit()
