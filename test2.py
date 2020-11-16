class Person:
    def __init__(self, fname, lname, mname):
        self.firstname = fname
        self.lastname = lname
        self.middlename = mname


    def printname(self):
        print(self.firstname, self.lastname, self.middlename)


class Student(Person):
    def __init__(self, fname, lname, mname, year):
        super().__init__(fname, lname, mname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

    def welcome2(self):
        print("Welcome", self.firstname, self.lastname, self.middlename, "tata banilor din", self.graduationyear)


x = Person("Mike", "Olsen", "Johny")
x.printname()
y = Student("nini", "serif", "bastan", 2019)
y.welcome2()
