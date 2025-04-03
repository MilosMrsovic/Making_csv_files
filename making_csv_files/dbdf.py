import os
from book import Book
import pandas as pd
from pandas import DataFrame

books = []
books_data_path = "books.csv"

if os.path.exists(books_data_path):
    df = pd.read_csv(books_data_path)
    for index, row in df.iterrows():
        book = Book.create_from_dict(row)
        books.append(book)
        
if (len(books) > 0):
    print("\nAll books in the library:")
    for book in books:
       print(book)
    
command = input("uneti zatrazeno (y/n): ")

while command == "y":
    book_id = input("Book ID:")
    book_id = int(book_id)
    book_title = input("Book title:")
    book_author = input("Book author:")
    book_published = input("Year of publishing:")
    book_published = int(book_published)
    book_genre = input("Book genre:")
    
    book = Book(book_id, book_title, book_author, book_published, book_genre)
    
    books.append(book)

    df = DataFrame([book.__dict__ for book in books])
    df.to_csv("books.csv", index=False)
    
    print(f"You have added new book : {book.title}")
    
    command = command = input("uneti zatrazeno (y/n): ")

print("\nAll books in the library:")
for book in books:
    print(book)
 
print("\nGoodbye!")