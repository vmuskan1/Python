#***************************************************************
#
#  Developer:         <Muskan Vadsaria>
#
#  Program #:         <Assignment Number>
#
#  File Name:         <Program11.py>
#
#  Course:            COSC 1336 Programming Fundamentals I 
#
#  Course Synonym:    <392XX>
#
#  Due Date:          <11/24/2019>
#
#  Instructor:        Sajjad Mohsin 
#
#  Chapter:           <Chapter #>
#
#  Description:
#     <An explanation of what the program is designed to do>
#
#***************************************************************

BASE_YEAR = 1903

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
    # Local dictionary variables
    year_dict = {}
    count_dict = {}
	
    developerInfo()
    showResults(*filedictionaries(*preload('Program11.txt')))
    #it gives out each number after reading each line
    # End of the main function
    
def preload(filename):
    return(open(filename,'r'),{},{})
#the first{} incidates year_dict and second{} indicates count-dict
#it returns whats in the file
# End of preload function

def filedictionaries(file,year_dict, count_dict):
    lineRead = file.readline().rstrip("\n")
    year = 1903
    #it reads the first line and also it starts from 1903
    while lineRead != '':
        year_dict[year] = lineRead
        if lineRead in count_dict:
            count_dict[lineRead]=count_dict[lineRead]+1
        else:
            count_dict[lineRead] =1
        year += 1 if year != 1904 and year!=1994 else 2
        lineRead = file.readline().rstrip("\n")
    return year_dict,count_dict
#creates the while stats\ement
# after creratering the year_dict it gives out year to one team  and marks as an entry
# in else statement it creates another entry which keeps track of winning team
#by skipping two year 1904 and 1994 and enters the new data into record.
#End of filedictionaries

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
def showResults(year_dict, count_dict):
  while True:
    # Receive user input
    year = int(input('Enter a year in the range 1903-2018: '))
    

    # Print results
    if year == 0:
       break
    elif year == 1904 or year == 1994:
        print("The world series wasn't played in the year", year)
    elif year < 1903 or year > 2018:
        print('The data for the year', year, \
              'is not included in our database.')
    else:
        winner = year_dict[year]
        wins = count_dict[winner]
        print('The team that won the world series in ', \
              year, ' is the ', winner, '.', sep='')
        print('They have won the world series', wins, 'times.')
    print("")
# ask the user to input year and later it runs the record and displays it
# if the user enters 0 it breaks ends the program from running
    # End of showResults

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
    print('Program:  Eleven')
    print()
    # End of the developerInfo function

# Call the main function.
main()

