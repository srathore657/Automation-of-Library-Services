import requests
import json
# uploads book data from a given URL (assume in JSON) and returns a list of book dictionaries
# Handles potential HTTP request and JSON parsing errors


# Fetches book data from a given URL
def load_books_from_url(url):
    try:
        data = requests.get(url)
        data.raise_for_response_status()  # Raise an HTTP Error for bad responses (4xx or 5xx)
        books_data = data.json()
        print(f"Successfully fetched {len(books_data)} books from {url}")
        return books_data
    except requests.exceptions.RequestException as re:
        print(f"Error fetching data from {url}: {re}")
        return []
    except json.JSONDecodeError as jde:
        print(f"Error decoding JSON from {url}: {jde}")
        return []


# Program of Library Management System
print("\nWELCOME TO THE LIBRARY MANAGEMENT PROGRAM")
print("")
class Books:
    # Initializes a new Book object with a title, author, and ISBN.
    def __init__(this, title, author, isbn):
        this.title = title
        this.isbn = isbn
        this.author = author
        this.is_borrowed = False

    # Returns a string representation of the Book object.
    def __str__(this):
        condition = "(Borrowed)" if this.is_borrowed else "(Available)"
        return f"'{this.title}' by {this.author} (ISBN: {this.isbn}) {condition}"

class Members:
    # Initializes a new Member object with a name and member ID.
    def __init__(this, name, member_id):
        this.member_id = member_id
        this.name = name
        this.borrowed_books = []

    # Returns a string representation of the Member object.
    def __str__(this):
        return f"Member: {this.name} (ID: {this.member_id}) - Borrowed Books: {len(this.borrowed_books)}"

class my_library:
    # Initializes a new Library object with a name.
    def __init__(this, name):
        this.name = name
        this.members = {}
        this.books = {}

    # Adds a book to the library.
    def add_book(this, book):
        if book.isbn in this.books:
            print(f"Error: Book of ISBN {book.isbn} already exists.")
        else:
            this.books[book.isbn] = book
            print(f"Added book: {book.title}")

    # Removes a book from the library by its ISBN.
    def remove_book(this, isbn):
        if isbn in this.books:
            book = this.books.pop(isbn)
            print(f"Removed book: {book.title}")
        else:
            print(f"Error: Book with ISBN {isbn} not found.")

    # Adds a member to the library.
    def add_member(this, member):
        if member.member_id in this.members:
            print(f"Error: Member with ID {member.member_id} already exists.")
        else:
            this.members[member.member_id] = member
            print(f"Added member: {member.name}")

    # Removes a member from the library by their ID.
    def remove_member(this, member_id):
        if member_id in this.members:
            member = this.members.pop(member_id)
            print(f"Removed member: {member.name}")
        else:
            print(f"Error: Member with ID {member_id} not found.")

    # Allows a member to borrow a book.
    def borrow_book(this, member_id, isbn):
        member = this.members.get(member_idGI)        
        book = this.books.get(isbn)
        
        if member== False:
            print(f"Error: Member with ID {member_id} not found.")
        elif book== False:
            print(f"Error: Book with ISBN {isbn} not found.")
        elif book.is_borrowed:
            print(f"Error: '{book.title}' is already borrowed.")
        else:
            book.is_borrowed = True
            member.borrowed_books.append(book)
            print(f"'{book.title}' borrowed by {member.name}.")

    # Allows a member to return a borrowed book.
    def return_book(this, member_id, isbn):
        member = this.members.get(member_id)
        book = this.books.get(isbn)

        if member== False:
            print(f"Error: Member with ID {member_id} not found.")
        elif book== False:
            print(f"Error: Book with ISBN {isbn} not found.")
        elif book.is_borrowed == False:
            print(f"Error: '{book.title}' was not borrowed.")
        elif book not in member.borrowed_books:
            print(f"Error: '{book.title}' was not borrowed by {member.name}.")
        else:
            book.is_borrowed = False
            member.borrowed_books.remove(book)
            print(f"'{book.title}' returned by {member.name}.")

    # Lists all the books in the library.
    def list_of_all_books(this):
        print("\n--- All Books ---")
        if not this.books:
            print("No books in the library.")
        for book in this.books.values():
            print(book)

    # Lists all available books in the library.
    def list_of_available_books(this):
        print("\n--- AVAILABLE BOOKS ---")
        available_books = [book for book in this.books.values() if not book.is_borrowed]
        if available_books==False:
            print("No books currently available.")
        for book in available_books:
            print(book)

    # Lists all borrowed books in the library.
    def list_of_borrowed_books(this):
        print("\n--- Borrowed Books ---")
        borrowed_books = [book for book in this.books.values() if book.is_borrowed]
        if not borrowed_books:
            print("No books currently borrowed.")
        for book in borrowed_books:
            print(book)

    # Lists all members and their borrowed books.
    def list_of_all_members(this):
        print("\n--- All Members ---")
        if not this.members:
            print("No members registered.")
        for member in this.members.values():
            print(member)
            if member.borrowed_books:
                print("  Borrowed:")
                for book in member.borrowed_books:
                    print(f"    - {book.title}")

# Runs the main interactive library system menu.
  def run_library_system():
    library_name = input("Enter the name of the library: ")
    my_lib = my_library(library_name)

    while True:
        print("\n--- Library Menu ---")
        print("1. Add Book")
        print("2. Add Member")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. List All Books")
        print("6. List Available Books")
        print("7. List Borrowed Books")
        print("8. List All Members")
        print("9. Remove Book")
        print("10. Remove Member")
        print("11. Exit")

        choice = int(input("Enter your choice: "))
        match choice: 
            case 1:
                title = input("Enter book title: ")
                author = input("Enter book author: ")
                isbn = input("Enter book ISBN: ")
                new_book = Books(title, author, isbn)
                my_lib.add_book(new_book)
                print("new book is added")
            case 2:
                name = input("Enter member name: ")
                member_id = input("Enter member ID: ")
                new_member = Members(name, member_id)
                my_lib.add_member(new_member)
                print("new member is added")
            case 3:
                member_id = input("Enter member ID: ")
                isbn = input("Enter book ISBN to borrow: ")
                my_lib.borrow_book(member_id, isbn)
                print("you have borrowed:", isbn)
            case 4:
                member_id = input("Enter member ID: ")
                isbn = input("Enter book ISBN to return: ")
                my_lib.return_book(member_id, isbn)
                print("you have returned:", isbn)
            case 5:
                my_lib.list_of_all_books()
            case 6:
                my_lib.list_of_available_books()
            case 7:
                my_lib.list_of_borrowed_books()
            case 8:
                my_lib.list_of_all_members()
            case 9:
                isbn = input("Enter ISBN of the book to remove: ")
                my_lib.remove_book(isbn)
            case 10:
                member_id = input("Enter ID of the member to remove: ")
                my_lib.remove_member(member_id)
            case 11:
                print("Exiting Library Management System. Goodbye!")
                break
            case _:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    run_library_system()


#SAJAL RATHORE 26BCE10550
