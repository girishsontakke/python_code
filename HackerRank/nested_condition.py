import datetime
class Library:
   def __init__(self, return_date, expected_date):
      self.return_date = return_date
      self.expected_date = expected_date
   
   def calculate_fine(self):
      if self.return_date[2] <= self.expected_date[2]:
         if self.return_date[2] == self.expected_date[2]:
            if self.return_date[1] <= self.expected_date[1]:
               if self.return_date[1] == self.expected_date[1]:
                  if self.return_date[0] <= self.expected_date[0]:
                     return 0
                  else:
                     return 15 *(self.return_date[0] - self.expected_date[0])
               else:
                  return 0
            else:
               return 500 *(self.return_date[1] - self.expected_date[1])
         else:
            return 0
      else:
         return 10000     
         

rdate = list(map(int, input().strip().split()))
edate = list(map(int, input().strip().split()))
library = Library(rdate, edate)
print(library.calculate_fine())

