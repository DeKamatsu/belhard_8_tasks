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

    def take_books(self, args):
        for b in args:
            self.books.add(b)
        if 0 < len(args) < 4:
            print(f"{self.fullname} взял(а) книги: {b}")
        elif len(args) > 0:
            print(f"{self.fullname} взял(а) {len(args)} книги.")

    def return_book(self, args):
        for b in args:
            if b not in self.books:
                raise ValueError(f"Петров В. В. не брал: {b}")
        for b in args:
            self.books.remove(b)
        if 0 < len(args) < 4:
            for b in args:
                print(f"{self.fullname} вернул(а) книги: {b}")
        elif len(args) > 0:
            print(f"{self.fullname} вернул(а) {len(args)} книги.")

# library_reader = LibraryReader("Fullname", "375557894545", 123)
# print(library_reader.fullname)
# print(library_reader.phone)
# print(library_reader.uid)
# print(library_reader.books)
#
# expected = {"Азбука", "Буратино"}
# library_reader.take_books(expected)
# print(library_reader.books)
#
# new_books = {"Весна", "Дом у озера", "Оно", "Страна радости"}
# library_reader.take_books(new_books)
# print(library_reader.books)
#
# expected = {"Азбука", "Буратино"}
# library_reader.return_book(expected)
# print(library_reader.books)
#
# new_books = {"Весна", "Дом у озера", "Страна радости", "Оно"}
# library_reader.return_book(new_books)
# print(library_reader.books)
