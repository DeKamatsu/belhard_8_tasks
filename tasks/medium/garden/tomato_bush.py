from tomato import Tomato


class TomatoBush:

    tomato_list: list
    it_is_ripe = False

    def __init__(self, *args):
        self.tomato_list = list(a for a in args)

    def grow_all(self):
        for t in self.tomato_list:
            t.grow()

    def all_are_ripe(self):
        self.it_is_ripe = True
        for t in self.tomato_list:
            if t.is_ripe() is not True:
                self.it_is_ripe = False
                return False
        return True

    def give_away_all(self):
        ripe_tomato = self.tomato_list
        if self.it_is_ripe:
            self.tomato_list = []
        return ripe_tomato

# Методы:
# - инициализатор **\_\_init\_\_**, который принимает args - произвольное количество томатов
#   и сохраняет их в self.tomato_list
# - метод **grow_all()**, который будет переводить все объекты из списка томатов на следующий этап созревания
# - метод **all_are_ripe()**, который будет возвращать True, если все томаты из списка стали спелыми, False, если нет
# - метод **give_away_all()**, который будет возвращать список томатов и очищать его на кусте томатов после сбора урожая


if __name__ == "__main__":

    # add 7 tomatoes with different kind of ripeness
    t1 = Tomato(1)
    t2 = Tomato(0)
    t3 = Tomato(2)
    t4 = Tomato(0)
    t5 = Tomato(1)
    t6 = Tomato(2)
    t7 = Tomato(3)

    # add 2 bushes with tomatoes
    t_b = TomatoBush(t1, t2, t3)
    t_b2 = TomatoBush(t4, t5, t6, t7)

    # print tomatoes of each bushes
    print('1'*20)
    for y in t_b.give_away_all():
        print(y)
    print(t_b.all_are_ripe())

    print('2'*20)
    for y in t_b2.give_away_all():
        print(y)
    print(t_b2.all_are_ripe())

    # growing bush # 1 until its tomatoes became ripe
    c = 0
    while t_b.all_are_ripe() is not True:
        t_b.grow_all()
        c += 1
        print(c)
    print(f"tomato bush #1 is rape on {c} step")

    # print tomatoes of each bushes, on 1-st bush tomatoes disappears
    print('3'*20)
    for y in t_b.give_away_all():
        print(y)
    print(t_b.all_are_ripe())

    print('4'*20)
    for y in t_b2.give_away_all():
        print(y)
    print(t_b2.all_are_ripe())

    # add disappeared tomatoes on bush #1 and check: they are all ripe
    t_b = TomatoBush(t1, t2, t3)

    print('5'*20)
    for y in t_b.give_away_all():
        print(y)
    print(t_b.all_are_ripe())

    print('6'*20)
    for y in t_b2.give_away_all():
        print(y)
    print(t_b2.all_are_ripe())
