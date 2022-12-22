import employee

def main():
    while True:
        information = employee.Employee(input("Enter employee name: "),
                                 float(input("Employee's hourly pay rate: $")),
                                 tuple(map(float, input("Enter no's of hours worked per week seperate by having comma: ").split(','))))
        if (information.getName() == "quit"):
            break
        else:
            print(information)
            print("")
main()
