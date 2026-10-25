books = {}                                     # Create a dictionary to store the books in the library. Key = ISBN of book, and value = Book object. This allows faster lookup using the dictionary key rather than searching through a list of books.
users = []                                     # Create a list to store the users in the library. Each user is an object of the User class. This allows us to store multiple users and their borrowed books.
date = "2026-10-22"                            # This is a placeholder for the current date. In a real program, you would use the datetime module to get the current date.
minTitleLength = 20                            # This is the minimum length of the title string. It is used to format the output of the PrintLibraryBooks() function. If the title is shorter than this length, it will be padded with spaces to align the output.
minAuthorLength = 35                           # This is the minimum length of the author string. It serves the same purpose as minTitleLength, but for the author string.

def DaysInMonth(month, year=None):
    """ Returns an integer value of the days inside the given month. """
    if month == 1: return 31                       # January has 31 days.
    elif month == 2: return 28 if year is None else 29 if IsLeapYear(year) else 28  # February has 28 days unless it's a leap year. If no year is given, assume a common year.
    elif month % 2 == 1 and month < 8: return 31   # There is a hill pattern from March-July, so assign 31 to odd numbers. Any number % 2 will either give a remainder of 0 or 1 (so odd or even).
    elif month % 2 == 0 and month < 8: return 30   # Then assign 30 to even numbers.
    elif month % 2 == 0 and month >= 8: return 31  # The hill pattern flips on august. August is an even number, so assign 31 to even numbers past August.
    else: return 30                                # Finally, assign 30 to odd numbers past August.

def IsLeapYear(year):
    """ Returns True if the given year is a leap year, and False if it is a common year. """
    if (year % 4 != 0): return False               # If the year number isn't divisible by four, it's a common year.
    elif (year % 100 != 0): return True            # If the year number isn't divisible by 100, it's a leap year.
    elif (year % 400 != 0): return False           # If the year number isn't divisible by 400, it's a common year.
    else: return True                              # Otherwise, it's a leap year.

def CalculateDueDate(borrowDate, period):
    """ Calculate the due date of a borrowed book and return a string in the format YYYY-MM-DD 
        borrowDate: String in the format YYYY-MM-DD
        period: Integer value of the borrowing period in days. """
    year, month, day = map(int, borrowDate.split("-"))  # Split the borrow date into year, month, and day. Convert them to integers.
    day += period                                       # Add the borrowing period to the day.
    while day > DaysInMonth(month, year):               # While the day is greater than the number of days in the month, subtract the number of days in the month from the day and increment the month. If the month is greater than 12, increment the year and set the month to 1.
        day -= DaysInMonth(month, year)
        month += 1
        if month > 12:
            month = 1
            year += 1
    return f"{year}-{month:02d}-{day:02d}"             # Return the due date in the format YYYY-MM-DD. The :02d formats the month and day to be two digits with leading zeros if necessary.

class Book:
    # Self initialisation learned through W3schools: https://www.w3schools.com/python/python_class_init.asp
    def __init__(self, isbn,title, author, period):
        self.isbn = isbn                     # ISBN of book. This is a unique identifier for each book.
        self.title = title                   # Title of book
        self.author = author                 # Author of book. Can have multiple authors in the string.
        self.period = period                 # Borrowing period for the book.

class User:
    def __init__(self, name, yob, contact):
            self.name = name                 # User's name.
            self.yob = yob                   # User's year of birth.
            self.contact = contact           # Contact can either be phone or email. First check if .isdigit(), if not it must be an email, then check if email is in valid format.
            self.brrwd = {}
    def BorrowBook(self, isbn):
        """ Allows a user to borrow a book. """
        try: self.brrwd[isbn] = CalculateDueDate(date, books[isbn].period)             # Calculate the due date of the book and store it in the user's borrowed books dictionary. Key = ISBN, and value = due date. Rather than storing the value as a period, where the library would have to calculate the due date each time, we can store the due date directly. This is more efficient, as the library can simply check if the due date has passed or not.
        except KeyError: print(f"Book with ISBN {isbn} not found.")
    def ReturnBook(self, isbn):
        """ Allows a user to return a book. """
        try: del self.brrwd[isbn]                 # Check if the book is in the user's borrowed books dictionary. If so, Remove the book from the user's borrowed books dictionary.
        except KeyError: print(f"You have not borrowed this book.")            # If the book is not in the user's borrowed books dictionary, print an error message.
    def PrintBorrowedBooks(self):
        """ Prints all the books a user has borrowed. It prints the due date rather than the days left, as the due date is more useful to the user. """
        for isbn in self.brrwd:                                     # For each key in the user's borrowed books (For each ISBN int)
            print(f"ISBN: {isbn}, Title: {books[isbn].title},{' ' * (minTitleLength - len(books[isbn].title))}" +   # Print the key (ISBN), the title of the book, the author of the book, and the due date. The due date is calculated with the current date and the borrowing period from the brrwd dictionary value
                  f"Author: {books[isbn].author},{' ' * (minAuthorLength - len(books[isbn].author))}" + 
                  f"Due Date: {self.brrwd[isbn]}")

# Add a bunch of book data to simulate pre-existing books in the library. They Key is the ISBN.
books[0] = Book(0, "The Silver Eyes", "Scott Cawthon & Kira Breed Wrisley", 7)
books[1] = Book(1, "Every Day", "David Levithan", 14)
books[2] = Book(2, "M is for Monster", "Talia Dutton", 14)
books[3] = Book(3, "Kill the Villainess", "Haegi", 27)
author = "Stephen King"
books[4] = Book(4, "The Shining", author, 14)
books[5] = Book(5, "Pet Sematary", author, 7)
books[6] = Book(6, "The Institute", author, 7)

# Add a bunch of user data to simulate pre-existing users in the library.
users.append(User("Kira", 1980, "CatLover2048@example.com"))
users.append(User("Ron", 1967, "GuyWithMoustache@example.com"))
users.append(User("Davidson", 2005, "FFunkinBoy@domain.edu.au"))

def PrintLibraryBooks():
    """ Function that prints all the books in the library collection. """
    for book in books:
        print(f"ISBN: {book}, Title: {books[book].title},{' ' * (minTitleLength - len(books[book].title))}" +   # The same as PrintBorrowedBooks(), but instead of the due date, it prints the borrowing period. This is more useful for library staff to calculate the due date for each user. It also shows users how long they can borrow a book.
              f"Author: {books[book].author},{' ' * (minAuthorLength - len(books[book].author))} Borrowing Period: {books[book].period} days")

def PrintUsers():
    """ Function that prints all the users in the library collection. """
    for user in users: print(f"Name: {user.name}, Year of Birth: {user.yob}, Contact: {user.contact}")          # Prints all the users in the library collection. It prints the user's name, year of birth, and contact information.


# Concepts we might add later...
# \ escapes the newline character, so the string continues on the next line. Learned through CISCO Module 4.5.1