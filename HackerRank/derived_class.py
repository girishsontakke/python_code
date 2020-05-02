class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    #   Class Constructor
    def __init__(self, firstName, lastName, idNumber, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores = scores

    def calculate(self):
        sm = sum(scores)
        a = sm / len(scores)
        if (a <= 100) and (a >= 90):
            grd = 'O'
        elif (a < 90) and (a >= 80):
            grd = 'E'
        elif (a < 80) and (a >= 70):
            grd = 'A'
        elif (a < 70) and (a >= 55):
            grd = 'P'
        elif (a < 55) and (a >= 40):
            grd = 'D'
        else:
            grd = 'T'

        return grd


firstName = 'girish'
lastName = 'Sontakke'
idnum = 123654
scores = [100, 80]
s = Student(firstName, lastName, idnum, scores)
s.printPerson()
print("Grade:", s.calculate())
