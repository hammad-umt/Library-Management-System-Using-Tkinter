# === Book class ===
class Book:
    """
    Yeh class physical book ko represent karti hai.
    """

    def __init__(self, title, author, ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.ISBN}"

# === Ebook class ===
class Ebook(Book):
    """
    Yeh class Ebook ko represent karti hai, jo ke Book se inherit karti hai.
    """

    def __init__(self, title, author, ISBN, booksize):
        super().__init__(title, author, ISBN)
        self.booksize = booksize

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.ISBN}, Size: {self.booksize}"

# === Custom Exception ===
class BookNotAvailableError(Exception):
    """
    Custom exception agar book available na ho.
    """
    pass

# === Library class ===
class Library:
    """
    Yeh class basic library functionality handle karti hai (books add, remove, lend, return waghera).
    """
    
    def __init__(self):
        self.books = []          # available books
        self.lent_books = []     # lent books
        self.index = 0           # Iterator ka index initialize karna

    def __iter__(self):
        """Iterator initialize karta hai."""
        self.index = 0  # Iterator ka index 0 pe reset karte hain
        return self

    def __next__(self):
        """Next book return karta hai."""
        if self.index < len(self.books):  # Agar books list mein koi aur book bachi ho
            book = self.books[self.index]
            self.index += 1  # Index ko update karte hain agle book ke liye
            return book
        else:
            raise StopIteration  # Jab sab books iterate ho jayein, iteration ko rokna

    def addBook(self, book):
        """
        Library mein new book add karta hai.
        """
        for b in self.books:
            if b.ISBN == book.ISBN:
                print(f"Book '{book.title}' already exists in the library.")
                return
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")
    
    def removeBook(self, book):
        """
        Library se book remove karta hai agar mojood ho.
        """
        if book in self.books:
            self.books.remove(book)
            print(f"Book '{book.title}' removed from the library.")
        else:
            print(f"Book '{book.title}' not found in the library.")
    
    def lendBook(self, book):
        """
        Book ko lend (udhaar) karta hai.
        """
        if book in self.books:
            self.books.remove(book)
            self.lent_books.append(book)
            print(f"Book '{book.title}' lent out.")
        else:
            raise BookNotAvailableError("Book not available for lending.")
    
    def returnBook(self, book):
        """
        Book ko wapas return karta hai.
        """
        if book in self.lent_books:
            self.lent_books.remove(book)
            self.books.append(book)
            print(f"Book '{book.title}' returned to the library.")
        else:
            print(f"Book '{book.title}' not found in lent books.")
    def displayBooks(self):
        """
        Library mein available books show karta hai using custom iterator.
        """
        if self.books:
            print("Books available in the library:")
            for book in self:  # Custom iterator ka use karke har book ko print karte hain
                 print(book)
            return self.books     
        else:
            print("No books available in the library.")
        return [] 
    
    def displayLentBooks(self):
        """
        Wo books show karta hai jo abhi udhaar di gayi hain.
        """
        if self.lent_books:
            print("Books currently lent out:")
            for book in self.lent_books:
                print(book)
                return self.lent_books
        else:
            print("No books currently lent out.")
    
    def displayBookbyAuthor(self, author):
        """
        Specific author ki books ko search karta hai.
        """
        for book in self.books:
            if book.author == author:
                yield book

# === DigitalLibrary class ===
class DigitalLibrary(Library):
    """
    DigitalLibrary class ebooks ko manage karti hai, aur Library class se inherit karti hai.
    """
    
    def __init__(self):
        super().__init__()
        self.ebooks = []
    
    def addEbook(self, ebook):
        """
        Nayi ebook add karta hai.
        """
        for e in self.ebooks:
            if e.ISBN == ebook.ISBN:
                print(f"Ebook '{ebook.title}' already exists.")
                return
        self.ebooks.append(ebook)
        print(f"Ebook '{ebook.title}' added to the digital library.")
    
    def removeEbook(self, ebook):
        """
        Ebooks se book remove karta hai agar mojood ho.
        """
        if ebook in self.ebooks:
            self.ebooks.remove(ebook)
            print(f"Ebook '{ebook.title}' removed from the digital library.")
        else:
            print(f"Ebook '{ebook.title}' not found in the digital library.")
    
    def lendEbook(self, ebook):
        """
        Ebook ko lend karta hai (digital lending).
        """
        if ebook in self.ebooks:
            self.ebooks.remove(ebook)
            self.lent_books.append(ebook)
            print(f"Ebook '{ebook.title}' lent out.")
        else:
            raise BookNotAvailableError("Ebook not available for lending.")
    
    def returnEbook(self, ebook):
        """
        Ebook ko return karta hai agar wo lent mein hai.
        """
        if ebook in self.lent_books:
            self.lent_books.remove(ebook)
            self.ebooks.append(ebook)
            print(f"Ebook '{ebook.title}' returned to the digital library.")
        else:
            print(f"Ebook '{ebook.title}' not found in lent ebooks.")
    
    def displayEbooks(self):
        """
        Sab available ebooks show karta hai.
        """
        if self.ebooks:
            print("Ebooks available in the digital library:")
            for ebook in self.ebooks:
                print(ebook)
                return self.ebooks
        else:
            print("No ebooks available in the digital library.")
            return []
    
    def displayLentEbooks(self):
        """
        Wo ebooks show karta hai jo abhi udhaar di gayi hain.
        """
        if self.lent_books:
            print("Ebooks currently lent out:")
            for ebook in self.lent_books:
                print(ebook)
                return self.lent_books
        else:
            print("No ebooks currently lent out.")
    
    def displayEbookbyAuthor(self, author):
        """
        Author ke mutabiq ebooks search karta hai.
        """
        for ebook in self.ebooks:
            if ebook.author == author:
                yield ebook

# === Main Menu Function ===
digital_library = DigitalLibrary()

digital_library.addBook(Book("Raja Gidh", "Bano Qudsia", "9789693502012"))
digital_library.addBook(Book("Peer-e-Kamil", "Umera Ahmed", "9789690014563"))
digital_library.addBook(Book("Aangan", "Khadija Mastoor", "9789692104378"))
digital_library.addBook(Book("Zavia", "Ashfaq Ahmed", "9789693501961"))
digital_library.addBook(Book("Udas Naslain", "Abdullah Hussain", "9789690017007"))
digital_library.addEbook(Ebook("Shehr-e-Zaat", "Umera Ahmed", "9789690023329", "PDF"))
digital_library.addEbook(Ebook("Mushaf", "Umera Ahmed", "9789692109878", "EPUB"))
digital_library.addEbook(Ebook("Amarbail", "Umera Ahmed", "9789690017325", "MOBI"))
digital_library.addEbook(Ebook("Hasil", "Umera Ahmed", "9789693502981", "PDF"))
digital_library.addEbook(Ebook("Mirat-ul-Uroos", "Deputy Nazir Ahmad", "9789692109876", "EPUB"))


def main():
    """
    Yeh function user ko menu provide karta hai jahan se wo library aur ebooks ke actions perform kar sakta hai.
    """
    digital_library = DigitalLibrary()
    while True:
        print("\n========== Library Management Menu ==========")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Lend Book")
        print("4. Return Book")
        print("5. Show All Available Books")
        print("6. Show All Lent Books")
        print("7. Search Books by Author")
        print("8. Add Ebook")
        print("9. Remove Ebook")
        print("10. Lend Ebook")
        print("11. Return Ebook")
        print("12. Show All Available Ebooks")
        print("13. Show All Lent Ebooks")
        print("14. Search Ebooks by Author")
        print("0. Exit")
        print("=============================================")
        choice = input("Enter your choice (0-14): ")
        # Har option ke liye user se input le kar action perform karte hain
        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            isbn = input("Enter ISBN: ")
            book = Book(title, author, isbn)
            digital_library.addBook(book)
        elif choice == '2':
            isbn = input("Enter ISBN to remove: ")
            for b in digital_library.books:
                if b.ISBN == isbn:
                    digital_library.removeBook(b)
                    break
            else:
                print("Book not found.")
        elif choice == '3':
            isbn = input("Enter ISBN to lend: ")
            for b in digital_library.books:
                if b.ISBN == isbn:
                    try:
                        digital_library.lendBook(b)
                    except BookNotAvailableError as e:
                        print(e)
                    break
            else:
                print("Book not found.")
        elif choice == '4':
            isbn = input("Enter ISBN to return: ")
            for b in digital_library.lent_books:
                if b.ISBN == isbn:
                    digital_library.returnBook(b)
                    break
            else:
                print("Book not found in lent books.")
        elif choice == '5':
            digital_library.displayBooks()

        elif choice == '6':
            digital_library.displayLentBooks()
        elif choice == '7':
            author = input("Enter author name: ")
            found = False
            for book in digital_library.displayBookbyAuthor(author):
                print(book)
                found = True
            if not found:
                print("No books by that author.")
        elif choice == '8':
            title = input("Enter ebook title: ")
            author = input("Enter author name: ")
            isbn = input("Enter ISBN: ")
            size = input("Enter size (e.g., 5MB): ")
            ebook = Ebook(title, author, isbn, size)
            digital_library.addEbook(ebook)
        elif choice == '9':
            isbn = input("Enter ISBN to remove: ")
            for e in digital_library.ebooks:
                if e.ISBN == isbn:
                    digital_library.removeEbook(e)
                    break
            else:
                print("Ebook not found.")
        elif choice == '10':
            isbn = input("Enter ISBN to lend: ")
            for e in digital_library.ebooks:
                if e.ISBN == isbn:
                    try:
                        digital_library.lendEbook(e)
                    except BookNotAvailableError as e:
                        print(e)
                    break
            else:
                print("Ebook not found.")
        elif choice == '11':
            isbn = input("Enter ISBN to return: ")
            for e in digital_library.lent_books:
                if e.ISBN == isbn:
                    digital_library.returnEbook(e)
                    break
            else:
                print("Ebook not found in lent list.")

        elif choice == '12':
            digital_library.displayEbooks()

        elif choice == '13':
            digital_library.displayLentEbooks()

        elif choice == '14':
            author = input("Enter author name: ")
            found = False
            for ebook in digital_library.displayEbookbyAuthor(author):
                print(ebook)
                found = True
            if not found:
                print("No ebooks by that author.")

        elif choice == '0':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")





# === Run the program ===
if __name__ == "__main__":
    main()
