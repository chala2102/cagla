# -----------------------------------------
# Library System using Composition
# -----------------------------------------

class Book:
    """This class represents one book in the library"""

    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def display_info(self):
        return f"{self.title} by {self.author} | ISBN: {self.isbn}"


class Library:
    """This class represents the library which contains many books"""

    def __init__(self, name):
        self.name = name
        self.books = []   # Library HAS books

    def add_book(self, book):
        self.books.append(book)
        return f"'{book.title}' has been added to the library."

    def remove_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                return f"'{book.title}' has been removed."
        return f"Sorry, '{title}' is not in the library."

    def list_books(self):
        if len(self.books) == 0:
            return "The library is currently empty."

        output = f"\nBooks available in {self.name}:\n"
        output += "-" * 40 + "\n"

        for num, book in enumerate(self.books, start=1):
            output += f"{num}. {book.display_info()}\n"

        return output

    def search_by_title(self, keyword):
        matches = []

        for book in self.books:
            if keyword.lower() in book.title.lower():
                matches.append(book)

        if matches:
            output = f"\nSearch results for '{keyword}':\n"
            for book in matches:
                output += f"- {book.display_info()}\n"
            return output
        else:
            return f"No books found with the title '{keyword}'."



# -----------------------------------------
# Testing the system
# -----------------------------------------

# Create the library
library = Library("City Library")

# Create some books
book1 = Book("Python Crash Course", "Eric Matthes", "978-1593279288")
book2 = Book("Clean Code", "Robert Martin", "978-0132350884")
book3 = Book("The Pragmatic Programmer", "Andrew Hunt & David Thomas", "978-0201616224")

# Add books
print(library.add_book(book1))
print(library.add_book(book2))
print(library.add_book(book3))

# Show all books
print(library.list_books())

# Search for a book
print(library.search_by_title("Python"))

# Remove a book
print(library.remove_book("Clean Code"))

# Show updated list
print(library.list_books())