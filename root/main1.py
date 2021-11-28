from Library import *
from gitupdate import *

if __name__ == "__main__":
    library_name = "Aryan Lohia's Library"
    OWNER = LibraryClass(library_name)
    print(f"\n\nWelcome to {library_name}\n")
    OWNER.Display_book()
    while (True):
            print("\nWhat would you like to do now?\nPress 1 to display booklist again\nPress 2 to search for a book in the booklist\nPress 3 to get a book\nPress 4 to add a book to the booklist\nPress q to quit\n")
            choice = input()
            if (choice.upper() != 'Q'):
                OWNER.User_choice( choice)
            else:
                break

    if(OWNER.update==True):
        update_booklist(OWNER.username)
