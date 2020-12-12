'''
Programmer: Anthony Flores-Alvarez
Course: CS 119 Section #24321
Description: This program will calculate the average score and letter grade for students
 Date: October 9, 2020
'''

# Function to ensure that user input is an integer to not crash the program
def intValidator(question):
    while True: 
        try: 
            userInput = int(input(question))
        except ValueError:
            print(" ")
            print("Error! Incorrect input. Please enter a valid integer.")
            continue
        if userInput < 0:
            print(" ")
            print("Error! Incorrect input. Please enter a valid integer.")
            continue
        else:
            return userInput
            break

print("---------------------------------------------")
print("Welcome to Average Score Calculator!")
print("---------------------------------------------")

# Asking for number of students in the class
numStudents = intValidator("How many students do you have in your class? ")

# Looping by how many students are in the class
for i in range(numStudents):
    
    # Asking for student name
    stuName = input("Enter the name of your student: ")

    # Asking for the student's 3 scores
    scoreOne = intValidator("Enter this student's first score: ")
    scoreTwo = intValidator("Enter this student's second score: ")
    scoreThree = intValidator("Enter this student's third score: ")
    
    # Calculating the average score of those 3
    scoreAverage = (scoreOne + scoreTwo + scoreThree) / 3
    
    # Determining the user's letter grade based on the average score
    if scoreAverage <= 100 and scoreAverage >= 98:
        studentLetterGrade = "A+"
    elif scoreAverage <= 97 and scoreAverage >= 95:
        studentLetterGrade = "A"
    elif scoreAverage <= 94 and scoreAverage >= 91:
        studentLetterGrade = "A-"
    elif scoreAverage <= 90 and scoreAverage >= 88:
        studentLetterGrade = "B+"
    elif scoreAverage <= 87 and scoreAverage >= 84:
        studentLetterGrade = "B"
    elif scoreAverage <= 83 and scoreAverage >= 80:
        studentLetterGrade = "B-"
    elif scoreAverage <= 79 and scoreAverage >= 75:
        studentLetterGrade = "C+"
    elif scoreAverage <= 74 and scoreAverage >= 70:
        studentLetterGrade = "C"
    elif scoreAverage < 70 and scoreAverage > 60:
        studentLetterGrade = "D"
    elif scoreAverage <=60 and scoreAverage >= 0:
        studentLetterGrade = "NC"
    
    # Printing out the student's average score and grade
    print("---------------------------------------------")
    print("Here is ", stuName, "'s average scores and grades: ")
    print("---------------------------------------------")
    print("Average Score: ", round(scoreAverage), " ", studentLetterGrade)
    print("---------------------------------------------")


print("---------------------------------------------")
print("Have a great day!")
print("---------------------------------------------")