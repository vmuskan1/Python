#********************************************************
#
#Developer:   Muskan Vadsaria
# Program:     Assignment Numnber 2
# File Name:   MuskanVadsaria_program2
# Course:      COSC 1336 Programming Fundamentals I
# Due Date:    Sep 20,2019
# Instructor:  Sajjad Mohsin
# Chapter:     Chapter 2
# Description: Calculating average of test scores
#
#********************************************************

#***************************************************************
#
#  Function:     main
# 
#  Description:  The main function of the program
#
#  Parameters:   None
#
#  Returns:      Nothing 
#
#**************************************************************
def main():


    developerInfo()


    score1 = int(input(" Enter your score for test 1 = "))
    score2 = int(input(" Enter your score for test 2 = "))
    score3 = int(input(" Enter your score for test 3 = "))
    score4 = int(input(" Enter your score for test 4 = "))
    score5 = int(input(" Enter your score for test 5 = "))
    # all the above score# will collect the data for test scores
    
    scores = score1 + score2+ score3 + score4 + score5
    # scores will add all the five scores together

    average = float(scores/5)
    print('Your average test score is ',average)
    #the above line does the average of scores by 5 and prints
    

    # End of the main Function

#***************************************************************
#
#  Function:     developerInfo
# 
#  Description:  Prints Programmer's information
#
#  Parameters:   None
#
#  Returns:      Nothing 
#
#**************************************************************
def developerInfo():
    print('Name:     Muskan Vadsaria')
    print('Course:   Programming Fundamentals I')
    print('Program:  Two')
    print()
    # End of the developerInfo function

# Call the main function
main()

# End of Program 2
    
