from tomato_bush import TomatoBush


class Gardener:

    name: str
    plants: list

    def __init__(self, name, args):
        self.name = name
        self.plants.extend(args)

    def work(self):
        for p in self.plants:  # не нужно?
            TomatoBush.grow_all()

    def harvest(self):
        for p in self.plants:  # не нужно?
            if TomatoBush.all_are_ripe:
                return TomatoBush.give_away_all()
            else:
                print("Томаты еще не созрели")
                return None

# Методы:
# - инициализатор **\_\_init\_\_**, который принимает name - имя садовника
#   и args - произвольное количество кустов томата
# - метод **work()**, который заставляет садовника работать, что позволяет всем растениям расти
# - метод **harvest()**, который проверяет, все ли плоды созрели.
#   Если созрели все плоды - садовник собирает урожай (метод возвращает список всех томатов),
#   если нет - метод печатает предупреждение, что томаты не созрели и возвращает None.

