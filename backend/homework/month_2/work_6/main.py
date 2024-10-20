import os
import json
from time import sleep


class Book:
    def __init__(self, title, author, year, read=False):
        self.title = title
        self.author = author
        self.year = year
        self.read = read

    def markAsRead(self):
        self.read = True

    def markAsUnread(self):
        self.read = False

    def __str__(self):
        readStatus = "✔️  read" if self.read else "✖️  unread"
        return f"{readStatus} | {self.title} by {self.author} ({self.year})"

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "read": self.read,
        }


class Library:
    def __init__(self, filepath="library.json"):
        self.books = []
        self.filepath = filepath
        self.load_books()

    def addBook(self, *books):
        self.books.extend(books)
        self.save_books()

    def listBooks(self):
        if not self.books:
            return "Библиотека пуста."
        return "\n".join(
            f"{index}. {book}" for index, book in enumerate(self.books, start=1)
        )

    def findTitle(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def markBookAsRead(self, title):
        book = self.findTitle(title)
        if book:
            book.markAsRead()
            self.save_books()
            return True
        return False

    def markBookAsUnread(self, title):
        book = self.findTitle(title)
        if book:
            book.markAsUnread()
            self.save_books()
            return True
        return False

    def removeBook(self, title):
        book = self.findTitle(title)
        if book:
            self.books.remove(book)
            self.save_books()
            print(f"Книга '{title}' удалена из библиотеки.")
        else:
            print(f"Книга '{title}' не найдена.")

    def save_books(self):
        with open(self.filepath, "w", encoding="utf-8") as file:
            json_books = [book.to_dict() for book in self.books]
            json.dump(json_books, file, ensure_ascii=False, indent=4)

    def load_books(self):
        if os.path.exists(self.filepath):
            with open(self.filepath, "r", encoding="utf-8") as file:
                books_data = json.load(file)
                for book_data in books_data:
                    self.books.append(
                        Book(
                            book_data["title"],
                            book_data["author"],
                            book_data["year"],
                            book_data["read"],
                        )
                    )

    def __str__(self):
        return self.listBooks()


library = Library()


def get_year_input():
    while True:
        year = input("Enter year: ")
        try:
            return int(year)
        except ValueError:
            print("Неправильный ввод года. Пожалуйста, введите число.")


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


while True:
    try:
        clear_screen()
        print("Menu:\n1. Enter Book\n2. Library\n━━━━━━━━━━━━━━━━━\n3. Exit")
        userInput = input("\noption: ")

        if userInput in ["exit", "quit", "e", "q", "3"]:
            clear_screen()
            break

        clear_screen()
        if userInput == "1":
            title = input("\nyour book:\n━━━━━━━━━━━━\nEnter title: ")
            author = input("Enter author: ")
            year = get_year_input()

            read = input("Read? [y/n]: ")
            read = read.lower() == "y"
            book = Book(title, author, year, read)
            library.addBook(book)

        elif userInput == "2":
            clear_screen()

            print(
                "Library:\n1. list books\n2. find book\n3. mark book as read\n4. mark book as unread\n5. remove book\n6. back\n━━━━━━━━━━━━━━━━━\n7. exit"
            )
            command = input("\noption: ")

            if command in ["exit", "quit", "e", "q", "7"]:
                clear_screen()
                break

            if command == "1":
                clear_screen()
                print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                print(library)
                print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                sleep(4)

            elif command == "2":
                title = input("title: ")
                book = library.findTitle(title)
                if book:
                    clear_screen()
                    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                    print(book)
                    sleep(4)
                    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                else:
                    print("━━━━━━━━━━━━━━━━")
                    print("Книга не найдена.")
                    print("━━━━━━━━━━━━━━━━")

            elif command == "3":
                title = input("title: ")
                if library.markBookAsRead(title):
                    print("Книга отмечена как прочитанная.")
                else:
                    print("Книга не найдена для отметки как прочитанная.")
                print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                print(library)
                print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                sleep(4)

            elif command == "4":
                title = input("title: ")
                if library.markBookAsUnread(title):
                    print("Книга отмечена как не прочитанная.")
                else:
                    print("Книга не найдена для отметки как не прочитанная.")
                print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                print(library)
                print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                sleep(4)

            elif command == "5":
                title = input("title: ")
                library.removeBook(title)
                print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                print(library)
                print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                sleep(4)

            elif command == "6":
                clear_screen()

            else:
                clear_screen()
                print("━━━━━━━━━━━━━━━━━")
                print("Неверная опция.")
                print("━━━━━━━━━━━━━━━━━")
    except KeyboardInterrupt:
        clear_screen()
        print(
            """
                         _
                        | |__ _  _ ___
                        | '_ \ || / -_)
                        |_.__/\_, \___|
                              |__/
            """
        )
        break
