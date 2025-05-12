# 📚 Library Management System (GUI using Tkinter)

This is a Python-based desktop application that provides a user-friendly interface for managing both physical books and ebooks. It is built using **Tkinter** for the GUI and follows a modular design where the core logic is separated into the `library_logic` module.

## 🧰 Features
- Add physical books or ebooks to the library
- Remove books by ISBN
- Lend and return books
- Search books by author
- View available and lent books
- Separate handling of ebooks and physical books
- User-friendly Tkinter interface

## 🖼️ GUI Overview
- Clean layout with labeled input fields
- Optional fields for eBooks (Format and Size)
- Interactive buttons for each feature
- Message boxes to show success/failure and book listings

## 📦 Requirements
- Python 3.x
- Tkinter (comes pre-installed with Python)
- A custom module `library_logic.py` (must be in the same directory)

## 📁 File Structure
LibraryManagementSystem/
├── app_gui.py # GUI code
├── library_logic.py # Contains classes: Book, Ebook, Library, DigitalLibrary
└── README.md # This file

## 🚀 How to Run
1. Make sure you have Python installed.
2. Ensure `library_logic.py` is present in the same folder.
3. Run the application:
   ```bash
   python app_gui.py

