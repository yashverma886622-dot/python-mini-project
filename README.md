Library Inventory Manager – Python CLI
Mini Project (Lab 3)
Student: Yash Verma
Roll No: 2501730159
Course: B.Tech CSE (AI/ML)
Subject: Programming for Problem Solving using Python
1. Project Overview

This is a command-line based Library Inventory Management System built using Python and Object-Oriented Programming (OOP).
The system allows users to:

Add books

Issue books

Return books

Search for books

View complete inventory

Save and load book data using JSON file

Maintain persistent catalog across program runs

This project follows the assignment instructions provided by faculty.


lab 3 assignment mini python

2. Learning Objectives

Understand class-based design (Book class, Inventory class)

Implement OOP principles like encapsulation and methods

Use JSON for file storage

Apply exception handling for safe file I/O

Build a menu-driven CLI system

Write modular Python project with packages

3. Features Implemented
 Task 1: Book Class

Attributes: title, author, isbn, status

Methods: issue(), return_book(), is_available(), __str__(), to_dict()

 Task 2: Inventory Manager

Add book

Issue book

Return book

Search by title

Search by ISBN

Display all books

 Task 3: JSON File Persistence

Loads data from books.json

Saves catalog automatically when books change

Handles missing or corrupted JSON using try-except

 Task 4: Menu-driven CLI

Options include:

Add Book

Issue Book

Return Book

View All Books

Search Book

Exit

 Task 5: Exception Handling + Logging

All file and input operations wrapped in try–except

Reliable and stable execution

 Task 6: Proper Project Packaging

Folder structure:

library-inventory-manager-yash/
│
├── library_manager/
│   ├── __init__.py
│   ├── book.py
│   ├── inventory.py
│
├── cli/
│   ├── __init__.py
│   ├── main.py
│
├── books.json
├── README.md
└── .gitignore

4. How to Run the Program
Step 1: Go to project folder
cd library-inventory-manager-yash

Step 2: Run the CLI
python cli/main.py


or

python3 cli/main.py

5. Sample Run (Example Output)
===== Library Inventory Manager =====
1. Add Book
2. Issue Book
3. Return Book
4. View All Books
5. Search Book
6. Exit

Enter choice: 1
Enter title: Harry Potter
Enter author: J.K. Rowling
Enter ISBN: 12345
Book added successfully.

Enter choice: 4
Harry Potter by J.K. Rowling | ISBN: 12345 | Status: available

6. JSON Catalog Example

books.json will contain:

[
    {
        "title": "Harry Potter",
        "author": "J.K. Rowling",
        "isbn": "12345",
        "status": "available"
    }
]

7. Academic Integrity

This project is implemented individually following academic guidelines.
All code is original as per assignment instructions.