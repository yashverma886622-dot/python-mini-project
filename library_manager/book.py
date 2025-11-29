from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    isbn: str
    status: str = "available"

    def __str__(self):
        return f"{self.title} | {self.author} | {self.isbn} | {self.status}"

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "status": self.status
        }

    def issue(self):
        if self.status == "available":
            self.status = "issued"
            return True
        return False

    def return_book(self):
        if self.status == "issued":
            self.status = "available"
            return True
        return False
