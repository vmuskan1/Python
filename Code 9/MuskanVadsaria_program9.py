def main():
    developerInfo()
    data()
    total_rainfall()
    average_rainfall()
    highest_rainfall()
    lowest_rainfall()

def rainfall_list():
    inFile = open('program9.txt','r')
    rainfall = inFile.readlines()
    inFile.close()

    index = 0
    while index < len(rainfall):
        rainfall[index] = float(rainfall[index])
        index += 1
    return rainfall

def data():
    print("Data of rainfall in inches for entire year:",rainfall_list())
    print()

def month():
    months = ["January", "February", "March", "April","May", "June",\
              "july", "August", "september", "October","November",\
              "December"]
    return months

def total_rainfall():
    print("Total rainfall : ",format(sum(rainfall_list()),",.2f"))

def average_rainfall():
    total = 0
    for num in rainfall_list():
        total += num
    average = total/len(rainfall_list())
    print("Average Rainfall : ",format(average, ",.2f"))

def highest_rainfall():
    month_index = rainfall_list().index(max(rainfall_list()))
    months = month()
    print("Highest Rainfall :", months[month_index], "with" , max(rainfall_list()),"inches")

def lowest_rainfall():
    month_index = rainfall_list().index(min(rainfall_list()))
    months = month()
    print("Lowst Rainfall: " , months[month_index],"with", min(rainfall_list()),"inches")
    
def developerInfo():
    print('Name:     Muskan Vadsaria')
    print('Course:   Programming Fundamentals I')
    print('Program:  Nine')
    print()

main()

          
    
