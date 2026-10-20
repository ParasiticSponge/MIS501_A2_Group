class Book:
    # https://www.w3schools.com/python/python_class_init.asp
    def __init__(self, title, author, period):
        self.title = title                   # Title of book
        self.author = author                 # Author of book. Can have multiple authors in the string.
        self.period = period                 # Borrowing period for the book.

class User:
    def __init__(self, name, yob, contact):
            self.name = name                 # User's name.
            self.yob = yob                   # User's year of birth.
            self.contact = contact           # Contact can either be phone or email. First check if .isdigit(), if not it must be an email, then check if email is in valid format.

# Add a bunch of books to the library collection. Expressed as a tuple because tuples are faster to work with, it can hold the book object class, and book data is unlikely to change.
books = ()
books.Add(Book("The Silver Eyes", "Scott Cawthon & Kira Breed Wrisley", 7))
books.Add(Book("Every Day", "David Levithan", 14))
books.Add(Book("M is for Monster", "Talia Dutton", 14))
books.Add(Book("Kill the Villainess", "Haegi", 27))
author = "Stephen King"
books.Add(Book("The Shining", author, 14))
books.Add(Book("Pet Sematary", author, 7))
books.Add(Book("The Institute", author, 7))

# Add a bunch of user data to simulate pre-existing sign-ups. Expressed as a tuple for the same reasons as books.
users = ()
users.Add(Book("Kira", 1980, "CatLover2048@example.com"))
users.Add(Book("Ron", 1967, "GuyWithMoustache@example.com"))
users.Add(Book("Davidson", 2005, "FFunkinBoy@domain.edu.au"))