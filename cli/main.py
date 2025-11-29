# allow running main.py directly by adding project root to sys.path
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))

from library_manager.inventory import LibraryInventory
from library_manager.book import Book

def menu():
    inv = LibraryInventory()

    while True:
        print("\n1. Add Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. Search Book")
        print("5. View All Books")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            t = input("Title: ")
            a = input("Author: ")
            i = input("ISBN: ")
            inv.add_book(Book(t, a, i))
            print("Book Added")

        elif choice == "2":
            i = input("Enter ISBN: ")
            b = inv.search_by_isbn(i)
            if b and b.issue():
                inv.save_to_file()
                print("Issued")
            else:
                print("Not Available")

        elif choice == "3":
            i = input("Enter ISBN: ")
            b = inv.search_by_isbn(i)
            if b and b.return_book():
                inv.save_to_file()
                print("Returned")
            else:
                print("Not Issued")

        elif choice == "4":
            t = input("Enter title or ISBN: ")
            b = inv.search_by_isbn(t)
            if b:
                print(b)
            else:
                res = inv.search_by_title(t)
                for x in res:
                    print(x)

        elif choice == "5":
            for book in inv.display_all():
                print(book)

        elif choice == "6":
            break

        else:
            print("Invalid choice")

menu()
