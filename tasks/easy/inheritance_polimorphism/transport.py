"""
Описать абстрактный класс Transport:

- атрибут brand - фирма, выпустившая транспорт (тип - str)
- атрибут model - модель (тип - str)
- атрибут issue_year - год выпуска (тип - int)
- атрибут color - цвет (тип - str)
- атрибут mileage - пробег (тип - int)
- магический метод __init__, который принимает brand, model, issue_year и color,
  а mileage устанавливает значение 0
- абстрактный метод move, который принимает num_km - количество километров,
  которое должен пройти транспорт, проверяет, чтобы num_km было больше 0 и
  увеличивает mileage на значение num_km. Если num_km меньше 0, то бросить
  исключение ValueError("Расстояние должно быть положительным числом")

Описать класс Car, который наследуется от Transport:

- атрибут engine_type - тип двигателя (тип str)
- магический метод __init__, который принимает brand, model, issue_year и color
  и engine_type
- переопределить метод move. Внутри метода вызвать родительский метод, а потом
  вернуть строку "{brand} {model} ({color} - {issue_year}) проехала {km}
  километров"

Описать класс Airplane, который наследуется от Transport:

- атрибут lifting_capacity - грузоподъемность (тип - int)
- магический метод __init__, который принимает brand, model, issue_year и color
  и lifting_capacity
- переопределить метод move. Внутри метода вызвать родительский метод, а потом
  вернуть строку "{brand} {model} ({color} - {issue_year}) пролетел {km}
  километров"
"""


from abc import ABC, abstractmethod


class Transport(ABC):

    brand: str
    model: str
    issue_year: int
    color: str
    mileage: int

    def __init__(self, brand, model, issue_year, color):
        self.brand = brand
        self.model = model
        self.issue_year = issue_year
        self.color = color
        self.mileage = 0

    @abstractmethod
    def move(self, num_km):
        if num_km > 0:
            self.mileage += num_km
        else:
            raise ValueError("Расстояние должно быть положительным числом")


class Car(Transport):

    engine_type: str

    def __init__(self, brand, model, issue_year, color, engine_type):
        super().__init__(brand, model, issue_year, color)
        self.engine_type = engine_type

    def move(self, num_km):
        Transport.move(self, num_km)
        return f"{self.brand} {self.model} ({self.color} - {self.issue_year}) проехала {self.mileage} километров"


class Airplane (Transport):

    lifting_capacity: int

    def __init__(self, brand, model, issue_year, color, lifting_capacity):
        super().__init__(brand, model, issue_year, color)
        self.lifting_capacity = lifting_capacity

    def move(self, num_km):
        Transport.move(self, num_km)
        return f"{self.brand} {self.model} ({self.color} - {self.issue_year}) пролетел {self.mileage} километров"


# Transport("toyota", "supra A80", 1999, "black")
#
# car = Car("toyota", "supra A80", 1999, "black", "petrol")
# # car.move(0)
# print(car.mileage)
# car.move(-15)
# print(car.mileage)
# result = car.move(15)
# print(car.mileage)
#
# airplane = Airplane("Боинг", "737", 2000, "white", 200)
# # # airplane.move(0)
# # airplane.move(-15)
# result = airplane.move(1005)
# result = airplane.move(688)
# print(airplane.mileage)
