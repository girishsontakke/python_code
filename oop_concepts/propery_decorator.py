#property decorator enables our class attribute to have getter, setter, deleter functionality and class methods to behave like attributes
class Employee:
    raise_amount = 1.5 #class variable
    num_of_emps = 0   

    def __init__(self, first, last, pay):
        self.fname = first  #instance variables
        self.last = last
        self.pay = pay
        Employee.num_of_emps += 1
    
    #creating method which can be called as attribute
    @property     
    def email(self):
        return '{}{}@gmail.com'.format(self.fname, self.last)   
    
    @property    
    def fullname(self):
        return '{} {}'.format(self.fname, self.last)
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split()
        self.fname = first
        self.last = last
     
    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.fname = None
        self.last = None
        
emp1 = Employee('Girish', 'Sontakke', 5000)
emp1.fname = 'tejas'
print(emp1.fname)
print(emp1.last)
# calling methods as attributes
print(emp1.fullname)
print(emp1.email)

emp1.fullname = 'Ajay Sinha'
print(emp1.fname)
print(emp1.email)
print(emp1.fullname)

del emp1.fullname

print(emp1.fname)