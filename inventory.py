import json
from pathlib import Path
from library_manager.book import Book

class LibraryInventory:
    def __init__(self, storage_path="books.json"):
        self.storage_path = Path(storage_path)
        self.books = []
        self.load_from_file()

    def add_book(self, book: Book):
        self.books.append(book)
        self.save_to_file()

    def search_by_title(self, title):
        return [b for b in self.books if title.lower() in b.title.lower()]

    def search_by_isbn(self, isbn):
        for b in self.books:
            if b.isbn == isbn:
                return b
        return None

    def display_all(self):
        return [str(b) for b in self.books]

    def save_to_file(self):
        with self.storage_path.open("w") as f:
            json.dump([b.to_dict() for b in self.books], f, indent=2)

    def load_from_file(self):
        if not self.storage_path.exists():
            return
        with self.storage_path.open("r") as f:
            try:
                data = json.load(f)
                for item in data:
                    self.books.append(Book(**item))
            except:
                self.books = []
