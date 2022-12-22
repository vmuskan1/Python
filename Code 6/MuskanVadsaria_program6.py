#**********************************************************
#
# Developer:   Muskan Vadsaria
# Program:     Assignment Numnber 6
# File Name:   MuskanVadsaria_program6
# Course:      COSC 1336 Programming Fundamentals I
# Due Date:    Oct 13,2019
# Instructor:  Sajjad Mohsin
# Chapter:     Chapter 4
# Description: Calculating the occupancy rate for a hotel
#
#***********************************************************

#***********************************************************
#
#  Function:     main
# 
#  Description:  The main function of the program
#
#  Parameters:   None
#
#  Returns:      Nothing 
#
#***********************************************************

def main():

    developerInfo()

    floors = int(input("How many floors the hotel has : "))
    #ask the user to enter how many floors in total does the hotel has
    total_rooms = 0
    unoccupied = 0
    total_occupied = 0
    for rooms in range (floors):
        
          numbers_ofrooms = rooms + 1
          print('Enter is numbers of rooms on floor',numbers_ofrooms)
          total = int(input())
          total_rooms = total + total_rooms
          print("Rooms on floor", numbers_ofrooms, ":" , total)
          #print to enter the total room on particular floors
          #ask user to enter the total room on floor asked
          #keep counts of all rooms on every floor and adds them up
          #prints the room on each floor of the hotel
    
          rooms_occupied = rooms 
          occupied = int(input("rooms in use? "))
          total_occupied += occupied 
          #ask the user to enter the total numbers of rooms occupied
          #later in total_occupied it counts all the rooms occupied in all the floors of the hotel
          
    unoccupied = total_rooms-total_occupied
    #formula for unoccupied rooms
    percentage = total_occupied/total_rooms *100
    #formula for percentage
    print("")
    print("Total Rooms :", total_rooms)
    print("Rooms Occupied :", total_occupied )
    print("Rooms Unoccupied :", unoccupied)
    print("percentage is:",format(percentage, ",.2f"),"%",sep="")
    #Prints total numbers of rooms occupied, unoccupied, total rooms, and percentage

    #End of the main Function
#************************************************************
#
#  Function:     developerInfo
# 
#  Description:  Prints Programmer's information
#
#  Parameters:   None
#
#  Returns:      Nothing 
#
#************************************************************
def developerInfo():
    print('Name:     Muskan Vadsaria')
    print('Course:   Programming Fundamentals I')
    print('Program:  Six')
    print()
    # End of the developerInfo function

# Call the main function
main()

# End of Program 2
