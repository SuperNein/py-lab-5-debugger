import pytest

from src.services.book_collections import BookCollection, IndexDict


def test_empty_book_collection(book):
    books = BookCollection()

    assert len(books) == 0

    with pytest.raises(IndexError):
        books[-1]
        books.pop()
        del books[-1]
        books.remove(book)


def test__book_collection(book, digital_book, magazine):
    books = BookCollection((book, ))
    assert books[-1] == book

    books.append(magazine)
    assert books[-1] == magazine
    assert len(books) == 2

    assert books.pop() == magazine
    assert len(books) == 1

    assert book in books
    assert magazine not in books

    assert len(books) == len(books.copy())

    books[-1] = digital_book
    assert books[-1] == digital_book

    assert len(books + BookCollection((magazine, ))) == 2


def test_index_dict_errors():
    with pytest.raises(TypeError):
        IndexDict("wrong index")
        IndexDict(books=["book1", "book2", "book3"])

    books = BookCollection()
    dic = IndexDict(books=books)
    with pytest.raises(TypeError):
        dic.append("book")
        dic.remove("book")


def test_index_dict(book, digital_book, magazine):
    books = BookCollection()
    dic = IndexDict(books=books)
    assert len(dic) == 0

    dic.append(book)
    assert len(dic) == 1

    assert book in dic['111']

    dic.remove(book)
    assert len(dic) == 0
