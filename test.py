while True:  # Keep the program running until the user chooses to quit.
    option = input("some menu...")
    if option == "1":
        name = input("input name")
        if name == "": break
        else:
            while True:
                option = input("some menu 2...")
                if option == "1":
                    print("getting user...")
                    while True:
                        isbn = input("Please enter the ISBN or Title of the book to borrow (or leave blank to exit): ")
                        if isbn == "": break
                        print("doing stuff with isbn")
                elif option == "2":
                    print("getting user...")
                    print("getting location")
                    while True:
                        isbn = input("Please enter the ISBN or Title of the book to return (or leave blank to exit): ")
                        if isbn == "": break
                        print("doing stuff with isbn")
                elif option == "3": print("borrowed books")                                                                             # Create a new Book object and add it to the borrowed_books list.
                elif option == "4": print("catalogue")
                elif option == "5": break
                else: print("Invalid option. Please try again.")
    elif option == "2":
        while True:
            option = input("some super menu...")
            if option == "1": pass
            elif option == "2": pass                                    # delete user
            elif option == "3": pass                                    # show all users
            elif option == "4": pass                                   # change user access
            elif option == "5": break
    elif option == "3": print("goodbye"); break
    else: print("Invalid option. Please try again.")