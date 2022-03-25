# Таунхаус. Класс Townhouse - подкласс House, файл townhouse.py

# Типовой дом
#
# Методы:
# - инициализатор **\_\_init\_\_**, который принимает адрес и начальную стоимость дома.
#   self.area по умолчанию присваиваем 60

from house import House


class Townhouse(House):

    def __init__(self, address, cost, area=60):
        super().__init__(address, area, cost)
        self.address = address
        self.area = area
        self.cost = cost
