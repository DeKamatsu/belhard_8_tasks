"""
Описать абстрактный класс Animal у которого:

- атрибут name - кличка (тип str)
- магический метод __init__, который принимает аргумент name
- абстрактный метод says, который не принимает аргументов

На основе Animal определить классы Cat, Dog, Cow, которые переопределят метод
says таким образом, чтобы он возвращал строку вида:

- "{кличка} - кошка. Говорит МЯУ!" для класса Cat
- "{кличка} - собака. Говорит ГАВ!" для класса Dog
- "{кличка} - корова. Говорит МУ!" для класса Cow
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    name: str

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def say(self):
        pass


class Cat(Animal):
    def say(self):
        return f'{self.name} - кошка. Говорит МЯУ!'


class Dog(Animal):
    def say(self):
        return f'{self.name} - собака. Говорит ГАВ!'


class Cow(Animal):
    def say(self):
        return f'{self.name} - корова. Говорит МУ!'


# a = [Cat('Tom'), Dog('Rex'), Cow('Pestrushka')]
# for i in a:
#     print(i.say())
