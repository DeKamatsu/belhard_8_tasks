from tomato import Tomato


class TomatoBush:

    tomato_list: list

    def __init__(self, args):
        self.tomato_list.extend(args(Tomato))

    def grow_all(self):
        for t in self.tomato_list:  # не нужно?
            Tomato.grow()

    def all_are_ripe(self):
        is_ripe = True
        for t in self.tomato_list:  # не нужно?
            if Tomato.is_ripe():
                is_ripe = False
        return is_ripe

    def give_away_all(self):
        ripe_tomato = self.tomato_list
        self.tomato_list = []
        return ripe_tomato

# Методы:
# - инициализатор **\_\_init\_\_**, который принимает args - произвольное количество томатов
#   и сохраняет их в self.tomato_list
# - метод **grow_all()**, который будет переводить все объекты из списка томатов на следующий этап созревания
# - метод **all_are_ripe()**, который будет возвращать True, если все томаты из списка стали спелыми, False, если нет
# - метод **give_away_all()**, который будет возвращать список томатов и очищать его на кусте томатов после сбора урожая

