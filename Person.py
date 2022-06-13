from datetime import date  #библиотека работы с системным временем

class Person():

    def printInfo(self):
        print(self.firstName)
        print(self.lastName)

    def printInfoFormatted(self):
        print(f"Name: {self.firstName}, LastName: {self.lastName}")

    def getAge(self):
        print(f"Age: {date.today().year-self.date_of_birth}") #текущий год - дата рождения = возраст

# ===========================================================================
# Main


p1 = Person()
p1.firstName = 'Ivan'
p1.lastName = 'Kozlov'
p1.date_of_birth = 1963

p1.printInfo()
p1.printInfoFormatted()
p1.getAge()

Person.printInfoFormatted(p1)
