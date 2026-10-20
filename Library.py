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

# Add a bunch of books to the library collection. Expressed as a list because lists are more flexible than tuples, and it can hold the book object class.
books = []
books.append(Book("The Silver Eyes", "Scott Cawthon & Kira Breed Wrisley", 7))
books.append(Book("Every Day", "David Levithan", 14))
books.append(Book("M is for Monster", "Talia Dutton", 14))
books.append(Book("Kill the Villainess", "Haegi", 27))
author = "Stephen King"
books.append(Book("The Shining", author, 14))
books.append(Book("Pet Sematary", author, 7))
books.append(Book("The Institute", author, 7))

# Add a bunch of user data to simulate pre-existing sign-ups. Expressed as a list for the same reasons as books.
users = []
users.append(User("Kira", 1980, "CatLover2048@example.com"))
users.append(User("Ron", 1967, "GuyWithMoustache@example.com"))
users.append(User("Davidson", 2005, "FFunkinBoy@domain.edu.au"))

def PrintBooks():
    """ Function that prints all the books in the library collection. """
    for book in books:
        print(f"Title: {book.title}, Author: {book.author}, Borrowing Period: {book.period} days")

def PrintUsers():
    """ Function that prints all the users in the library collection. """
    for user in users:
        print(f"Name: {user.name}, Year of Birth: {user.yob}, Contact: {user.contact}")