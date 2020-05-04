from abc import ABCMeta, abstractmethod


class Book(object, metaclass=ABCMeta):
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @abstractmethod
    def display(self):
        print('Something')#this is abstract method and not concrete method


# Write MyBook class
class MyBook(Book):
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
        print(self.author)

    def display(self):
        print('Title:', self.title)
        print('Author:', self.author)
        print('Price:', self.price)
        # super().display()
        # super() is use to instantiate the abstract method in base class


title = 'MyBook'
author = 'Me'
price = 500
new_novel = MyBook(title, author, price)
new_novel.display()
