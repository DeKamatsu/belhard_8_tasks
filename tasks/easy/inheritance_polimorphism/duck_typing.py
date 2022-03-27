"""
Создать 3 класса:

AmericanPerson, RussianPerson, GermanyPerson

в каждом классе определить метод i_love_science()

AmericanPerson.i_love_science() -> "I love science"
RussianPerson.i_love_science() - "Я люблю науку"
GermanyPerson.i_love_science() - "ich liebe Wissenschaft"


Написать функцию person_love_science, которая принимает объект и вызывает метод
i_love_science. Функция должна возвращать строку вида
"{obj.__class__.__name__} says that: {obj.i_love_science()}"

В блоке if __name__ == "__main__": сделать объекты трех классов и по очереди
передать их в функцию person_love_science.

https://www.youtube.com/watch?v=8o7ZKTvZpLc
"""


class AmericanPerson:

    @staticmethod
    def i_love_science():
        return "I love science"


class RussianPerson:

    @staticmethod
    def i_love_science():
        return "Я люблю науку"


class GermanyPerson:

    @staticmethod
    def i_love_science():
        return "ich liebe Wissenschaft"


def person_love_science(arg):
    return f"{arg.__class__.__name__} says that: {arg.i_love_science()}"


if __name__ == "__main__":
    a = AmericanPerson()
    r = RussianPerson()
    g = GermanyPerson()
    people = [a, r, g]
    for p in people:
        print(p.i_love_science())

    p = GermanyPerson()
    print(person_love_science(p))
