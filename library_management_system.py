class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        self.books = []

    def add_book_to_shelf(self, book):
        self.books.append(book)

    def show_all_books(self):
        self.print_books(self.books)

    def print_books(self, books):
        for book in books:
            print(str(book))
        print()

    def search_books(self, title):
        filtered_books = filter(lambda book: title.lower() in book.title.lower(), self.books)
        self.print_books(list(filtered_books))


leave_library = False

nice_library = Library()

while not leave_library:
    user_options = input("""
What do u wanna do 1,2,3 or 4? 
1.leave library 
2.show all books
3.search book
4.add book 
""")
    if user_options == "1":
        leave_library = True
    elif user_options == "2":
        nice_library.show_all_books()
    elif user_options == "3":
        book = input("which book do u wanna search? \n")
        nice_library.search_books(book)
    elif user_options == "4":
        name_of_book = input("whats the name of your book you wanna submit? \n")
        author_of_book = input("whos the author of the book? \n")
        nice_library.add_book_to_shelf(Book(name_of_book, author_of_book))
    else:
        print("not a valid option")
