'''
Programmer: Anthony Flores-Alvarez
Course: CS 119 Section #24321
Description: This program is an employee manager. It has 8 options
to choose from, each doing something different, such as adding new
employees, sorting them, displaying, etc. No built-in functions were
used other than len() and index()
Date: October 26, 2020
'''

# Declaring original employee list and salaries
Employees = ["Mike navarro", "Miguel saba", "Maria Rami"]
Salaries = [20000.00, 30000.00, 40000.00]

# Adds a new employee to the employee list
def addEmployee(Employee, Salary):
    global Employees
    global Salaries
    # Adding passed employee name and salary to global lists
    Employees = Employees + [Employee]
    Salaries = Salaries + [Salary]
    return None
    
# Removes an employee from the employee list
def removeEmployee(Employee, Salary):
    global Employees
    global Salaries
    try:
        # Saving index of passed employee
        i = Employees.index(Employee)
    except ValueError:
        print(Employee, "is not an employee. Please restart the \nprogram and enter an actual employee.")
        print("------------------------------------------------")
        exit()
    else:
        # Removing that employee from global list of names and salaries
        Employees = [e for e in Employees if e != Employees[i]]
        Salaries = [f for f in Salaries if f != Salaries[i]]

# Inserts a new employee in the location of the given index
def insertNewEmployee(Employee, Index, Salary):
    global Employees
    global Salaries
    # Storing passed employee name and salary
    passedEmployee = [Employee]
    passedSalary = [Salary]
    # Storing the employees that are before and after that index
    employeeBefore = Employees[0:index]
    employeeAfter = Employees[index:]
    # Storing the salaries that are before and after that index
    salaryBefore = Salaries[0:index]
    salaryAfter = Salaries[index:]
    # Storing them in new order back into global list of employees and salaries
    Employees = employeeBefore + passedEmployee + employeeAfter
    Salaries = salaryBefore + passedSalary + salaryAfter
    return None
    
# Sorts the salaries in descending order
def sortSalaries(Employees, Salaries):
    # Looping through salary list with focus on 2 places
    for i in range(len(Salaries)):
        for j in range(i+1, len(Salaries)):
            # If the first salary is less than the following...
            if Salaries[i] < Salaries[j]:
                # .. swap them
                Salaries[i], Salaries[j] = Salaries[j], Salaries[i]
                Employees[i], Employees[j] = Employees[j], Employees[i]
        
    return None

# Searches for an employee in the employee list
def searchEmployee(Employee):
    global Employees
    global Salaries
    try:
        # Getting and storing the employee's index
        index = Employees.index(Employee)
    except ValueError: 
        print(Employee, "is not an employee. Please restart the \nprogram and enter an actual employee.")
        print("------------------------------------------------")
        exit()
    else:
        # Returning back that index and salary
        return([index, Salaries[index]])

# Calculates the total salary from the sum of all employees' salaries
def totalSalary(Salaries):
    totalSalary = 0
    # Looping through all salaries...
    for i in range(len(Salaries)):
        # ... and summing them
        totalSalary = totalSalary + Salaries[i]
    # Giving back total salarys
    return totalSalary

# Displays the list of employees
def displayList(Employees, Salaries):
    print(Employees)
    print(Salaries)

# Ensures that the user enters an integer
def intValidator(question):
  while True:
    try:
       userInput = int(input(question))       
    except ValueError:
       print(" ")
       print("Invalid choice! Please select from the menu.")
       continue
    else:
       return userInput 
       break 
   
# Ensures that the user enters a float
def floatValidator(question):
  while True:
    try:
       userInput = float(input(question))
    except ValueError:
       print(" ")
       print("Invalid number! Please enter a valid number: ")
       continue
    if userInput < 0:
       print(" ")
       print("Error! Please enter a positive number: ")
       continue
    else:
       return userInput 
       break 
   
# HEADING
print("------------------------------------------------")
print("Welcome to Employee Manager!")
print("------------------------------------------------")
print(" 1 - Add a new Employee\n 2 - Remove an Employee \n 3 - Insert new Employee \n 4 - Sort Salaries in Descending Order \n 5 - Search for an Employee \n 6 - Find Total Salary \n 7 - Display Employee List \n 8 - Quit Program")
print("------------------------------------------------")
# Asking for user's choice
userinput = intValidator("Please enter a number: ")
# Looping until the user enters 8 to close the program
while (True):
    # Case for option 1 - Add Employee
    if userinput == 1:
        print("------------------------------------------------")
        print("Adding An Employee")
        print("------------------------------------------------")
        newemployee = str(input("Enter the employee name you want to add: "))
        Salary = floatValidator("Enter the employee salary you want to add: ")
        print("------------------------------------------------")
        print("Before: ")
        print(Employees)
        print(Salaries)
        print("------------------------------------------------")
        addEmployee(newemployee, Salary)
        print("After: ")
        print(Employees)
        print(Salaries)
        print("------------------------------------------------")
    
    # Case for option 2 - Remove Employee
    elif userinput == 2:
        print("------------------------------------------------")
        print("Removing An Employee")
        print("------------------------------------------------")
        newemployee = str(input("Enter the employee name you want to remove: "))
        Salary = floatValidator("Enter the employee salary you want to remove: ")
        print("------------------------------------------------")
        print("Before: ")
        print(Employees)
        print(Salaries)
        print("------------------------------------------------")
        removeEmployee(newemployee, Salary)
        print("After: ")
        print(Employees)
        print(Salaries)
        print("------------------------------------------------")
    
    # Case for option 3 - Insert Employee
    elif userinput == 3:
        print("------------------------------------------------")
        print("Inserting An Employee")
        print("------------------------------------------------")
        index = intValidator("Where do you want to insert the item (Enter the index number): ")
        newemployee = str(input("Please enter the employee name you want to insert: "))
        Salary = floatValidator("Please enter the employee salary you want to insert: ")
        print("------------------------------------------------")
        print("Before: ")
        print(Employees)
        print(Salaries)
        insertNewEmployee(newemployee, index, Salary)
        print("------------------------------------------------")
        print("After: ")
        print(Employees)
        print(Salaries)
        print("------------------------------------------------")
    
    # Case for option 4 - Sort Salaries
    elif userinput == 4:
        print("------------------------------------------------")
        print("Sorted Salaries: ")
        print("------------------------------------------------")
        print("Before: ")
        print(Employees)
        print(Salaries)
        print("------------------------------------------------")
        sortSalaries(Employees, Salaries)
        print("After: ")
        print(Employees)
        print(Salaries)
    
    # Case for option 5 - Search Employee
    elif userinput == 5:
        print("------------------------------------------------")
        print("Searching For An Employee")
        print("------------------------------------------------")
        newemployee = str(input("Enter the employee name you want to search: "))
        print("------------------------------------------------")
        print(newemployee, "'s Details: \n")
        print(searchEmployee(newemployee))
        print("------------------------------------------------")
    
    # Case for option 6 - Total Salary
    elif userinput == 6:
        print("------------------------------------------------")
        print("Calculated Total Salary: ")
        print("------------------------------------------------")
        print("Total: $", totalSalary(Salaries))
        print("------------------------------------------------")
    
    # Case for option 7 - Display List
    elif userinput == 7:
        print("------------------------------------------------")
        print("Displaying Employee List")
        print("------------------------------------------------")
        print("Employee List: \n")
        displayList(Employees, Salaries)
        print("------------------------------------------------")
        
    # Case for option 8 - Quit
    elif userinput == 8:
        print("------------------------------------------------")
        print("Quitting Program")
        print("------------------------------------------------")
        print("Thank you! Have a nice day! :)")
        print("------------------------------------------------")
        exit()
        
    # If none was entered
    else:
        print("\n------------------------------------------------")
        print("Sorry!", userinput, " is not a valid option. Try again!")
        print("------------------------------------------------\n")
    
    # Prompts menu again
    print("------------------------------------------------")
    print("Welcome to Employee Manager!")
    print("------------------------------------------------")
    print(" 1 - Add a new Employee\n 2 - Remove an Employee \n 3 - Insert new Employee \n 4 - Sort Salaries in Descending Order \n 5 - Search for an Employee \n 6 - Find Total Salary \n 7 - Display Employee List \n 8 - Quit Program")
    print("------------------------------------------------")
    userinput = intValidator("Please enter a choice: ")