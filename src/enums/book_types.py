from enum import Enum


class BookTypes(str, Enum):
    book = "book"
    digital_book = "digital_book"
    magazine = "magazine"
