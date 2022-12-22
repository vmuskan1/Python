#********************************************************************
#
#  Developer:         <Muskan Vadsaria>
#
#  Program #:         7
#
#  File Name:         Program7.py
#
#  Course:            COSC 1336 Programming Fundamentals I 
#
#  Due Date:          <10/20/19>
#
#  Instructor:        Sajjad Mohsin 
#
#  Chapter:           <Chapter 4&6>
#
#  Description:
#     This program reads and displays the contents
#     of a file.
#********************************************************************
def main():
    
    inFile = open('program7.txt', 'r')
    
    lineRead = inFile.readline()
    total_before = 0
    total_after1 = 0
    total_after2 = 0
    total_after3 = 0
    total_after = 0
    while lineRead != '':
       words = lineRead.split() 
       for word in words:
          num = float(word)
          total_before = total_before + num
          print(format(num, '.2f'))
       #it reads the pay from text file abour each faculty
          if num > 60000.00:
              percent = 4
              total_raise = num * percent / 100
              total = num + total_raise
              total_after1 = total + total_after1
              print("Your pay right now is: $",num,sep="")
              print("Your pay will raise to: ",percent,"%",sep="")
              print("your pat after raise: $",format(total_raise , ",.2f"),sep="")
              print("Now your pay will be, $",format(total,",.2f"),"\n" ,sep="")
        #it calculates and print the raise, after and before pay
        #of the faculty who earns more than $60000.00
          elif num > 50000.00:
              percent = 7
              total_raise = num * percent / 100
              total = num + total_raise
              total_after2 = total + total_after2
              print("your pay right now is: $",num,sep="")
              print("Your pay will raise to: ", percent,"%",sep="")
              print("your pay after raise: $",format(total_raise,",.2f"),sep="")
              print("Now your pay will be, $",format(total,",.2f"),"\n" ,sep="")
        #it calculates and print the raise, after and before pay
        #of the faculty who earns more than $50000.00
          else:
              percent = 5.5
              total_raise = num * percent / 100
              total = num + total_raise
              total_after3 = total + total_after3
              print("your pay right now is: $",num,sep="")
              print("Your pay will raise to:", percent ,"%",sep="")
              print("your pay after raise: $",format(total_raise,",.2f"),sep="")
              print("Now your pay will be, $",format(total,",.2f"),"\n" , sep="")
        #it calculates and print the raise, after and before pay for all others
       total_after = total_after1 + total_after2 +total_after3 
       lineRead = inFile.readline()
       
    # Close the file.
    inFile.close()
    print('Total Faculty payroll before the raise is $',format(total_before, ",.2f"),sep="")
    print('Total Faculty payroll after the raise is $',format(total_after, ",.2f"),sep="")
# Call the main function.
main()
