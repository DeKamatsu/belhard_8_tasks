"""
Создать класс BookCard, в классе должны быть:

- private атрибут author - автор (тип str)
- private атрибут title - название книги (тип str)
- private атрибут year - год издания (тип int)
- магический метод __init__, который принимает author, title, year
- магические методы сравнения для сортировки книг по году издания
- сеттеры и геттеры к атрибутам author, title, year. В сеттерах сделать проверку
  на тип данных, если тип данных не подходит, то бросить ValueError. Для года
  издания дополнительно проверить на валидность (> 0, <= текущего года).

Аксессоры реализоваться через property.
"""
from datetime import date

CURRENT_YEAR = date.today().year


class BookCard:

    __author: str
    __title: str
    __year: int

    def __init__(self, author, title, year):
        if type(author) != str \
                or type(title) != str \
                or type(year) != int \
                or year <= 0 \
                or year > date.today().year:
            raise ValueError
        else:
            self.__author = author
            self.__title = title
            self.__year = year

    def __cmp__(self, other):
        return self.__year - other.year

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, val: str):
        if type(val) != str:
            raise ValueError
        else:
            self.__author = val

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, val: str):
        if type(val) != str:
            raise ValueError
        else:
            self.__title = val

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, val: int):
        print(type(val))
        print(val)
        print(date.today().year)
        if type(val) != int or val <= 0 or val > date.today().year:
            raise ValueError
        else:
            self.__year = val


# a = BookCard('1w', 'gheh', 2022)
# print(a.year, a.title, a.author)
# b = BookCard('2w', "hhhh", 4)
# print(b.year, b.title, b.author)
# print(a == b)
