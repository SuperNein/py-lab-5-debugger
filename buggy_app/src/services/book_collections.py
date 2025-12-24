from typing import Iterable, Any, Literal

from src.enums.index import Index
from src.services.book import Book


class BookCollection:
    def __init__(self, books: Iterable[Book] | None = None):
        if books is None:
            books = ()
        elif any(not isinstance(book, Book) for book in books):
            raise TypeError("Book elements expected")
        self.__items: list[Book] = list(books)

    def __getitem__(self, key: int | slice):
        return self.__items[key]

    def copy(self) -> BookCollection:
        return BookCollection(self.__items[:])

    def __iter__(self):
        return iter(self.__items)

    def __len__(self):
        return len(self.__items)

    def __contains__(self, item: Any):
        return item in self.__items

    def append(self, item: Book) -> None:
        if not isinstance(item, Book):
            raise TypeError(f"Book object expected, {type(item)} given")
        self.__items.append(item)

    def remove(self, item: Book) -> None:
        if not isinstance(item, Book):
            raise TypeError(f"Book object expected, {type(item)} given")
        self.__items.remove(item)

    def pop(self, key: int = -1):
        res = self[key]
        del self[key]
        return res

    def __delitem__(self, key: int | slice):
        del self.__items[key]

    def __setitem__(self, key: int, value: Book):
        if not isinstance(value, Book):
            raise TypeError(f"Book object expected, {type(value)} given")
        self.__items[key] = value

    def __str__(self) -> str:
        return str([str(book) for book in self.__items])

    def __add__(self, other: BookCollection) -> BookCollection:
        if not isinstance(other, BookCollection):
            raise TypeError(f"cannot add BookCollection with {type(other)}")
        return BookCollection(self.__items + other.__items)

    def __iadd__(self, other: BookCollection) -> BookCollection:
        if not isinstance(other, BookCollection):
            raise TypeError(f"cannot add {type(other)} to BookCollection")
        self.__items.extend(other.__items)
        return self

    def index(self, item: Book) -> int:
        return self.__items.index(item)


class IndexDict:
    def __init__(
            self,
            index: Literal[Index.isbn, Index.author, Index.year] = "isbn",
            books: Iterable[Book] | None = None):
        if index not in Index:
            raise TypeError(f"index must be one of {[ind for ind in Index]}")
        self.index = index

        if isinstance(books, BookCollection):
            self.__items = books
        elif any(not isinstance(book, Book) for book in books):
            raise TypeError("Book elements expected")
        else:
            self.__items = BookCollection(books)

    def __generate_dict(self) -> dict[str, BookCollection]:
        """Generate actual dictionary of collection"""
        res: dict[str, BookCollection] = dict()
        books = self.__items.copy()
        while books:
            book = books.pop()
            key = getattr(book, self.index)
            if key not in res:
                res[key] = BookCollection((book,))
            else:
                res[key].append(book)
        return res

    def __iter__(self):
        return iter(self.__generate_dict())

    def __len__(self):
        return len(self.__generate_dict())

    def remove(self, item: Book) -> None:
        if not isinstance(item, Book):
            raise TypeError(f"Book object expected, {type(item)} given")
        self.__items.remove(item)

    def append(self, item: Book) -> None:
        if not isinstance(item, Book):
            raise TypeError(f"Book object expected, {type(item)} given")
        self.__items.append(item)

    def __getitem__(self, key: Any) -> BookCollection:
        d = self.__generate_dict()
        if key is None:
            return self.__items.copy()
        return d.get(key, BookCollection())
