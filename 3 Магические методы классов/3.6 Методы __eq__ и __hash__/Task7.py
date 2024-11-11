import sys

# здесь объявляйте классы
class Record:
    START_PK = 1
    def __init__(self, fio, descr, old):
        self.pk = Record.START_PK
        Record.START_PK += 1
        self.fio = fio
        self.descr = descr
        self.old = int(old)

    def __hash__(self):
        return hash((self.fio.lower(), self.old))
    
    def __eq__(self, value):
        return hash(self) == hash(value)
    
class DataBase:
    def __init__(self, path):
        self.path = path
        self.dict_db = {}
    
    def write(self, record):
        if record not in self.dict_db:
            self.dict_db[record] = [record]
        else:
            self.dict_db[record].append(record)

    def read(self, pk):
        for i in self.dict_db.values():
            for j in i:
                if j.pk == pk:
                    return j

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines())) # список lst_in не менять!

# здесь продолжайте программу (используйте список строк lst_in)
db = DataBase('/whatever')

for i in lst_in:
    i = i.split(';')
    record = Record(i[0], i[1], i[2])
    db.write(record)
