import mysql.connector
from prettytable import PrettyTable

# Database configuration
DB_CONFIG = {
    'user': 'root',
    'password': 'Smruti@123',
    'host': '127.0.0.1',
    'database': 'apollo_db',
}

def create_connection():
    conn = mysql.connector.connect(**DB_CONFIG)
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            author VARCHAR(255) NOT NULL,
            year INT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_book(title, author, year):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO books (title, author, year) VALUES (%s, %s, %s)', (title, author, year))
    conn.commit()
    conn.close()

def get_books():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM books')
    books = cursor.fetchall()
    conn.close()
    return books

def update_book(book_id, title, author, year):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE books SET title = %s, author = %s, year = %s WHERE id = %s', (title, author, year, book_id))
    conn.commit()
    conn.close()

def delete_book(book_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM books WHERE id = %s', (book_id,))
    conn.commit()
    conn.close()

def print_books():
    books = get_books()
    table = PrettyTable(['ID', 'Title', 'Author', 'Year'])
    for book in books:
        table.add_row(book)
    print(table)

if __name__ == "__main__":
    create_table()
    while True:
        print("Apollo DB Management System")
        print("1. Add Book")
        print("2. View Books")
        print("3. Update Book")
        print("4. Delete Book")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            year = input("Enter book year: ")
            add_book(title, author, int(year))
        elif choice == '2':
            print_books()
        elif choice == '3':
            book_id = int(input("Enter book ID to update: "))
            title = input("Enter new title: ")
            author = input("Enter new author: ")
            year = input("Enter new year: ")
            update_book(book_id, title, author, int(year))
        elif choice == '4':
            book_id = int(input("Enter book ID to delete: "))
            delete_book(book_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice! Please try again.")
