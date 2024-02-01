class Book:
    def __init__(self, id: int, name: str, pages: int):
        """
        Создание и подготовка к работе объекта "Книга"

        :param id: Айди
        :param name: Название
        :param pages: Количество страниц

        """
        if not isinstance(id, (int)):
            raise TypeError("id книги должен быть типа int")
        if id <= 0:
            raise ValueError("id книги должен быть положительным числом")
        self.id = id

        if not isinstance(name, (str)):
            raise TypeError("Название книги должно быть string")
        self.name = name
        if not isinstance(pages, (int)):
            raise TypeError("количество страниц книги должен быть типа int")
        if id <= 0:
            raise ValueError("У книги не может быть 0 и меньше страниц")
        self.pages = pages

    def __str__(self) -> str:
        return f'название книги "{self.name}"'
    def __repr__(self) -> str:
        return f'книга (id={self.id},name={self.name!r},pages={self.pages})'
class Library:
    def __init__(self, books: list):
        if len(books) == 0:
            return books
        else:
            self.books=books
    def get_next_book_id(self,id: int):
        if len(books) == 0:
            return 1
        else:
            id+=1
            return id
    def get_index_by_book_id(self,id: int):
        if id in self.books:
            return self.books.index[id]
        else:
            raise ValueError('Книги с запрашиваемым id не существует')


