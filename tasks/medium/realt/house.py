# Дом. Класс House - файл house.py

# Дом может:
# 1. Предоставлять информацию о себе
# 2. Изменять свою стоимость
#
# Атрибуты:
# - **address** - адрес дома
# - **area** - площадь дома
# - **cost** - стоимость дома
#
# Методы:
# - инициализатор **\_\_init\_\_**, который принимает адрес, площадь и начальную стоимость дома
# - метод **increase_cost()**, который принимает значение, на которое нужно увеличить self.cost
# - метод **decrease_cost()**, который принимает значение, на которое нужно уменьшить self.cost
# оимость дома


class House:

    address: str
    area: int
    cost: int
    sold: bool

    def __init__(self, address, area, cost):
        self.sold = False
        self.address = address
        self.area = area
        if int(cost) >= 0:
            self.cost = int(cost)
        else:
            raise ValueError('Subzero cost is impossible.')

    def increase_cost(self, delta):
        self.cost += delta

    def decrease_cost(self, delta):
        self.cost -= delta
