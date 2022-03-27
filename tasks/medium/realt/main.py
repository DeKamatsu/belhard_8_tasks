# Задача. Файл main.py

if __name__ == '__main__':
    from house import House
    from person import Person
    from townhouse import Townhouse

    # выполнить следующие задания:
    # 1. Создать несколько объектов классов House и Townhouse
    h1 = House('Minsk', 45, 90_000)
    h2 = House('Borisov', 45, 67_000)
    th1 = Townhouse('Minsk', 75, 127_000)
    th2 = Townhouse('Vitebsk', 82_000)
    th3 = Townhouse('Sokol', 200, 150_000)

    houses = [h1, h2, th1, th2, th3]
    for h in houses:
        print(h.address, h.area, h.cost)

    # 2. Создайте объект Person
    Valera = Person('Valerij', 34, 100_000)

    # 3. Используя объект класса Person, увеличить количество денег
    Valera.earn_money(50_000)

    # 4. Попробуйте купить дома
    Valera.make_deal(th1)
    Valera.make_deal(th3)
    Valera.make_deal(th2)

    # 5. Если денег не достаточно, то продолжить увеличивать количество денег
    years_counter = 0
    while len(Valera.realty) < len(houses):
        Valera.earn_money(50_000)
        years_counter += 1
        for h in houses:
            Valera.make_deal(h)
    print(f"{Valera.name} worked for {years_counter} years to buy all real estate on the market!")

    Valera.info()

