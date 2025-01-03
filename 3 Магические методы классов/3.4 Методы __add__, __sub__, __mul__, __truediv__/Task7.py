class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

class Lib:
    def __init__(self):
        self.book_list = []
    
    def __add__(self, book):
        self.book_list.append(book)
        return self
    
    def __sub__(self, other):
        if isinstance(other, Book):
            self.book_list.remove(other)
        else:
            self.book_list.pop(other)
        return self
    
    def __len__(self):
        return len(self.book_list)
