#***************************************************************
#
#  Developer:         <Muskan Vadsaria>
#
#  Program #:         <Assignment Number 1>
#
#  File Name:         <Program1.py>
#
#  Course:            COSC 1336 Programming Fundamentals I 
#
#  Due Date:          <Due Date>
#
#  Instructor:        Sajjad Mohsin 
#
#  Chapter:           <Chapter 2>
#
#  Description:
#     <An explanation of what the program is designed to do>
#
#***************************************************************

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
    
    amount = 32500.00
    twiceMonth = amount/24
    #we divide by 24 because in a month we give check twice
    #meaning 12months*2per month = 24

    biWeekly = amount/26
    #the check is given after every 15 days 
    
    print('Annual Salary           = $',amount , sep='')
    print('When paid twice a month = $',format(twiceMonth , ',.2f'),sep ='' )
    print('When paid bi-weekly     = $', biWeekly , sep='')
    
    # End of the main function 
    
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
    print('Program:  One')
    print()
    # End of the developerInfo function

# Call the main function
main()

# End of Program 1
