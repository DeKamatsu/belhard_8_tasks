# Таунхаус. Класс Townhouse - подкласс House, файл townhouse.py

# Типовой дом
#
# Методы:
# - инициализатор **\_\_init\_\_**, который принимает адрес и начальную стоимость дома.
#   self.area по умолчанию присваиваем 60

from house import House


class Townhouse(House):

    def __init__(self, address, area, cost=0):
        super().__init__(address, area, cost)
        self.sold = False
        if cost == 0:
            self.area = 60
            self.cost = int(area)
        else:
            self.address = address
            self.area = area
            if int(cost) >= 0:
                self.cost = int(cost)
            else:
                raise ValueError('Subzero cost is impossible.')
