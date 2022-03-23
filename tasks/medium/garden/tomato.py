class Tomato:

    index: int
    ripeness: str
    states = ("Отсутствует", "Цветение", "Зеленый", "Красный")

    def __init__(self, index):
        self.index = index
        self.ripeness = self.states[0]

    def grow(self):
        if self.states.index(self.ripeness) < 3:
            self.ripeness = self.states[self.states.index(self.ripeness) + 1]

    def is_ripe(self):
        return True if self.states.index(self.ripeness) == 4 else False

# Методы:
# - инициализатор **\_\_init\_\_**, который принимает index и присваивает его self.index,
#   а self.ripeness устанавливается первым значением из self.states
# - метод **grow()**, который будет переводить томат на следующую стадию созревания
# - метод **is_ripe()**, который будет проверять, что томат созрел (достиг последней стадии созревания).
#   Должен возвращать True или False

