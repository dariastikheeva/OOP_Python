class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def next(self):
        return self.__next
    @next.setter
    def next(self, next):
        if isinstance(next, StackObj) or next is None:
            self.__next = next

    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self, data):
        self.__data = data

class Stack:
    def __init__(self):
        self.top = None
    
    def push(self, obj):
        if self.top == None:
            self.top = obj
        else:
            curr = self.top
            while curr.next != None:
                curr = curr.next
            curr.next = obj

    def pop(self):
        curr = self.top
        if curr:
            prev = None
            while curr.next:
                prev = curr
                curr = curr.next  
            if prev:
                prev.next = None
            else:
                self.top = None
        return curr

    def get_item(self):
        lst = []
        curr = self.top
        while curr:
            lst.append(curr)
            curr = curr.next
        return lst
    
    def __add__(self, obj):
        self.push(obj)
        return self
    
    def __mul__(self, lst):
        for i in lst:
            self.push(StackObj(i))
        return self
    
    def check_indx(self, indx):
        return type(indx) == int and indx < len(self.get_item())
    
    def __getitem__(self, indx):
        if self.check_indx(indx):
            return self.get_item()[indx]
        else:
            raise IndexError('неверный индекс')
    
    def __setitem__(self, key, value):
        if self.check_indx(key):
            self.get_item()[key].data = value.data
        else:
            raise IndexError('неверный индекс')
