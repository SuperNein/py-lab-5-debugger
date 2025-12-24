from enum import Enum


class Index(str, Enum):
    isbn = "isbn"
    author = "author"
    year = "year"
