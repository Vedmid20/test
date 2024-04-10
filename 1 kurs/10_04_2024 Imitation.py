from colorama import *

class Library:
    def __init__(self):
        self.lstofbooknames = []
        self.lstofauthor = []
        self.lstofyear = []

    def addBookName(self):
        bookNameInput = input('Введіть назву книги: ')
        ex2.lstofbooknames.append(f'Назва книги: {bookNameInput}')

    def addAuthor(self):
        authorInput = input('Введіть автора книги: ')
        ex2.lstofauthor.append(f'автор книги: {authorInput}')

    def addYear(self):
        yearInput = input('Введіть рік випуску: ')
        ex2.lstofyear.append(f'рік випуску: {yearInput}')

    def pars(self):
        for i in ex2.lstofbooknames:
            for j in ex2.lstofauthor:
                for s in ex2.lstofyear:
                    print(i, j, s)
        print(f'Додані книги в бібліотеку користувачем: {ex3.name} {ex3.lastname}')

class Book:
    def __init__(self, bookname, author, year):
        self.bookname = bookname
        self.author = author
        self.year = year

class User:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname


ex2 = Library()

ex3 = User(name=input('Введіть своє імя: '), lastname=input('Введіть своє прізвище: '))
def menu():
    print(f'1.Додати нові книги\n2.Видалити книги з катлогу\n3.Повернути книгу в бібліотеку')
    choice = int(input('Оберіть операцію номером: '))
    if choice == 1:
        ex1 = Book(bookname=ex2.lstofbooknames, author=ex2.lstofauthor, year=ex2.lstofyear)
        ex2.addBookName()
        ex2.addAuthor()
        ex2.addYear()
        ex2.pars()
    elif choice == 2:
        menu()
    elif choice == 3:
        menu()
    else:
        pass
menu()