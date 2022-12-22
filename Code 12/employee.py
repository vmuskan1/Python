class Employee:
    def __init__(self,name = "", hourlyPayRate = 7.25, hourWorked = (0,0,0,0)):
        self.__name = name
        self.__hourlyPayRate = hourlyPayRate
        self.__hourWorked = hourWorked

    def getName(self):
        return self.__name
    def setName(self, name):
        self.__name = name
    # it gets and set and returns the name of employee

    def getRate(self):
        return(self.__hourlyPayRate)
    def setRate(self, hourlyPayRate):
        self.__hourlyPayRate = hourlyPayRate
    #it gets and sets and returns the hourly pay rate of employee

    def getHours(self):
        return self.__hourWorked
    def setHours(Self, hourWorked):
        self.__hourWorked = hourWorked
    # it gets and sets and returns #'s of hours an employee worked

    def getRegularHours(self):
        total = 0
        for week in self.__hourWorked:
            total += week if week <= 40 else 40
        return total
    #this sets the no of hhours as the regulatr hours to 40

    def getOvertimeHours(self):
        total = 0
        for week in self.__hourWorked:
            total += (week-40) if week > 40 else 0
        return total
    #this gets the overtime hours worked by subtracting total no by 40

    def getRegpay(self):
        return self.getRegularHours() * self.__hourlyPayRate
    #it calculates the regular pay and returns it
    def getOvertimepay(self):
        return self.getOvertimeHours()*self.__hourlyPayRate * 1.5
    #calculates over time pay and returns it
    def getGrossPay(self):
        return self.getRegpay() + self.getOvertimepay()
    #callculates gross pay by adding both pays

    def getTax(self):
        return self.getGrossPay() * (0.1 if self.getGrossPay()< 2000
                            else 0.15 if self.getGrossPay() < 3500
                            else 0.28 if self.getGrossPay() < 6000
                            else 0.31 if self.getGrossPay() < 10000
                            else 0.36)
    #it calculates the tax using gross pay 10%- under 2000, 15%- under 3500
    #28%-under 6000,31% under 10000 and 36% tax for 10000 or above
    def __str__(self):
        return("Name: " + self.__name + "\n" +
                 "Regular Hoours: "+ format(self.getRegularHours())+ "\n" +
                 "Overtime Hours: " + format(self.getOvertimeHours()) + "\n" +
                 "Total Hours: " + format(sum(self.getHours())) + "\n" +
                 "Pay Rate: $" + format(self.getRate(), '.2f')+ "\n" +
                 "Monthly Regular Pay: $" + format(self.getRegpay(),".2f") + "\n"+
                 "Monthly Overtime Pay: $" + format(self.getOvertimepay(),".2f") + "\n"+
                 "Monthly Gross Pay: $" + format(self.getRegpay() + self.getOvertimepay(),".2f") + "\n"+
                 "Monthly  Taxes: $" + format(self.getTax(),".2f") + "\n"+
                 "Monthly Net Pay: $" + format(self.getGrossPay() - self.getTax(),".2f"))
