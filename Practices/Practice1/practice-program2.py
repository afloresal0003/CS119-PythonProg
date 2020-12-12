'''
Programmer: Anthony Flores-Alvarez
Course: CS 119 Section #24321
Description: This program allows the user to enter values for a salesperson’s 
             base salary, total sales, and commission rate. The program computes 
             and outputs the salesperson’s pay by adding the base salary to the 
             product of the total sales and commission rate.
 Date: September 5, 2020
'''

#Collecting user's values and storing them
baseSalary = float(input("Enter your base salary: "))
totalSales = float(input("Enter your total sales: "))
commRate = float(input("Enter your commision rate: "))
pay = baseSalary + (totalSales * commRate)
print("Your pay is: $", round(pay, 2))