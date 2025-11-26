# ------------------------------------------------------------
# Name: ALKA
# Roll No: 2501060083
# Course: BCA (AI & DS)
# Semester: 1st
# Subject: Problem Solving with Python
# Assignment: Unit-2 Mini Project
# Title: Library Inventory & Borrowing System
# ------------------------------------------------------------

print("\n==============================================")
print("         WELCOME TO LIBRARY MANAGER")
print("==============================================\n")

# Global Data Storage
books = {}
borrowed = {}

# ------------------------------------------------------------
# DISPLAY ALL BOOKS
# ------------------------------------------------------------
def view_books():
    if not books:
        print("\nNo books available!\n")
        return

    print("\n================ LIBRARY BOOKS ================\n")
    print(f"{'Book ID':<10} {'Title':<20} {'Author':<15} {'Copies':<10}")
    print("-" * 60)

    for book_id, data in books.items():
        print(f"{book_id:<10} {data['title']:<20} {data['author']:<15} {data['copies']:<10}")
    print()

# ------------------------------------------------------------
# SEARCH FUNCTIONS
# ------------------------------------------------------------
def search_by_id(book_id):
    return books.get(book_id, None)

def search_by_title(keyword):
    results = []
    for bid, data in books.items():
        if keyword.lower() in data["title"].lower():
            results.append((bid, data))
    return results

# ------------------------------------------------------------
# BORROW BOOK
# ------------------------------------------------------------
def borrow_book():
    student = input("Enter student name: ")
    book_id = input("Enter Book ID to borrow: ")

    if book_id not in books:
        print("\n❌ Book does not exist in library.\n")
        return

    if books[book_id]["copies"] > 0:
        books[book_id]["copies"] -= 1
        borrowed[student] = book_id
        print(f"\n✔ {student} successfully borrowed {book_id}.\n")
    else:
        print("\n❌ No copies available right now.\n")

# ------------------------------------------------------------
# RETURN BOOK
# ------------------------------------------------------------
def return_book():
    student = input("Enter student name: ")
    book_id = input("Enter Book ID to return: ")

    if student not in borrowed:
        print("\n❌ This student has not borrowed any book.\n")
        return

    if borrowed[student] != book_id:
        print("\n❌ This student did not borrow this book.\n")
        return

    books[book_id]["copies"] += 1
    del borrowed[student]

    print(f"\n✔ Book {book_id} returned successfully.\n")
    print("Current Borrowed Books:", borrowed)

# ------------------------------------------------------------
# ADD BOOK
# ------------------------------------------------------------
def add_book():
    print("\nEnter Book Details:")
    book_id = input("Book ID: ")
    title = input("Title: ")
    author = input("Author: ")
    copies = int(input("Copies: "))

    books[book_id] = {"title": title, "author": author, "copies": copies}
    print("\n✔ Book added successfully!\n")

# ------------------------------------------------------------
# MAIN MENU
# ------------------------------------------------------------
def menu():
    while True:
        print("\n========= LIBRARY MENU =========")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. Exit")
        print("===============================\n")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_book()

        elif choice == "2":
            view_books()

        elif choice == "3":
            print("\nSearch by:")
            print("1. Book ID")
            print("2. Title\n")
            search_choice = input("Enter choice: ")

            if search_choice == "1":
                bid = input("Enter Book ID: ")
                result = search_by_id(bid)
                if result:
                    print("\nBook Found:", result, "\n")
                else:
                    print("\n❌ Book Not Found\n")

            elif search_choice == "2":
                keyword = input("Enter title keyword: ")
                results = search_by_title(keyword)
                if results:
                    print("\nSearch Results:")
                    for r in results:
                        print(r)
                else:
                    print("\n❌ No matching books found\n")
            else:
                print("\n❌ Invalid search choice.\n")

        elif choice == "4":
            borrow_book()

        elif choice == "5":
            return_book()

        elif choice == "6":
            print("\nThank you for using Library Manager!\n")
            break

        else:
            print("\n❌ Invalid choice. Please try again.\n")

# ------------------------------------------------------------
# Start Program
# ------------------------------------------------------------
menu()
