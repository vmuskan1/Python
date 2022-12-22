#********************************************************************
#
#  Author:            <Muskan Vadsaria>
#
#  Program #:         10
#
#  File Name:         Program10.py
#
#  Course:            COSC 1336 Programming Fundamentals I 
#
#  Due Date:          <Due Date>
#
#  Instructor:        Sajjad Mohsin 
#
#  Chapter:           <Chapter 5,6,7,8>
#
#  Description:
#
#********************************************************************

def main():
    developerInfo()
    list()
    find_average()
    above_average()
    below_average()
#**************************************************************    
def list():

    inFile = open('program10.txt', 'r')
    outFile = open('program10-out.txt', 'a')
    outFile.write(str("%12s    %12s  %16s\n" % ("Account #", "Income", \
                                                "Members"))) 
    
    print("%12s    %10s  %14s" % ("Account #", "Income", "Members"))
	
    lineRead = inFile.readline()       
    while lineRead != '':              
       words = lineRead.split()        
       acctNum = int(words[0])         
       annualIncome = float(words[1])  
       members = int(words[2])         
       print("%10d  %15.2f  %10d" % (acctNum, annualIncome, members))
       outFile.write(str("%10d   %16.2f   %12d\n" % (acctNum, annualIncome, \
                                                     members)))
       lineRead = inFile.readline()  
    inFile.close()
    print()
#*************************************************
def print_lists():
    inFile = open('program10.txt', 'r')
	
    lines = inFile.readline()
    Account = []
    Income = []
    Members = []
    
    while lines != '':              
       words = lines.split()
       acctNum = int(words[0])
       Account.append(acctNum)      
       annualIncome = float(words[1])  
       Income.append(annualIncome)  
       members = int(words[2])         
       Members.append(members)      

       lines = inFile.readline()    
    inFile.close()
    return Account, Income, Members
#********************************************************************
def find_average():
    Account, Income, Members = print_lists()
    total = 0
    for num in Income:
        total += num    
    average = total / len(Income)
    print('Average household income is: $',format(average, '.2f'), sep = '')
    print()
    return average
#finds the average using formula of total income/ my num of families.
#later it prints the average

#***********************************************************
def above_average():
    Account, Income, Members = print_lists()
    Average = find_average()
    outFile = open("program10-out.txt", "a")
    index = 0
    print("   Above Average")
    print("Account #\tIncome")
    print('--------------------------')
    while index < len(Income):
          if Income[index] > Average:
              print(Account[index], '\t\t', '$', format(Income[index], '.2f'),\
                    sep = '')
              index +=1
          else:
              index +=1
    print()
    #prints account number and income of each family who has income above average income
#**************************************************************
def below_average():
    Account, Income, Members = print_lists()
    outFile = open('program10-out.txt', 'a')
    index = 0 
    poverty = 0
    print("     Below Average")
    print('Account #\tIncome')
    print('--------------------------')
    while index < len(Members):
        poverty_level = 16460 + 4320 * (Members[index] - 2)
        if Income[index] < poverty_level:
            print(Account[index], '\t\t', '$', format(Income[index], '.2f'),\
                    sep = '')
            index +=1 
            poverty += 1
        else:
            index +=1
    print()
    #print accout number and income of each family who falls below average
    poverty_percentage = poverty / len(Members)
    outFile.write(str(format(poverty_percentage, '.2%')))
    print("The percentage of households below the 2018 United States’\n" + \
          "Contiguous States poverty level is: ", \
          format(poverty_percentage, '.2%'))
    #prints perctange of household below US contuguos poverty
    
#**************************************************************
def developerInfo():
    print('Name:     <Muskan Vadsaria>')
    print('Course:   Programming Fundamentals I')
    print('Program:  Ten')
    print()
    #infomation about the program developer
main()
