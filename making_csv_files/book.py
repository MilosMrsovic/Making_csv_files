class Book:
    def __init__(self,book_id, title, author, published, genre,):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.published = published 
        self.genre = genre
        
        
    def __str__(self):
        return f"Book ID: {self.book_id}, \n{self.title}, {self.author}, \n{self.published}, \n{self.genre}"
    
    @staticmethod
    def create_from_dict(row):
        return Book(row["book_id"], row["title"], row["author"], row["published"], row["genre"])