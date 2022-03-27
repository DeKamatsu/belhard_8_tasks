"""
Описать класс Warrior:

- атрибут name - имя юнита (тип str)
- атрибут health_points - показатель здоровья (тип int от 0 до 100)
- магический метод __init__, который принимает аргумент name и создает юнита со
  100 health_points
- метод hit, который принимает аргумент other типа Warrior. Если значение
 health_points у other <= 0 бросить исключение ValueError("Второй воин мертв").
 Если нет, то снять у other 20 health_points и вывести на экран сообщение
 "{self.name} атаковал {other.name}. У {other.name} {other.health_points} HP"

Описать класс Arena:

- атрибут warriors - все воины на арене (тип list)
- магический метод __init__, который принимает необязательный аргумент warriors.
 Если был передан список warriors, та заполняет им атрибут. Если нет, то заполняет
 пустым списком.
- метод add_warrior, который принимает аргумент warrior и добавляет его к warriors.
 Если данный воин уже есть в списке, то бросить исключение ValueError("Воин уже на арене").
 Если нет, то добавить воина к списку warriors и вывести сообщение на экран
 "{warrior.name} участвует в битве"
- метод choose_warrior, который не принимает аргументов и возвращает случайного
  воина из warriors
- метод battle, который не принимает аргументов и симулирует битву. Сперва
 должна пройти проверка, что воинов на арене больше 1. Если меньше, то бросить
 исключение ValueError("Количество воинов на арене должно быть больше 1").
 Битва продолжается, пока на арене не останется только один воин. Сперва
 в случайном порядке выбираются атакующий и защищающийся. Атакующий ударяет
 защищающегося. Если у защищающегося осталось 0 health_points, то удалить его
 из списка воинов и вывести на экран сообщение "{defender.name} пал в битве".
 Когда останется только один воин, то вывести сообщение "Победил воин: {winner.name}".
 Вернуть данного воина из метода battle.
"""
import random


class Warrior:

    name: str
    health_points: int

    def __init__(self, name):
        self.name = name
        self.health_points = 100

    def hit(self, other):
        if type(other) == Warrior:
            if other.health_points <= 0:
                raise ValueError("Второй воин мертв")
            else:
                other.health_points -= 20
                print(f"{self.name} атаковал {other.name}. У {other.name} осталось {other.health_points} HP")
        else:
            raise TypeError("Это вообще не воин!")


class Arena:

    warriors: list

    def __init__(self, *args):
        self.warriors = list()
        for a in args:
            self.warriors.extend(a)

    def add_warrior(self, *args):
        for w in args:
            if w in self.warriors:
                raise ValueError("Воин уже на арене")
            else:
                self.warriors.append(w)
                print(f"{w.name} участвует в битве")

    def choose_warrior(self):
        return self.warriors[random.randint(0, len(self.warriors) - 1)]

    def battle(self):
        if len(self.warriors) < 2:
            raise ValueError("Количество воинов на арене должно быть больше 1")
        else:
            while len(self.warriors) != 1:
                w1 = self.warriors[random.randint(0, len(self.warriors) - 1)]
                w2 = self.warriors[random.randint(0, len(self.warriors) - 1)]
                while w2 == w1:
                    w2 = self.warriors[random.randint(0, len(self.warriors) - 1)]
                w1.hit(w2)
                if w2.health_points <= 0:
                    print(f"{w2.name} пал в битве")
                    self.warriors.remove(w2)
            print(f"Победил воин: {self.warriors[0].name}")
            return self.warriors[0]


# ===================================================================================================

if __name__ == '__main__':

    warrior = Warrior("war_name")

    print(warrior.name == "war_name")
    print(warrior.health_points == 100)

    attacker = Warrior("attacker")
    print(hasattr(attacker, "hit"))

    defender = Warrior("defender")
    print(defender.health_points == 100)
    attacker.hit(defender)
    print(defender.health_points == 80)

    defender.health_points = 0
    # while ValueError:
    #     attacker.hit(defender)

    empty_arena = Arena()

    print(isinstance(empty_arena.warriors, list))
    print(len(empty_arena.warriors) == 0)

    warrior = Warrior("Warrior")
    warrior2 = Warrior("Warrior2")
    arena_with_warriors = Arena([warrior])

    print(isinstance(arena_with_warriors.warriors, list))
    print(len(arena_with_warriors.warriors) == 1)
    print(warrior in arena_with_warriors.warriors)

    arena = Arena()
    warrior = Warrior("Warrior")

    arena.add_warrior(warrior)
    print(len(arena.warriors) == 1)
    print(warrior in arena.warriors)

    # arena.add_warrior(warrior)

    arena = Arena()
    warrior = Warrior("Warrior")
    arena.warriors.append(warrior)

    print(warrior is arena.choose_warrior())

    arena = Arena()
    # arena.battle()

    arena.warriors.append(Warrior("Warrior"))
    # arena.battle()

    for i in range(5):
        arena.warriors.append(Warrior(f"Warrior # {i}"))

    winner = arena.battle()

    print(winner in arena.warriors)
    print(len(arena.warriors) == 1)
