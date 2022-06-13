from datetime import date


class Person():
    staticField = 'baseValue'

    def __init__(self, firstName, lastName, yearOfBirth):
        self.firstName = firstName
        self.lastName = lastName
        self.yearOfBirth = yearOfBirth

    def printInfoFormatted(self):
        print(f"Name: {self.firstName}, LastName: {self.lastName}")

    def getAge(self):
        if self.yearOfBirth is not None:
            print(f"Age: {date.today().year - self.yearOfBirth}")  # текущий год - дата рождения = возраст
        else:
            print('Нет информации о возрасте')
#============================================


p1 = Person('Vasya', 'Petrov', 1980)
p1.printInfoFormatted()
p1.getAge()

p2 = Person('Vasya', None, None)
p2.printInfoFormatted()
p2.getAge()

print('staticField = ' + p2.staticField)
p2.staticField = 'changedInObject'
print('p2 staticField?(no!) = ' + p2.staticField)
print('p1 staticField = ' + p1.staticField+'\n')

Person.staticField = 'changedInStatic'
print('p2 staticField?(no!) = ' + p2.staticField)
print('p1 staticField = ' + p1.staticField)
print('Person staticField = ' + Person.staticField)
