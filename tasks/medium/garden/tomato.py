class Tomato:

    index: int
    ripeness: str
    states = {0: "Отсутствует", 1: "Цветение", 2: "Зеленый", 3: "Красный"}

    def __init__(self, index=0):
        self.index = index
        self.ripeness = self.states[index]

    def grow(self):
        if self.index < 3:
            self.index += 1
            self.ripeness = self.states[self.index]

    def is_ripe(self):
        return True if self.ripeness == "Красный" else False  # or the same - if index == 4 (so why we need ripeness?)

    def __str__(self):
        return self.ripeness

# Методы:
# - инициализатор **\_\_init\_\_**, который принимает index и присваивает его self.index,
#   а self.ripeness устанавливается первым значением из self.states
# - метод **grow()**, который будет переводить томат на следующую стадию созревания
# - метод **is_ripe()**, который будет проверять, что томат созрел (достиг последней стадии созревания).
#   Должен возвращать True или False


if __name__ == "__main__":

    t1 = Tomato(1)
    t2 = Tomato(0)
    t3 = Tomato(2)
    t1.grow()
    t1.grow()
    t_b = [t1, t2, t3]
    t = 1
    for x in t_b:
        c = 0
        while x.is_ripe() is not True:
            x.grow()
            c += 1
        print(f"tomato #{t} is rape on {c} step")
        print(x.is_ripe())
        t += 1
