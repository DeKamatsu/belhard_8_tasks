from tomato_bush import TomatoBush


class Gardener:

    name: str
    plants: list

    def __init__(self, name, *args):
        self.name = name
        self.plants = list(a for a in args)

    def work(self):
        for p in self.plants:
            p.grow_all()
            # for i in p.give_away_all():
                # print("Зрелость помидорки", i)

    def harvest(self):
        ripe_tomato_list = []
        for p in self.plants:
            if p.all_are_ripe():
                ripe_tomato_list.extend(p.give_away_all())
            else:
                print("Томаты еще не созрели")
                return None
        return ripe_tomato_list

# Методы:
# - инициализатор **\_\_init\_\_**, который принимает name - имя садовника
#   и args - произвольное количество кустов томата
# - метод **work()**, который заставляет садовника работать, что позволяет всем растениям расти
# - метод **harvest()**, который проверяет, все ли плоды созрели.
#   Если созрели все плоды - садовник собирает урожай (метод возвращает список всех томатов),
#   если нет - метод печатает предупреждение, что томаты не созрели и возвращает None.


if __name__ == "__main__":

    pass
