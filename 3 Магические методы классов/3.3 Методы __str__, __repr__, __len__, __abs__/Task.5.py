class ObjList:
    def __init__(self, data):
        self.__next = None
        self.__prev = None
        self.__data = data

    def set_next(self, obj):
        self.__next = obj

    def set_prev(self, obj):
        self.__prev = obj

    def get_next(self):
        return self.__next

    def get_prev(self):
        return self.__prev

    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def add_obj(self, obj):
        if not self.head:
            self.head = obj
        if self.tail:
            self.tail.set_next(obj)
        obj.set_prev(self.tail)
        self.tail = obj
        self.count += 1

    def remove_obj(self, indx):
        if self.tail == None:
            return
        c = 0
        h = self.head
        while c != indx:
            h = h.get_next()
            c += 1
        if h == self.head and h == self.tail:
            self.head = self.tail = None
        elif h == self.head:
            self.head = h.get_next()
            h.get_next().set_prev(None)
        elif h == self.tail:
            self.tail = h.get_prev()
            h.get_prev().set_next(None)
        else:
            h.get_next().set_prev(h.get_prev())
            h.get_prev().set_next(h.get_next())
        self.count -= 1

    def __len__(self):
        return self.count
    
    def __call__(self, indx):
        if indx == 0:
            return self.head.get_data() if self.head else None
        else:
            h = self.head
            c = 0
            while c != indx:
                h = h.get_next()
                c += 1
            return h.get_data() if h else None
