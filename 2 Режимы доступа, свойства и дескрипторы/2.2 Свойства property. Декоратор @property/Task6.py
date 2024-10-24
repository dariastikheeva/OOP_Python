class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None
        self.__prev = None
    
    @property
    def next(self):
        return self.__next
    @next.setter
    def next(self, next):
        if type(next) == StackObj or next is None:
            self.__next = next

    @property
    def prev(self):
        return self.__prev
    @prev.setter
    def prev(self, prev):
        self.__prev = prev

    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self, data):
        self.__data = data

class Stack:
    def __init__(self):
        self.top = None
        self.last = None

    def push(self, obj):
        if not self.top:
            self.top = obj
        if self.last:
            self.last.next = obj
        obj.prev = self.last
        self.last = obj

    def pop(self):
        if not self.last:
            return
        p = self.last.prev
        if p:
            n = p.next
            p.next = None
        self.last = p
        if self.last == None:
            self.top = None
        return n
    
    def get_data(self):
        lst = []
        h = self.top
        while h:
            lst.append(h.data)
            h = h.next
        return lst
