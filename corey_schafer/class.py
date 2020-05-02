class Employee:
    def __init__(self, first, last, pay):
        self.fname = first
        self.last = last
        self.pay = pay
        self.email = first + last + "@" + "gmail.com"

    def fullname(self):
        return '{} {}'.format(self.fname, self.last)


emp1 = Employee('girish', 'Sontakke', 5000)
print(emp1.pay)
print(emp1.fullname())
