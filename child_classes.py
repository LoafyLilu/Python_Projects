#creating a class,  properties and method
class User:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
    
  def printname(self):
    print(self.firstname, self.lastname)

#creating an instance of the class User

x = User("Mary", "Joe")
x.printname()

#creating the first subclass, with two additional properties

class Employee(User):
    def __init__(self, fname, lname, basePay, startDate):
        super().__init__(fname, lname)
        self.basePay = basePay
        self.startDate = startDate

    def printEmp(self):
        print(self.firstname, self.lastname, self.startDate)

#creating an instance of the subclass
y = Employee("Jeff", "Andrews", "20", "07/01/2018")
z = Employee("Amy", "Parker", "18", "01/01/2020")
w = Employee("Mark", "Banner", "16", "04/01/2022")
print(y.basePay, y.firstname)

#creating a second sublass , with two additional properties
class Customer(User):
    def __init__(self, fname, lname, cxType, nextOrder):
        super().__init__(fname,lname)
        self.cxType = cxType
        self.nextOrder = nextOrder

    def printCx(self):
        print(self.firstname, self.lastname,  self.cxType, self.nextOrder)

#creating a instance of the second subclass
a = Customer("Bob", "Smith", "Raw Materials", "05/01/2023")

a.printCx()


    
