# -*- coding: utf-8 -*-
"""
This program tracks library books that users borrow.
    Authors: 
        Christopher Moyle - 
        Peter Poli - 
        Samantha Stevens - A00054394
"""
import os

books = {}                                     # Create a dictionary to store the books in the library. Key = ISBN of book, and value = Book object. This allows faster lookup using the dictionary key rather than searching through a list of books.
users = []                                     # Create a list to store the users in the library. Each user is an object of the User class. This allows us to store multiple users and their borrowed books.
date = "2026-10-22"                            # This is a placeholder for the current date. In a real program, you would use the datetime module to get the current date.
minTitleLength = 20                            # This is the minimum length of the title string. It is used to format the output of the print_library_catalogue() function. If the title is shorter than this length, it will be padded with spaces to align the output.
minAuthorLength = 35                           # This is the minimum length of the author string. It serves the same purpose as minTitleLength, but for the author string.

# Functions

'''
clear_screen()
Clears the user console screen using the appropriate OS system clear screen commands
nt identifies Windows OS - uses cls
anything else identifies Mac or Linux - uses clear

Arguments :
N/A

Returns
N/A
'''
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')    # call correct OS clear screen function using os.system to identify OS - nt for windows, otherwise OS is Mac or Linux
    return


def days_in_month(month, year=None):
    """ Returns an integer value of the number days in the given month. """
    """
    int days_in_month(month,year)
    Returns an integer value of the number of days in the month passed as an int and year passed as an int - if year is not passed then leap year not taken into account
    Arguments :
        month : int
        year  : int - year passed so month == 2 will return 29 for leap years and 28 for other years
              : None - year not passed so month == 2 will return 28

    Returns   : int value of the number of days in month
    """
    days_in_months = [31,28,31,30,31,30,31,31,30,31,30,31]
    days = days_in_months[month-1]
    if year!=None and (is_leap_year(year) and month==2) : days+=1
    return days

def is_leap_year(year):
    """
    bool is_leap_year(year)
    Returns a boolean value, either True for leap year or False for normal year
    Arguments -
        year  - int value representing the year
    Returns   - True for leap year False for normal year
    """
    return year % 4 == 0 and (year % 400 !=0 and year % 100 !=0 )       # Return True for leap year and False for normal year

def calculate_due_date(borrowDate, period):
    """ Calculate the due date of a borrowed book and return a string in the format YYYY-MM-DD 
        borrowDate: String in the format YYYY-MM-DD
        period: Integer value of the borrowing period in days. 
    """
    year, month, day = map(int, borrowDate.split("-"))  # Split the borrow date into year, month, and day. Convert them to integers.
    day += period                                       # Add the borrowing period to the day.
    while day > days_in_month(month, year):               # While the day is greater than the number of days in the month, subtract the number of days in the month from the day and increment the month. If the month is greater than 12, increment the year and set the month to 1.
        day -= days_in_month(month, year)
        month += 1
        if month > 12:
            month = 1
            year += 1
    return f"{year}-{month:02d}-{day:02d}"             # Return the due date in the format YYYY-MM-DD. The :02d formats the month and day to be two digits with leading zeros if necessary.

# Object defintions
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

class Member(User):
    def __init__(self, name, yob, contact):
        super().__init__(name, yob, contact)  # Call the parent class constructor to initialize name, yob, and contact.
        self.borrowed = {}  
    def borrow_book(self, isbn):
        """ Allows a user to borrow a book. """
        try: self.borrowed[isbn] = calculate_due_date(date, books[isbn].period)             # Calculate the due date of the book and store it in the user's borrowed books dictionary. Key = ISBN, and value = due date. Rather than storing the value as a period, where the library would have to calculate the due date each time, we can store the due date directly. This is more efficient, as the library can simply check if the due date has passed or not.
        except KeyError: print(f"Book with ISBN {isbn} not found.")
    def return_book(self, isbn):
        """ Allows a user to return a book. """
        try: del self.borrowed[isbn]                 # Check if the book is in the user's borrowed books dictionary. If so, Remove the book from the user's borrowed books dictionary.
        except KeyError: print(f"You have not borrowed this book.")            # If the book is not in the user's borrowed books dictionary, print an error message.
    def print_borrowed(self):
        """ Prints all the books a user has borrowed. It prints the due date rather than the days left, as the due date is more useful to the user. """
        for isbn in self.borrowed:                                     # For each key in the user's borrowed books (For each ISBN int)
            print(f"ISBN: {isbn}, Title: {books[isbn].title},{' ' * (minTitleLength - len(books[isbn].title))}" +   # Print the key (ISBN), the title of the book, the author of the book, and the due date. The due date is calculated with the current date and the borrowing period from the borrowed dictionary value
                    f"Author: {books[isbn].author},{' ' * (minAuthorLength - len(books[isbn].author))}" + 
                    f"Due Date: {self.borrowed[isbn]}")


# Add a bunch of book data to simulate pre-existing books in the library. They Key is the ISBN.
books[0] = Book(0, "The Silver Eyes", "Scott Cawthon & Kira Breed Wrisley", 7)
books[1] = Book(1, "Every Day", "David Levithan", 14)
books[2] = Book(2, "M is for Monster", "Talia Dutton", 14)
books[3] = Book(3, "Kill the Villainess", "Haegi", 27)
author = "Stephen King"
books[4] = Book(4, "The Shining", author, 14)
books[5] = Book(5, "Pet Sematary", author, 7)
books[6] = Book(6, "The Institute", author, 7)

# library_assets = {
#     0: Book(),
#     1: Book("J. R. R. Tolkien", "The Hobbit", 7, "blah blah blah", paperback=9780261103344, hardcover=9780261103283, digital=9780261103587),
#     2: Book("David Levithan", "Everyday", 14, "blah blah blah", paperback=9780307931894, digital=9780307931111),
#     3: Book("Talia Dutton", "M is for Monster", 14, "blah blah blah", paperback=9781419751974),
#     4: Book("Haegi", "Kill the Villainess", 27, "blah blah blah", paperback=9798400902864),
#     5: Book("Stephen King", "Pet Sematary", 7, "blah blah blah", paperback=9781444708134, audio=9781473688582, digital=9781848940857),
#     6: Book("Stephen King", "The Institute", 7, "blah blah blah", paperback=9781529355413, audio=9781529355383, digital=9781529355420),
#     4: Book("Stephen King", "The Shining", 14, "blah blah blah", paperback=9781399765350),
#     5: Newspaper("The Courier Mail", "03/09/1945", None, physical=9780000000000, digital=9780000000001),
#     6: Music("The Rolling Stones", "Tattoo You", 7, "Hard Rock", ("Start Me Up", ...), cd=9780000000002, vinyl=9780000000003, digital=9780000000004),
#     7: Video("CoolAuthor", "CoolTitle", "SOMESUMMARY", 14, dvd=9780000000005, bluray=9780000000006, digital=9780000000007),
#     8: Misc("", "", 14, physical=9780000000008, digital=9780000000009)
# }


# Add a bunch of user data to simulate pre-existing users in the library.
users.append(Member("Kira", 1980, "CatLover2048@example.com"))
users.append(Member("Ron", 1967, "GuyWithMoustache@example.com"))
users.append(Member("Davidson", 2005, "FFunkinBoy@domain.edu.au"))

def print_library_catalogue():
    """ Function that prints all the books in the library collection. """
    for book in books:
        print(f"ISBN: {book}, Title: {books[book].title},{' ' * (minTitleLength - len(books[book].title))}" +   # The same as print_user_book_list(), but instead of the due date, it prints the borrowing period. This is more useful for library staff to calculate the due date for each user. It also shows users how long they can borrow a book.
              f"Author: {books[book].author},{' ' * (minAuthorLength - len(books[book].author))} Borrowing Period: {books[book].period} days")

def list_library_users():
    """ Function that prints all the users in the library collection. """
    for user in users: print(f"Name: {user.name}, Year of Birth: {user.yob}, Contact: {user.contact}")          # Prints all the users in the library collection. It prints the user's name, year of birth, and contact information.


# Concepts we might add later...
# \ escapes the newline character, so the string continues on the next line. Learned through CISCO Module 4.5.1


def validate_user():
    pass

def sign_up():
    """ Allows a user to sign up for the library system. If users sign up, they should automatically be logged in. """
    name = input("Please enter your name: ")
    yob = input("Please enter your year of birth in the format YYYY: ")
    contact = input("Please enter your contact information (phone or email): ")
    print(f"Thank you for signing up, {name}!")

def login():
# TODO Validation
    while True:
        option = user_menu()                                                                          # After validation, show the user menu.
        if option == "1": borrow_asset(users[0])                                                       # For testing purposes, we will use the first user in the list.
                                                                                                     # TODO: OTHER OPTIONS
        elif option == "4": print_library_catalogue()                                                      # Print all the books in the library.
        elif option == "5": break
        else: print("Invalid option. Please try again.")

def borrow_asset(user):
    """ Allows a user to borrow assets. """
    found = check_asset(user, "borrow")
    if found != None: alrdy_brrwd_msg(user, found[0][0])                                                    # If they already own it, tell the user they already borrowed that book, otherwise add it to the borrowed books library

def return_asset(user):
    found = check_asset(user, "return")
    if found != None: user.return_book(found[0][0])                                                        # Call the return_book method from the User class.

def check_asset(user, decision):
    """ Allows a user to return assets. """
    while True:
        while True:
            action = input(f"Please enter the type of media you would like to {decision} (book, newspaper, music, video, misc) or enter 'd' to finish:\n> ")
            if action.lower() not in ("book", "newspaper", "music", "video", "misc", "d"): print("Invalid option. Please try again.")  # If the input is not a valid option, print an error message.
            else: break                                                                                     # If the input is valid, break out of the loop and continue with the rest of the function.
        if action == "d": break                                                                      # Exit the loop and return back to caller (login() function).
        name = input(f"Please enter the title of the {action} you would like to {decision}:\n> ")
        media_type = Book if action.lower() == "book" else None                                      # Convert the input to lowercase to make it case-insensitive.
        found = [(isbn, books[isbn].title) for isbn in books if name.lower() in books[isbn].title.lower() and isinstance(books[isbn], media_type)] # 
        if len(found) == 0: print(f"{action} with title '{name}' not found. Please try again.")    # If the list is empty, the book is not found, so print an error message.
        else: alrdy_brrwd_msg(user, found[0][0])                                                    # If they already own it, tell the user they already borrowed that book, otherwise add it to the borrowed books library

def alrdy_brrwd_msg(user, isbn):
    """ Checks if the user has already borrowed the book. If they have, tell them, otherwise, add the book to the user's borrowed books library. """
    if isbn in user.borrowed: print(f"You have already borrowed {books[isbn].title}.")  # Check if the user has already borrowed the book.
    else:
        user.borrow_book(isbn)                                                      # Call the borrow_book method from the User class.
        print(f"Successfully borrowed {books[isbn].title}. It is due on {user.borrowed[isbn]}.")  # Print the title of the book and the due date.

def menu():
    option =input(
f"""
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃  Welcome to the Library System  ┃
┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
┃     Please select an option:    ┃
┃           1: Log In             ┃
┃           2: Sign Up            ┃
┃           3: Quit               ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
""")
    return option
def user_menu():
    option = input(
f"""
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃            User Menu            ┃
┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
┃     Please select an option:    ┃
┃       1: Borrow                 ┃
┃       2: Return                 ┃
┃       3. View Your Books        ┃
┃       4. View Library Catalouge ┃
┃       5: Back to Main Menu      ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
""")
    return option

def Goodbye():
    print("""
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃  Thank you for using the Library System. Goodbye!  ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛""")

def main():
    """ Main function that runs the program. """
    # TESTING PURPOSES ONLY.
    # print("all books:")
    # PrintLibraryBooks()
    # print()

    # user = users[0]     # For testing purposes, we will use the first user in the list.
    # user.borrow_book(0)  # User borrows the book
    # user.borrow_book(3)  # User borrows the book
    # print("borrowed books:")
    # user.PrintBorrowedBooks()  # Print the user's borrowed books
    # print()

    # user.ReturnBook(3)  # User returns the book
    # print("borrowed books after returning a book:")
    # user.PrintBorrowedBooks()  # Print the user's borrowed books after returning a book

    while True:  # Keep the program running until the user chooses to quit.
        option = menu()  # Display the menu and get the user's choice.
        if option == "1": login()
        elif option == "2": sign_up()
        elif option == "3":
            Goodbye()
            break
        else: print("Invalid option. Please try again.")


#clear_screen() # Clear the cosnole screen

main()
