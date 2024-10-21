class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_obj(self, obj):
        if not self.head:
            self.head = obj
        if self.tail:
            self.tail.set_next(obj)
        obj.set_prev(self.tail)
        self.tail = obj

    def remove_obj(self):
        if self.tail == None:
            return
        p = self.tail.get_prev()
        if p:
            p.set_next(None)
        self.tail = p
        if self.tail == None:
            self.head = None

    def get_data(self):
        lst = []
        h = self.head
        while h:
            lst.append(h.get_data())
            h = h.get_next()
        return lst


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
