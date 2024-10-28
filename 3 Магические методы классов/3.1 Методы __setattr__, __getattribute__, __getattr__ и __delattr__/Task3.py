class Book:
    def __init__(self, title='', author='', pages=0, year=0):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year

    def __setattr__(self, name, value):
        if name in ('title', 'author'):
            if isinstance(value, str):
                object.__setattr__(self, name, value)
            else:
                raise TypeError("Неверный тип присваиваемых данных.")
        elif name in ('pages', 'year'):
            if isinstance(value, int):
                object.__setattr__(self, name, value)
            else:
                raise TypeError("Неверный тип присваиваемых данных.")

        
book = Book('Python ООП', 'Сергей Балакирев', 123, 2022)
