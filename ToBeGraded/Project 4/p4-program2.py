'''
Programmer: Anthony Flores-Alvarez
Course: CS 119 Section #24321
Description: This program will calculate the average scores
of 5 students after their highest and lowest scores are dropped.
It will then display each student's average score after this update.
Date: October 26, 2020
'''
# Global 2D List to store the students' names and scores
scoresAndNamesList = []

# Ensures that the user enters valid inputs
def ValidateUserInput(score):
    
    # If the user enters not enough test scores, it will close the program
    if (len(score)) != 7:
        print("------------------------------------------------")
        print("Sorry! Invalid test scores.")
        print("Please restart the program and enter 5 scores per student.")
        print("------------------------------------------------")
        exit()
        
    # Loops through each score entered by the user
    # Starts at 2 because first 2 are the names of the students
    for i in range(2, len(score)):
        try: 
            # If the user enters inputs that are not numbers, closes program
            if((score[i]).isdigit() != True):
                print("------------------------------------------------")
                print("Sorry!", score[i], "is not a valid score.")
                print("------------------------------------------------")
                print("Remember that inputs must be positive integers.")
                print("------------------------------------------------")
                print("Restart the program and try again!")
                print("------------------------------------------------")
                exit()
                return False
                
        # If the user enters any other invalid inputs, closes program
        except:
            print("------------------------------------------------")
            print("Sorry!", score[i], "is not a valid score.")
            print("------------------------------------------------")
            print("Remember that inputs must be positive integers.")
            print("------------------------------------------------")
            print("Restart the program and try again!")
            print("------------------------------------------------")
            exit()
    
    # If everything checks out
    return True

# Finds the lowest score in a student's 5 tests
def findLowest(scores):
    
    try:
        # Setting first score to lowest
        lowestScore = int(scores[2])
        
    # To catch errors when user enters random stuff
    except:
        print("-------------------------------------------------------------------")
        print("Sorry your inputs were invalid. Restart the program and try again!")
        print("-------------------------------------------------------------------")
        exit()
        
    # Looping through the scores to find lowest
    for i in range(3, len(scores)):
        
        if(int(scores[i]) < lowestScore):
            
            lowestScore = int(scores[i])
            
    # Giving back the lowest score to calcScore()
    return int(lowestScore)

# Finds the highest score in a student's 5 tests
def findHighest(scores):
    
    # Setting first score to highest
    highestScore = int(scores[2])
    
    # Looping through scores to find highest
    for i in range(3, len(scores)):
        if(int(scores[i]) > highestScore):
            highestScore = int(scores[i])
            
    # Giving back the highest score to calcScore()
    return int(highestScore)

# Calculates the average score
def calcScore(scores):
    
    # List to store all averages for the students
    averageScoresList = []
    
    # Loop through all students one by one
    for i in range(len(scores)):
        
        # Storing lowest score of the student
        lowestScore = findLowest(scores[i])
        # Storing highest score of the student
        highestScore = findHighest(scores[i])
        
        # Initializing total
        total = 0
        
        # Totataling all of this student's scores
        for j in range(2, len(scores[i])):
            total = total + int(scores[i][j])
            
        # Calculating the average score by removing the lowest and highest scores
        averageScore = (total - (lowestScore + highestScore)) / 3
        # Rounding up the score just in case
        averageScore = round(averageScore, 2)
        
        # Adding score to average score list
        averageScoresList.append(averageScore)
    
    # Return the average score list
    return averageScoresList

# Asks the user for student info including student full name and 5 scores
def getStudentInfo():
    
    global scoresAndNamesList
    
    # Asking for the scores in specific format
    print("Enter student firstName lastName ex1 ex2 ex3 ex4 ex5")
    
    # Number of students
    numOfStudents = 7
    
    # Looping to get info from each student
    while(numOfStudents > 0):
        
        # Input separated by space
        score = list(input().split())
        
        # If it's a valid input...
        if(ValidateUserInput(score)):
            
            # ... adding it to the list
            scoresAndNamesList.append(score)
            
            # Decrementing
            numOfStudents = numOfStudents - 1
            
        # Invalid input case
        else:
            print("-----------------------------------------------------------------------")
            print("\n Error! Please enter valid inputs: ")
            print("-----------------------------------------------------------------------")

# MAIN Function
def main():
    
    # Getting user input
    getStudentInfo()
    
    # Printing the average scores
    print("-----------------------------------------------------------------------")
    print("Highest and Lowest Scores Dropped. Updated Average Scores Per Student: ")
    print("-----------------------------------------------------------------------")
    for i in range(len(scoresAndNamesList)):
        for j in range(0, 1):
            print(scoresAndNamesList[i][j],"'s Average Score: ", calcScore(scoresAndNamesList)[i])
    print("------------------------------------------------")
    print("Thank you! Have a nice day! :)")
    print("------------------------------------------------")
    
    
    
# Program begins
print("------------------------------------------------")
print("Welcome to Average Score Updater!")
print("------------------------------------------------")
print("This program will drop the highest and lowest scores")
print("for each student that you enter.")
print("\nNOTES: ")
print("- Please enter each student's scores in the following format: ")
print("\n     'FirstName LastName Score1 Score2 Score3 Score4 Score5'")
print("\n- Example:")
print("\n     'Anthony Flores 98 56 78 100 21'")
print("\n- Ensure that there is a space in between.")
print("- Immediately after the last score, press enter")
print("\n- Input should look like this: ")
print("\nJones Tom 94 99 96 74 56\nThompson Frank 67 58 86 95 47\nJackson Tom 95 97 94 87 67\nJackie Michael 43 23 34 77 64\nJohnson Sara 84 93 64 57 89\nColt McCoy 84 93 64 57 70\nFreeman Tina 67 58 86 95 47")
print("\nYou can actually just copy and paste the example above if you'd like as well.")
print("Just make sure to copy it so it follows the proper format still/as it's written.")
print("\n------------------------------------------------")
main ()