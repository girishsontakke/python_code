class Employee:
    raise_amount = 1.5 #class variable
    num_of_emps = 0   


    def __init__(self, first, last, pay):
        self.fname = first  #instance variables
        self.last = last
        self.pay = pay
        self.email = first + last + "@" + "gmail.com"
        Employee.num_of_emps += 1
        
        
    def fullname(self):
        return '{} {}'.format(self.fname, self.last)
    
    def raise_pay(self):
        self.pay = int(self.pay * self.raise_amount)
        
    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.fname, self.last, self.pay)
    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)
    
    def __add__(self, other):
        return self.pay + other.pay
    
emp1 = Employee('Girish', 'Sontakke', 5000)
emp2 = Employee('Ajay', 'Sinha', 6000)
print(emp1)     

# print(repr(emp1))
# print(str(emp1))

print(emp1.__repr__())
print(emp1.__str__())

print(emp1 + emp2)