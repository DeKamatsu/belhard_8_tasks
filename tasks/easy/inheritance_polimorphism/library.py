"""
Определить класс Person:

- атрибут fullname - ФИО (тип str)
- атрибут phone - номер телефона (тип str)
- магический метод __init__, который принимает fullname и phone

Описать класс LibraryReader, который наследуется от Person:

- атрибут uid - номер читательского билета (тип int)
- атрибут books - список книг (тип set)
- магический метод __init__, который принимает fullname, phone, uid, а books
  заполняет пустым множеством
- метод take_books(*args), который принимает произвольное количество книг
  (книга - строка с названием книги) и возвращает строку: "Петров В.В. взял(а)
  книги: Приключения, Словарь, Энциклопедия", если было взято до 3 книг
  включительно. Если было взято больше книг, то возвращает строку: "Петров В.В.
  взял(а) 4 книги".
- метод return_book(*args), который принимает произвольное количество книг
  (книга - строка с названием книги) и возвращает строку: "Петров В.В. вернул(а)
  книги: Приключения, Словарь, Энциклопедия", если было возвращено до 3 книг
  включительно. Если было возвращено больше книг, то возвращает строку:
  "Петров В.В. вернул(а) 4 книги". Если какой-то книги нет, то бросить исключение
  ValueError с сообщением "Петров В. В. не брал: Рассказы", при этом книги не
  должны быть удалены

Названия книг в сообщениях должны быть отсортированы по алфавиту.
"""


class Person:

    fullname: str
    phone: str

    def __init__(self, fullname, phone):
        self.fullname = fullname
        self.phone = phone


class LibraryReader(Person):

    uid: int
    books: set

    def __init__(self, fullname, phone, uid):
        super().__init__(fullname, phone)
        self.uid = uid
        self.books = set()

    def take_books(self, *args):
        if type(args[0]) == set:
            args = args[0]
        for b in args:
            self.books.add(b)
        if 0 < len(args) < 4:
            return f"{self.fullname} взял(а) книги: {', '.join(sorted(args))}"
        elif len(args) >= 4:
            return f"{self.fullname} взял(а) {len(args)} книги"

    def return_book(self, *args):
        if type(args[0]) == set:
            args = args[0]
        is_error = False
        for b in args:
            if b not in sorted(self.books):  # i'm not sure in conditions of the technical task,
                # but set return elements in random order so i had to sort it to pass tests
                is_error += True
                raise ValueError(f"{self.fullname} не брал: {b}")
        if is_error is False:
            for b in args:
                self.books.remove(b)
        if 0 < len(args) < 4:
            return f"{self.fullname} вернул(а) книги: {', '.join(args)}"
        elif len(args) >= 4:
            return f"{self.fullname} вернул(а) {len(args)} книги"


if __name__ == '__main__':

    library_reader = LibraryReader("Fullname", "375557894545", 123)

    expected = {"Азбука", "Буратино"}

    result = library_reader.take_books(*expected)

    print(library_reader.books == expected)

    new_books = {"Весна", "Дом у озера", "Оно", "Страна радости"}

    expected.update(new_books)
    result = library_reader.take_books(*new_books)
    result == "Fullname взял(а) 4 книги"
    print(library_reader.books == expected)

    try:
        library_reader.return_book("Азбука", "Страна радости")
    except ():
        print("Error")

    library_reader = LibraryReader("Fullname", "375557894545", 123)
    library_reader.books = {
        "Азбука", "Буратино", "Весна", "Дом у озера", "Оно", "Страна радости"
    }
    result = library_reader.return_book(
        "Весна", "Дом у озера", "Оно", "Страна радости"
    )
    print(result == "Fullname вернул(а) 4 книги")

    print(len(library_reader.books) == 2)
    result = library_reader.return_book("Азбука", "Буратино")
    print(result == "Fullname вернул(а) книги: Азбука, Буратино")
