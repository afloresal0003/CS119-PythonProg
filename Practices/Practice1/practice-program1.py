'''
Programmer: Anthony Flores-Alvarez
Course: CS 119 Section #24321
Description: This program declares two variables with values assigned to them
             and then the product of these two values is displayed.
 Date: September 5, 2020
'''

'''Main'''
# Hard-coded integer initialization & declaration
integerOne = 3
integerTwo = 5
product = integerOne * integerTwo
# Outputting the product of the integers
print("The product of", integerOne, "and", integerTwo, "is", product)



'''Alternate'''
integer1 = int(input("Enter an integer: "))
integer2 = int(input("Enter an integer: "))
print("The product of {} and {} is {}.".format(integer1, integer2, (integer1*integer2)))
