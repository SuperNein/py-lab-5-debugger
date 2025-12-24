from typing import Any
from random import randint, choice

from src.common import constants as cst
from src.enums.book_types import BookTypes
from src.services.book import Book
from src.services import book


book_types = {
    BookTypes.book: book.Book,
    BookTypes.digital_book: book.DigitalBook,
    BookTypes.magazine: book.Magazine,
}

def generate_random_book_kwargs() -> dict[str, Any]:
    def generate_isbn() -> str:
        prefix = randint(cst.ISBN_PREFIX[0], cst.ISBN_PREFIX[1])
        country = randint(cst.ISBN_COUNTRY[0], cst.ISBN_COUNTRY[1])
        publishing = randint(cst.ISBN_PUBLISHING[0], cst.ISBN_PUBLISHING[1])
        control = randint(cst.ISBN_CONTROL[0], cst.ISBN_CONTROL[1])
        return f"{prefix}{country}{publishing}{control}"

    return {
        "title": choice(cst.BOOK_TITLES),
        "author": choice(cst.AUTHOR_NAMES),
        "year": randint(cst.YEAR_RANGE[0], cst.YEAR_RANGE[1]),
        "genre": choice(cst.BOOK_GENRES),
        "isbn": generate_isbn(),
    }

def generate_random_book() -> Book:
    book_type = choice([book_type for book_type in BookTypes])
    kwargs = generate_random_book_kwargs()
    if book_type == BookTypes.magazine:
        kwargs["issue"] = randint(cst.MAGAZINE_ISSUE[0], cst.MAGAZINE_ISSUE[1])
    return book_types[book_type](**kwargs)
