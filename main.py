""" This program tracks library books that users borrow.
    Authors: 
        Christopher Moyle - 
        Peter Poli - 
        Samantha Stevens - A00054394
"""

from Library import users, books, PrintLibraryBooks   # Using our custom Library class, we only need to access the books and users.

def SignUp():
    name = input("Please enter your name: ")
    yob = input("Please enter your year of birth in the format YYYY: ")
    contact = input("Please enter your contact information (phone or email): ")

def LogIn():
    pass

def ValidateUser():
    pass

def Menu():
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
def Goodbye():
    print("""
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃  Thank you for using the Library System. Goodbye!  ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛""")

def main():
    """ Main function that runs the program. """
    # TESTING PURPOSES ONLY.
    # Menu()
    print("all books:")
    PrintLibraryBooks()
    print()

    user = users[0]     # For testing purposes, we will use the first user in the list.
    user.BorrowBook(0)  # User borrows the book
    user.BorrowBook(3)  # User borrows the book
    print("borrowed books:")
    user.PrintBorrowedBooks()  # Print the user's borrowed books
    print()

    user.ReturnBook(3)  # User returns the book
    print("borrowed books after returning a book:")
    user.PrintBorrowedBooks()  # Print the user's borrowed books after returning a book

    while True:  # Keep the program running until the user chooses to quit.
        option = Menu()  # Display the menu and get the user's choice.
        if option == "1": LogIn()
        elif option == "2": SignUp()
        elif option == "3":
            Goodbye()
            break
        else: print("Invalid option. Please try again.")
main()