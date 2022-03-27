# Человек. Класс Person - файл person.py
#
# Человек может:
# 1. Предоставить информацию о себе
# 2. Заработать деньги
# 3. Купить дом
#
# Атрибуты:
# - ** name ** - имя
# - ** age ** - возраст
# - ** money ** - количество денег
# - ** realty ** - недвижимость(список домов)
#
# Методы:
# - инициализатор **\_\_init\_\_ **, который принимает name и age, присваивает их self.name и self.age
# соответственно.self.cash присваивает 0, а self.realty присваивает пустой список - метод ** info() **, который
# будет выводить поля name, age, realty и money.
# - метод ** earn_money() **, который принимает значение, на которое нужно увеличить money
# - метод ** make_deal() **, который принимает объект класса House или Townhouse, и если у человека достаточно
# денег, то списывает их с money и добавляет объект дома к self.realty
#

from house import House
from townhouse import Townhouse


class Person:

    name: str
    age: str
    money: int
    realty: list

    def __init__(self, name, age, money):
        self.name = name
        self.age = age
        self.money = money
        self.realty = list()

    def earn_money(self, income):
        if income >= 0:
            self.money += income
        else:
            raise ValueError("It's subzero income. Impossible!")

    def make_deal(self, house):
        if house.sold is True:
            print('The house was sold earlier!')
        else:
            if type(house) == House or type(house) == Townhouse:
                if self.money >= house.cost:
                    self.money -= house.cost
                    house.sold = True
                    self.realty.append(house)
                    print(f"it's a deal! {self.name} bought a {'house' if type(house) == House else 'townhouse'} "
                          f"{house.area} sq.m. at the address: {house.address}.")
                else:
                    print(f"{self.name} hasn't enough money to buy a {'house' if type(house) == House else 'townhouse'} "
                          f"{house.area} sq.m. at the address: {house.address}.")
            else:
                print(f"{self.name} is trying to buy not a house.")

    def info(self):
        print(f"Client: {self.name}, money: {self.money} units. Real estate owned:")
        c = 1
        for h in self.realty:
            print(f"{c}) {'house' if type(h) == House else 'townhouse'} {h.area} sq.m. area "
                  f"at the address: {h.address}.")
            c += 1
