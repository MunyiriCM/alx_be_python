from library_system import Book, EBook, PrintBook, Library

def main():
    # Create library
    my_library = Library()

    # Create books
    book1 = Book("To Kill a Mockingbird", "Harper Lee")
    ebook1 = EBook("Digital Fortress", "Dan Brown", 5)
    printbook1 = PrintBook("The Hobbit", "J.R.R. Tolkien", 310)

    # Add books to the library
    my_library.add_book(book1)
    my_library.add_book(ebook1)
    my_library.add_book(printbook1)

    # List books in the library
    print("\nBooks in the library:")
    my_library.list_books()

if __name__ == "__main__":
    main()
