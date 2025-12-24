import logging
import random
from typing import Callable, Any

from src.services.book import Book
from src.services.library import Library
from src.services.generators import generate_random_book


class Simulation:
    def __init__(self, logger, seed: int | None = None):
        self._logger = logger
        if seed is not None:
            random.seed(seed)
        self._logger.info(f"Initializing simulation with seed: {seed}")

        self._library = Library()
        self.__actions: list[tuple[Callable, dict[str, Any]]] = [
            (self.add_book, {}),
            (self.find_book, {}),
            (self.switch_book, {}),
            (self.remove_book, {}),
            (self.remove_random_book, {}),
        ]

    def _choose_random_book(self) -> Book:
        return random.choice(tuple(book for book in self._library))

    def _choose_random_action(self) -> tuple[Callable, dict[str, Any]]:
        return random.choice(self.__actions)

    def _push_random_books(self, num: int) -> None:
        for _ in range(num):
            book = generate_random_book()
            self._library.append(book)

    def add_book(self, book: Book | None = None) -> str:
        if book is None:
            book = generate_random_book()
        self._library.append(book)
        return f"Added {book}"

    def remove_book(self, book: Book | None = None) -> str:
        if book is None:
            book = self._choose_random_book()
        if book not in self._library:
            raise ValueError(f"Trying to remove nonexistent {book}")
        self._library.remove(book)
        return f"Removed {book}"

    def remove_random_book(self, book: Book | None = None) -> str:
        if book is None:
            book = generate_random_book()
        try:
            data = self.remove_book(book)
        except ValueError as e:
            return f"Failed to remove random {book}"
        return data

    def find_book(
            self,
            book: Book | None = None,
            isbn: bool = True,
            author: bool = False,
            year: bool = False,
    ) -> str:
        if book is None:
            book = self._choose_random_book()
        book_index = [
            book.isbn if isbn else None,
            book.author if author else None,
            book.year if year else None,
        ]
        self._library.find(*book_index)
        return f"Found {book}"

    def switch_book(
            self,
            old_book: Book | None = None,
            new_book: Book | None = None,
    ) -> str:
        if old_book is None:
            old_book = self._choose_random_book()
        if new_book is None:
            new_book = generate_random_book()
        if (not isinstance(old_book, Book)) or (not isinstance(new_book, Book)):
            raise TypeError("Book element expected")
        self._library.switch_book(old_book, new_book)
        return f"Switched {old_book} to {new_book}"

    def run(self, steps: int) -> None:
        self._logger.info(f"Run simulation with {steps} steps.")
        self._push_random_books(steps)

        step = 0
        act: Callable[[Any], str]
        kwargs: dict[str, Any]

        while step < steps:
            act, kwargs = self._choose_random_action()
            try:
                data: str = act(**kwargs)
            except Exception as e:
                self._logger.error(f"Step {step+1:<3} | {act}: {kwargs} | {e}")
                continue

            step += 1
            self._logger.info(f"Step {step:<3} | {act}: {kwargs} | {data}")
            print(f"Step {step:<3} | {data}")
