# Задача. Файл main.py

if __name__ == '__main__':
    from house import House
    from townhouse import Townhouse
    from person import Person

    # выполнить следующие задания:
    # 1. Создать несколько объектов классов House и Townhouse
    h1 = House('Minsk', 45, 50_000)
    h2 = House('Borisov', 45, 27_000)
    th1 = Townhouse('Minsk', 75, 87_000)
    th2 = Townhouse('Vitebsk', 62_000)
    th3 = Townhouse('Sokol', 200, 150_000)

    # 2. Создайте объект Person
    Valera = Person('Valerij', 34, 100_000)
    # 3. Используя объект класса Person, увеличить количество денег
    Valera.earn_money(30_000)
    # 4. Попробуйте купить дома
    Valera.make_deal(h1)
    # 5. Если денег не достаточно, то продолжить увеличивать количество денег
