import pytest

from src.services.library import Library


def test_library(book, digital_book, magazine):
    lib = Library()

    lib.append(book)
    lib.append(digital_book)
    lib.append(magazine)

    assert digital_book in lib

    lib.remove(digital_book)
    assert digital_book not in lib

    assert magazine in lib.find(isbn="333")
    assert book not in lib.find(isbn="333")

    lib.switch_book(book, digital_book)
    assert book not in lib
    assert magazine in lib
