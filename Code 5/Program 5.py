#***************************************************************
#
#  Developer:         Muskan Vadsaria 
#
#  Program #:         Assignment Number 5
#
#  File Name:         MuskanVadsaria_Program3.py>
#
#  Course:            COSC 1336 Programming Fundamentals I 
#
#  Due Date:          sep 29,2019
#
#  Instructor:        Sajjad Mohsin 
#
#  Chapter:           Chapter #3
#
#  Description:       Finding discounted rate for a software company
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

    retail_price = 99
    #variable reprenting the price
    
    quantity_1 = 100
    quantity_2 = 70
    quantity_3 = 50
    quantity_4 = 20
    quantity_5 = 10    
    # variables represening the quantity
    
    discount1 = 20
    discount2 = 30
    discount3 = 35
    discount4 = 40
    discount5 = 50
    # variables representing the discount rate
    total_savings = 0
    total_cost = 0
    units_sold = int(input("Enter the number of  units sold : "))
    #get the number of units sold from user

    if units_sold >= quantity_1 :
        total_savings = (units_sold * retail_price)* (discount5/100)
        total_cost = (units_sold * retail_price)-total_savings
        print("discount applied is:" ,discount5,"%")
    else:
        if units_sold >= quantity_2:
            total_savings = (units_sold * retail_price)* (discount4/100)
            total_cost = (units_sold * retail_price)-total_savings
            print("discount applied is:" ,discount4,"%")
        else:
            if units_sold >= quantity_3:
                total_savings = (units_sold * retail_price)* (discount3/100)
                total_cost = (units_sold * retail_price)-total_savings
                print("discount applied is:" ,discount3,"%")
            else:
                if units_sold >= quantity_4:
                    total_savings = (units_sold * retail_price)* (discount2/100)
                    total_cost = (units_sold * retail_price)-total_savings
                    print("discount applied is:" ,discount2,"%")
                else:
                    if units_sold >= quantity_5:
                        total_savings = (units_sold * retail_price)* (discount1/100)
                        total_cost = (units_sold * retail_price)-total_savings
                        print("discount applied is:" ,discount1,"%")
                    else:
                        print("you don't meet the quota")
                        
    #It determines and displays the discount applied

    print("Total saving due to discount is: $" , format(total_savings , ',.2f'), sep ='')
    #prints the total saving from discount

    
    print("The total cost of the purchase is: $" , format(total_cost , ',.2f'), sep ='')
    #prints the total cost of purchase                  

    #End of main Function


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
    print('Program:  Five')
    print()
    # End of the developerInfo function

# Call the main function
main()

# End of Program 4
