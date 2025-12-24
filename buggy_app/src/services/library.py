from typing import Any

from src.enums.index import Index
from src.services.book import Book
from src.services.book_collections import BookCollection, IndexDict


class Library:
    def __init__(self):
        self._books = BookCollection()
        self._index_isbn = IndexDict(Index.isbn, self._books)
        self._index_author = IndexDict(Index.author, self._books)
        self._index_year = IndexDict(Index.year, self._books)

    def __contains__(self, item: Book) -> bool:
        return item in self._books

    def __iter__(self):
        return iter(self._books)

    def append(self, item: Book) -> None:
        self._books.append(item)

    def remove(self, item: Book) -> None:
        self._books.remove(item)

    def find(
            self,
            isbn: str | None = None,
            author: str | None = None,
            year: int | None = None,
    ) -> BookCollection:
        isbn_books = self._index_isbn[isbn]
        author_books = self._index_author[author]
        year_books = self._index_year[year]

        res = set(isbn_books) & set(author_books) & set(year_books)
        return BookCollection(res)

    def borrow_book(
            self,
            isbn: str | None = None,
            author: str | None = None,
            year: int | None = None,
    ) -> Book | None:
        books = self.find(isbn, author, year)
        books_id = [self._books.index(book) for book in books]
        for id in books_id:
            if not self._books[id].borrowed:
                return self._books[id]()
        return None

    def put_book(
            self,
            isbn: str | None = None,
            author: str | None = None,
            year: int | None = None,
    ) -> Book | None:
        books = self.find(isbn, author, year)
        books_id = [self._books.index(book) for book in books]
        for id in books_id:
            if self._books[id].borrowed:
                return self._books[id]()
        return None

    def switch_book(
            self,
            book: Book,
            new_book: Book,
    ) -> None:
        if (not isinstance(book, Book)) or (not isinstance(new_book, Book)):
            raise TypeError("Book element expected")
        books = self.find(book.isbn, book.author, book.year)
        books_id = [self._books.index(i_book) for i_book in books]
        for id in books_id:
            if book == self._books[id]:
                self._books[id] = new_book
                break
        else:
            raise KeyError("book not found")

    def stat(
            self,
            number: bool = True,
            isbn: bool = True,
            author: bool = True,
            year: bool = True,
    ) -> dict[str, Any]:
        res: dict[str, Any] = dict()
        if number:
            res["number"] = len(self._books)
        if isbn:
            res["isbn"] = {ind for ind in self._index_isbn}
        if author:
            res["author"] = {ind for ind in self._index_author}
        if year:
            res["year"] = {ind for ind in self._index_year}
        return res
