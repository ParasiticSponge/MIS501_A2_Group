""" This program tracks library books that users borrow.
    Authors: 
        Christopher Moyle - 
        Peter Poli - 
        Samantha Stevens - A00054394
"""

from Library import users, books, PrintLibraryBooks                                                  # Using our custom Library class, we only need to access the books and users.
def ValidateUser():
    pass

def SignUp():
    """ Allows a user to sign up for the library system. If users sign up, they should automatically be logged in. """
    name = input("Please enter your name: ")
    yob = input("Please enter your year of birth in the format YYYY: ")
    contact = input("Please enter your contact information (phone or email): ")
    print(f"Thank you for signing up, {name}!")

def LogIn():
                                                                                                     # TODO Validation
    while True:
        option = UserMenu()                                                                          # After validation, show the user menu.
        if option == "1": BorrowBook(users[0])                                                       # For testing purposes, we will use the first user in the list.
                                                                                                     # TODO: OTHER OPTIONS
        elif option == "4": PrintLibraryBooks()                                                      # Print all the books in the library.
        elif option == "5": break
        else: print("Invalid option. Please try again.")

def BorrowBook(user):
    """ Allows a user to borrow books. """
    while True:
        action = input("Please enter ISBN or Title of the book. Enter 'd' to finish: ")
        if action == "d": break                                                                      # Exit the loop and return back to caller (LogIn() function).
        if action.isdigit():                                                                         # Check if the input is a number.
            action = int(action)                                                                     # Convert the input to an integer.
            # The 'in' concept has been learned through CISCO module 3.6.4. It checks to see if the specified value exists in a string/list/tuple etc.
            if action in books:                                                                      # Check if the ISBN is in the books dictionary.
                if action in user.brrwd: print(f"You have already borrowed {books[action].title}.")  # Check if the user has already borrowed the book.
                else:
                    user.BorrowBook(action)                                                          # Call the BorrowBook method from the User class.
                    print(f"Successfully borrowed {books[action].title}. It is due on {user.brrwd[action]}.")  # Print the title of the book and the due date.
            else: print(f"Book with ISBN {action} not found. Please try again.")                     # If the ISBN is not in the books dictionary, print an error message.
        else:
            found = [(isbn, books[isbn].title) for isbn in books if action.lower() in books[isbn].title.lower()] # Create a tuple of (ISBN, title) for all books that match the string input. This is so if there is more than one, the user can specify which one they want.
            if len(found) == 0: print(f"Book with title '{action}' not found. Please try again.")    # If the list is empty, the book is not found, so print an error message.
            if len(found) > 1:                                                                       # If the list is longer than 1, multiple books match the input, so the user must choose between them.
                print(f"Multiple books found with the name '{action}'. Please choose a number from the list below.")
                # The use of enumeration was learned through AI. Please see group document for details. Enumeration loops through the tuple and returns the index associated with the value.
                for i, (isbn, title) in enumerate(found, start=1): print(f"{i}. ISBN: {isbn}, Title: {title}")   # Print the ISBN and title of each book that matches the input. The user can then choose which one they want to borrow.
                action = input("Please enter the number of the book you want to borrow: ")           # Reuse the action variable.
                if action.isdigit():                                                                 # Check if the input is a number.
                    action = int(action)                                                             # Convert the input to an integer.
                    if action < 1 or action > len(found): print("Invalid option. Please try again.") # Check if the input is a valid number.
                    else:
                        isbn, _ = found[action - 1]                                                  # Unpack the tuple into two variable, but keep isbn and discard the other with _.
                        AlrdyBrrwdMsg(user, isbn)                                                    # If they already own it, tell the user they already borrowed that book, otherwise add it to the borrowed books library
            else:                                                                                    # If the length is only one, don't ask the user to choose, just unpack the tuple and check the book
                isbn, _ = found[0]                                                                   # Unpack the tuple into two variable, but keep isbn and discard the other with _.
                AlrdyBrrwdMsg(user, isbn)

def AlrdyBrrwdMsg(user, isbn):
    """ Checks if the user has already borrowed the book. If they have, tell them, otherwise, add the book to the user's borrowed books library. """
    if isbn in user.brrwd: print(f"You have already borrowed {books[isbn].title}.")  # Check if the user has already borrowed the book.
    else:
        user.BorrowBook(isbn)                                                      # Call the BorrowBook method from the User class.
        print(f"Successfully borrowed {books[isbn].title}. It is due on {user.brrwd[isbn]}.")  # Print the title of the book and the due date.

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
def UserMenu():
    option = input(
f"""
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃            User Menu            ┃
┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
┃     Please select an option:    ┃
┃       1: Borrow                 ┃
┃       2: Return                 ┃
┃       3. View Your Books        ┃
┃       4. View Library's Books   ┃
┃       5: Log Out                ┃
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
    # user.BorrowBook(0)  # User borrows the book
    # user.BorrowBook(3)  # User borrows the book
    # print("borrowed books:")
    # user.PrintBorrowedBooks()  # Print the user's borrowed books
    # print()

    # user.ReturnBook(3)  # User returns the book
    # print("borrowed books after returning a book:")
    # user.PrintBorrowedBooks()  # Print the user's borrowed books after returning a book

    while True:  # Keep the program running until the user chooses to quit.
        option = Menu()  # Display the menu and get the user's choice.
        if option == "1": LogIn()
        elif option == "2": SignUp()
        elif option == "3":
            Goodbye()
            break
        else: print("Invalid option. Please try again.")
main()