class Library:
    def __init__(self):
        self.books = []
        self.no_of_books = 0
    
    def addBook(self, book):
        self.books.append(book)
        self.no_of_books = len(self.books)
        print(f"book {book} was added successfully.")
    
    def showBooks(self):
        print(f"The library has {self.no_of_books} books. The books are: ")
        if self.books:
            for i, book in enumerate(self.books):
                print(f"book no.{i+1}: {book}")
        else:
            print(f"No books available.")

l = Library()

l.addBook("book1")
l.addBook("book2")
l.addBook("book3")
l.addBook("book4")

l.showBooks()

    
    
