from tkinter import *
from tkinter import messagebox
from library_logic import Book, Ebook, DigitalLibrary, Library

Gui = Tk()
Gui.title("Library Management System")
Gui.geometry("750x600")
Gui.config(bg="#f0f0f0")  # Light background color for the whole window

# Create library objects
library = Library()
dlibrary = DigitalLibrary()

# String Variables
b_name = StringVar()
a_name = StringVar()
isbn = StringVar()
book_size = StringVar()
book_format = StringVar()

# Header Frame
title_frame = Frame(Gui, bg="#007ACC", height=60)
title_frame.pack(side=TOP, fill=X)
title_label = Label(title_frame, text="Welcome to the Library Management System", font=("Arial", 18), bg="#007ACC", fg="white")
title_label.pack(side=TOP, pady=10)

# Main Frame for Book Information
add_frame = Frame(Gui, bg='#f0f0f0', height=500)
add_frame.pack(pady=20, padx=30)

# Labels and Entries for Book Information
book_label = Label(add_frame, text="Enter Book Title:", font=("Arial", 12), bg='#f0f0f0')
book_label.grid(row=1, column=0, padx=20, pady=10, sticky=W)
book_entry = Entry(add_frame, width=40, font=("Arial", 12), textvariable=b_name)
book_entry.grid(row=1, column=1, padx=10, pady=10)

author_label = Label(add_frame, text="Enter Author Name:", font=("Arial", 12), bg='#f0f0f0')
author_label.grid(row=2, column=0, padx=20, pady=10, sticky=W)
author_entry = Entry(add_frame, width=40, font=("Arial", 12), textvariable=a_name)
author_entry.grid(row=2, column=1, padx=10, pady=10)

isbn_label = Label(add_frame, text="Enter ISBN:", font=("Arial", 12), bg='#f0f0f0')
isbn_label.grid(row=3, column=0, padx=20, pady=10, sticky=W)
isbn_entry = Entry(add_frame, font=("Arial", 12), textvariable=isbn)
isbn_entry.grid(row=3, column=1, padx=10, pady=10)

# eBook Options (Checkbox and Fields for eBook specific info)
ebook_checkbox_var = IntVar()
ebook_checkbox = Checkbutton(add_frame, text="Is this an eBook?", variable=ebook_checkbox_var, font=("Arial", 12), bg='#f0f0f0', command=lambda: ebook_gui())
ebook_checkbox.grid(row=4, columnspan=2, padx=20, pady=10)

def ebook_gui():
    if ebook_checkbox_var.get() == 1:
        format_entry.config(state=NORMAL)  # Enable format field
        book_size_entry.config(state=NORMAL)  # Enable book size field
    else:
        format_entry.config(state=DISABLED)  # Disable format field
        book_size_entry.config(state=DISABLED)  # Disable book size field

# Labels for eBook format and size (Initially disabled)
format_label = Label(add_frame, text="Enter Format (PDF, EPUB, MOBI):", font=("Arial", 12), bg='#f0f0f0')
format_label.grid(row=5, column=0, padx=20, pady=10, sticky=W)
format_entry = Entry(add_frame, width=40, font=("Arial", 12), state=DISABLED, textvariable=book_format)
format_entry.grid(row=5, column=1, padx=10, pady=10)

book_size_label = Label(add_frame, text="Enter Book Size (in MB):", font=("Arial", 12), bg='#f0f0f0')
book_size_label.grid(row=6, column=0, padx=20, pady=10, sticky=W)
book_size_entry = Entry(add_frame, width=40, font=("Arial", 12), state=DISABLED, textvariable=book_size)
book_size_entry.grid(row=6, column=1, padx=10, pady=10)

# Functions for the actions
def add_book():
    if ebook_checkbox_var.get() == 1:
        dlibrary.addEbook(Ebook(b_name.get(), a_name.get(), isbn.get(), book_size.get()))
        messagebox.showinfo("Success", "Ebook added successfully!")
    else:
        library.addBook(Book(b_name.get(), a_name.get(), isbn.get()))
        messagebox.showinfo("Success", "Book added successfully!")

def remove_book():
    if ebook_checkbox_var.get() == 1:
        for e in dlibrary.ebooks:
            if e.ISBN == isbn.get():
                dlibrary.removeEbook(e)
                messagebox.showinfo("Success", "Ebook removed successfully!")
                break
    else:
        for b in library.books:
            if b.ISBN == isbn.get():
                library.removeBook(b)
                messagebox.showinfo("Success", "Book removed successfully!")
                break

def lend_book():
    if ebook_checkbox_var.get() == 1:
        for e in dlibrary.ebooks:
            if e.ISBN == isbn.get():
                try:
                    dlibrary.lendEbook(e)
                    messagebox.showinfo("Success", "Ebook lent successfully!")
                except Exception as e:
                    messagebox.showerror("Error", str(e))
                break
    else:
        for b in library.books:
            if b.ISBN == isbn.get():
                try:
                    library.lendBook(b)
                    messagebox.showinfo("Success", "Book lent successfully!")
                except Exception as e:
                    messagebox.showerror("Error", str(e))
                break

def return_book():
    if ebook_checkbox_var.get() == 1:
        for e in dlibrary.lent_books:
            if e.ISBN == isbn.get():
                dlibrary.returnEbook(e)
                messagebox.showinfo("Success", "Ebook returned successfully!")
                break
    else:
        for b in library.lent_books:
            if b.ISBN == isbn.get():
                library.returnBook(b)
                messagebox.showinfo("Success", "Book returned successfully!")
                break

def show_all_books():
    books = library.displayBooks() or []
    ebooks = dlibrary.displayEbooks() or []
    if not books and not ebooks:
        messagebox.showinfo("Available Books", "No books available.")
        return

    all_books = "Available Physical Books:\n"
    for book in books:
        all_books += f"{str(book)}\n"

    all_books += "\nAvailable Ebooks:\n"
    for ebook in ebooks:
        all_books += f"{str(ebook)}\n"

    messagebox.showinfo("Library Books", all_books)

def show_lent_books():
    lent_books = library.displayLentBooks() or []
    lent_ebooks = dlibrary.displayLentEbooks() or []
    if not lent_books and not lent_ebooks:
        messagebox.showinfo("Lent Books", "No books are currently lent out.")
        return

    all_lent_books = "Lent Physical Books:\n"
    for book in lent_books:
        all_lent_books += f"{str(book)}\n"

    all_lent_books += "\nLent Ebooks:\n"
    for ebook in lent_ebooks:
        all_lent_books += f"{str(ebook)}\n"

    messagebox.showinfo("Lent Books", all_lent_books)

def search_books_by_author():
    for book in library.displayBookbyAuthor(a_name.get()):
        messagebox.showinfo("Books by Author", str(book))
    for ebook in dlibrary.displayEbookbyAuthor(a_name.get()):
        messagebox.showinfo("Ebooks by Author", str(ebook))

def exit_program():
    Gui.quit()






# Button Frame
button_frame = Frame(Gui, bg="#f0f0f0")
button_frame.pack(pady=30)


buttons = [
    ("1. Add Book", add_book),
    ("2. Remove Book", remove_book),
    ("3. Lend Book", lend_book),
    ("4. Return Book", return_book),
    ("5. Show All Available Books", show_all_books),
    ("6. Show All Lent Books", show_lent_books),
    ("7. Search Books by Author", search_books_by_author),
    ("0. Exit", exit_program)
]

# Display buttons in a grid (4 rows, 2 columns)
for index, (text, command) in enumerate(buttons):
    row = index // 2
    col = index % 2
    Button(button_frame, text=text, width=30, font=("Arial", 12), bg="#007ACC", fg="white", command=command).grid(row=row, column=col, padx=10, pady=10)


# Add sample books
library.addBook(Book("Raja Gidh", "Bano Qudsia", "9789693502012"))
library.addBook(Book("Peer-e-Kamil", "Umera Ahmed", "9789690014563"))
library.addBook(Book("Aangan", "Khadija Mastoor", "9789692104378"))
library.addBook(Book("Zavia", "Ashfaq Ahmed", "9789693501961"))
library.addBook(Book("Udas Naslain", "Abdullah Hussain", "9789690017007"))
dlibrary.addEbook(Ebook("Shehr-e-Zaat", "Umera Ahmed", "9789690023329", "PDF"))
dlibrary.addEbook(Ebook("Mushaf", "Umera Ahmed", "9789692109878", "EPUB"))
dlibrary.addEbook(Ebook("Amarbail", "Umera Ahmed", "9789690017325", "MOBI"))
dlibrary.addEbook(Ebook("Hasil", "Umera Ahmed", "9789693502981", "PDF"))
dlibrary.addEbook(Ebook("Mirat-ul-Uroos", "Deputy Nazir Ahmad", "9789692109876", "EPUB"))

# Run the main loop
Gui.mainloop()
