import datetime


class Library:
    def __init__(self, return_date, expected_date):
        self.return_date = datetime.datetime.strptime(return_date, '%d %m %Y')
        self.expected_date = datetime.datetime.strptime(expected_date, '%d %m %Y')

    def calculate_fine(self):
        if self.return_date > self.expected_date:
            if self.return_date.year == self.expected_date.year:
                if self.return_date.month == self.expected_date.month:
                    return 15 * (self.return_date.day - self.expected_date.day)
                else:
                    return 500 * (self.return_date.month - self.expected_date.month)
            else:
                return 10000
        else:
            return 0


rdate = input()
edate = input()
library = Library(rdate, edate)
print(library.calculate_fine())
