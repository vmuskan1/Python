#***************************************************************
#
#  Developer:         <Muskan Vadsaria>
#
#  Program #:         <Assignment Number 4>
#
#  File Name:         <Program1.py>
#
#  Course:            COSC 1336 Programming Fundamentals I 
#
#  Due Date:          <sep 27,2019>
#
#  Instructor:        Sajjad Mohsin 
#
#  Chapter:           <Chapter 3>
#
#  Description:       Calculating gross pay of employee
#     
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
    
    Id_Number = int(input("Enter your ID number: "))
    #ask user to enter ID number
    
    pay_rate  = float(input("Enter your hourly pay rate: "))
    #ask user to enter their hourly pay rate
    
    hours_worked = int(input("Enter the Total #'s of Hours you worked: "))
    #ask user to enter the numbers of hours they wroked in a week

    normal_hours = 40
    overtime_hours = 0
    if hours_worked > normal_hours :
        regular_hours = normal_hours
        overtime_hours = hours_worked - normal_hours
        total_hours = regular_hours + overtime_hours
        regular_pay = (pay_rate * regular_hours)
        overtime_pay = pay_rate * 1.5 * overtime_hours
    else:
        regular_hours = hours_worked
        overtime_hours = 0
        total_hours = regular_hours + overtime_hours
        regular_pay = (pay_rate * regular_hours)
        overtime_pay = pay_rate * 1.5 * overtime_hours
        
          
    #ask user to enter #'s of hours they worked and later it calculates, and
    #prints the overtime and regular hour worked
    print("Regular hours: ", regular_hours)
    print("Overtime hours: ", overtime_hours)
    print("Total hours: ", total_hours)
    print("Regular Pay: $",format(regular_pay, ',.2f'), sep ='')
    print("Overtime Pay: $",format(overtime_pay, ',.2f') , sep ='')
    #calculates the pay 

    gross_pay = regular_pay + overtime_pay
    print("Gross Pay: $",format(gross_pay, ',.2f'),sep ='')
    # calculates gross pay
    income_tax = 0
    if gross_pay > 600:
        income_tax = ( gross_pay * (10.5/100))
    else:
        ("no tax")
    parking_charge = 25
    deduction = parking_charge + income_tax
    print("Deduction: $",format(deduction, ',.2f'), sep ='')
    #finds the deduction
    
    net_pay = gross_pay - deduction
    print("Net Pay: $",format(net_pay , ',.2f'),sep ='')
    #calculates Net Pay
    
    
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
    print('Program:  Four')
    print()
    # End of the developerInfo function

# Call the main function
main()

# End of Program 1
