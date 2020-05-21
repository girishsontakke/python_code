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



emp1 = Employee('girish', 'Sontakke', 5000)
emp2 = Employee('girish2', 'Sontakke2', 4000)

print(emp1.pay)
print(emp1.fullname())
print(emp1.__dict__)
print(Employee.__dict__)
emp1.raise_amount = 2
print(emp1.__dict__)
print(emp2.__dict__)
print(emp1.raise_amount)
print(emp2.raise_amount)
print(Employee.raise_amount)