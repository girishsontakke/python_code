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

class Developer(Employee):
    raise_amount = 1.10
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        # Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())
            


#inheritance use method resolution order
dev1 = Developer('Girish', 'Sontakke', 50000, "python")
emp1 = Employee('tejas', 'chaudhary', 50000)
print("dev1 email =",dev1.email)
# print(help(Developer))
print("Salary of dev1 =", dev1.pay)
dev1.raise_pay()
print("Salary of dev1 after upraisal =", dev1.pay)
print("Salary of emp1",emp1.pay)
emp1.raise_pay()
print("Salary of emp1 after upraisal =", emp1.pay)

print("Programming Language of dev1 =", dev1.prog_lang)

#instantiating manager class

mng_1 = Manager('ajay', 'sinha', 6000, [dev1])
print('Email of manager1 =', mng_1.email)
mng_1.add_emp(emp1)
print("List of employees after adding tejas")
mng_1.print_emps()
mng_1.remove_emp(emp1)
print("List of employees after removing tejas")
mng_1.print_emps()

#Some built-in functions

print(isinstance(mng_1, Employee))
print(isinstance(mng_1, Developer))
print(issubclass(Manager, Developer))
print(issubclass(Manager, Employee))
