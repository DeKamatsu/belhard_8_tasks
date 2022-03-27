from gardener import Gardener
from tomato import Tomato
from tomato_bush import TomatoBush

if __name__ == '__main__':

    # ```
    # выполнить следующие задания:
    # 1. Создать несколько объектов класса TomatoBush,
    #    в каждом из которых будет минимум по 2 помидора
    tb1 = TomatoBush(Tomato(0), Tomato(0))
    tb2 = TomatoBush(Tomato(1), Tomato(2))

    # 2. Создайте объект Gardener, в который передать объекты, созданные в п.1
    gard = Gardener("Semen", tb1, tb2)

    # 3. Используя объект класса Gardener, поухаживайте за кустом с помидорами
    gard.work()
    # 4. Попробуйте собрать урожай
    gard.harvest()
    # 5. Если томаты еще не дозрели, продолжайте ухаживать за ними
    # 6. Соберите урожай
    ripe_tomato_list = None
    while ripe_tomato_list is None:
        gard.work()
        ripe_tomato_list = gard.harvest()

    # 7. Вывести сообщение о том, сколько томатов собрали

    for t in ripe_tomato_list:
        print(t)

    print(f"Собрано {len(ripe_tomato_list)} шт. помидор")

    # checking that ere is no more tomatoes on the bushes
    ripe_tomato_list = gard.harvest()
    for t in ripe_tomato_list:
        print(t)
    print(f"Собрано {len(ripe_tomato_list)} шт. помидор")
