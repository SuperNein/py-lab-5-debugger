class Book:
    def __init__(
            self,
            title: str,
            author: str,
            year: int,
            genre: str,
            isbn: str,
            borrowed: bool = False,
    ):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.isbn = isbn
        self.borrowed = borrowed

    def __call__(self) -> Book:
        self.borrowed = not self.borrowed
        return self

    def __str__(self) -> str:
        return f"<<{self.isbn}: {self.author}, {self.title}, {self.year}: {self.genre}>>"

    def __repr__(self) -> str:
        return (f"{self.__class__.__name__}"
                f"(title={self.title!r}, author={self.author!r}, year={self.year}, "
                f"genre={self.genre!r}, isbn={self.isbn!r}, borrowed={self.borrowed!r})")

    def __eq__(self, other: Book) -> bool:
        return self.__dict__ == other.__dict__

    def __hash__(self):
        return hash((self.isbn, self.title, self.author))


class DigitalBook(Book):
    def __init__(
            self,
            title: str,
            author: str,
            year: int,
            genre: str,
            isbn: str,
    ):
        super().__init__(title, author, year, genre, isbn)
        self.readers: int = 0

    def __call__(self, readers_num: int = 1) -> Book:
        self.readers += readers_num
        return self

    def __repr__(self) -> str:
        return (f"{self.__class__.__name__}"
                f"(title={self.title!r}, author={self.author!r}, year={self.year}, "
                f"genre={self.genre!r}, isbn={self.isbn!r})")


class Magazine(Book):
    def __init__(
            self,
            title: str,
            author: str,
            year: int,
            genre: str,
            isbn: str,
            borrowed: bool = False,
            issue: int = 1,
    ):
        super().__init__(title, author, year, genre, isbn, borrowed)
        self.issue = issue

    def __str__(self) -> str:
        return f"<<{self.isbn}: {self.author}, {self.title}, {self.year}, #{self.issue}: {self.genre}>>"

    def __repr__(self) -> str:
        return (f"{self.__class__.__name__}"
                f"(title={self.title!r}, author={self.author!r}, year={self.year}, "
                f"genre={self.genre!r}, isbn={self.isbn!r}, "
                f"borrowed={self.borrowed!r}, issue={self.issue!r})")
