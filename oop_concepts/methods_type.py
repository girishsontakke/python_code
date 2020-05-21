class Employee:

   raise_amount = 1.5  # class variable
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

   @classmethod
   def set_raise_amount(cls, amount):
      cls.raise_amount = amount
      
   #classmethod to create objects
   #classmethod as alternative constructor
   @classmethod
   def from_string(cls, emp_str):
      first, last, pay = emp_str.split('-')
      return cls(first, last, pay)
   
   @staticmethod
   def is_workday(date):
      if date.weekday() == 5 or date.weekday() == 6:
         return False
      return True
      
emp1 = Employee('girish', 'Sontakke', 4000)
print(Employee.raise_amount)
print(emp1.raise_amount)

Employee.set_raise_amount(2)
print(Employee.raise_amount)
print(emp1.raise_amount)

# emp1.set_raise_amount(3) #we should not run class method with instances
# print(Employee.raise_amount)
# print(emp1.raise_amount)

emp_str1 = "tejas-sontakke-3000"
new_emp = Employee.from_string(emp_str1)
print(new_emp.email)
print(new_emp.pay)

import datetime
date = datetime.date(2020, 5, 9)
print(Employee.is_workday(date))
date1 = datetime.date(2020, 5, 11)
print(Employee.is_workday(date1))
