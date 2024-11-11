import sys

# здесь объявляйте класс
class BookStudy:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = int(year)

    def __hash__(self):
        return hash((self.name.lower(), self.author.lower()))

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))  # список lst_in не менять!

# здесь продолжайте программу (используйте список строк lst_in)
lst_bs = []

for book in lst_in:
    book = book.split(';')
    bs = BookStudy(book[0], book[1], book[2])
    lst_bs.append(bs)

unique_books = len(set(hash(i) for i in lst_bs))
