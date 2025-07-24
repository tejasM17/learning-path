from datetime import datetime

class library:
    def __init__(self, book_track, avilabal, return_date ):
        self.book_track = book_track
        self.avilabal = avilabal
        self.return_date = return_date
        self.__books = {}
        self.__borrowers = {}

    def add_book(self, book_id, book_name):
        self.__books[book_id] = book_name
        return f"Id: {book_id}\nName: {book_name}\n"

    def borrow_book(self, book_id, borrower_name):
        
        if book_id not in self.__books:
            return f"❌ Book with ID {book_id} does not exist."

        if book_id in self.__borrowers:
            return f"⚠️ Book already borrowed by {self.__borrowers[book_id][0]} on {self.__borrowers[book_id][1].strftime('%Y-%m-%d %H:%M:%S')}."

        borrow_time = datetime.now()
        self.__borrowers[book_id] = (borrower_name, borrow_time)
        
    def show_borrowed_books(self):
        if not self.__borrowers:
            print("📚 No books are currently borrowed.")
            return

        print("----📖 BORROWED BOOKS ----")
        a = 0
        
        for book_id, (borrower, time) in self.__borrowers.items():
            print(f" {a+1}: 📘 {self.__books[book_id]} | 👤 Borrower: {borrower} | 🕒 Date: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
            a += 1

    def return_book(self, book_id, borrower_name):
        for id, (name, time) in self.__borrowers.items():
            if id == book_id and name == borrower_name:
                del self.__borrowers[book_id]
                return f"✅ Book with ID {book_id} returned by {borrower_name} on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}."
        return f"❌ Book with ID {book_id} not borrowed by {borrower_name}."

    def Book_rock(self):
        print("----BOOKS IN LIBRARY----")
        for book_id, book_name in self.__books.items():
            status = "Available" if book_id not in self.__borrowers else "Borrowed"
            print(f"ID: {book_id}Name: {book_name}\nStatus: {status}\n")


book_library = library("book_track", "avilabal", "return_date")


print(book_library.Book_rock())

print(f"{book_library.add_book(111, "Atomic Habits")}")
print(f"{book_library.add_book(222, "The Power Of Your Subconscious Mind")}\n")


print(f"{book_library.borrow_book(111, "Sharath")}\n")
print(f"{book_library.borrow_book(222, "Tejas")}\n")

print(f"{book_library.show_borrowed_books()}\n")


print(f"{book_library.return_book(111, "Sharath")}\n")
print(f"{book_library.return_book(222, "Tejas")}\n")
