books = []

while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Delete Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")

        books.append([book_id, title, author])
        print("Book Added Successfully")

    elif choice == "2":
        print("\nBooks in Library:")

        for book in books:
            print(book)

    elif choice == "3":
        search_title = input("Enter Book Title to Search: ")

        found = False

        for book in books:
            if book[1].lower() == search_title.lower():
                print("Book Found:", book)
                found = True

        if not found:
            print("Book Not Found")

    elif choice == "4":
        delete_id = input("Enter Book ID to Delete: ")

        found = False

        for book in books:
            if book[0] == delete_id:
                books.remove(book)
                print("Book Deleted Successfully")
                found = True
                break

        if not found:
            print("Book Not Found")

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")
