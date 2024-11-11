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
    
    def push_back(self, obj):
        if self.top == None:
            self.top = obj
        else:
            curr = self.top
            while curr.next != None:
                curr = curr.next
            curr.next = obj

    def pop_back(self):
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

    def get_data(self):
        lst = []
        curr = self.top
        while curr:
            lst.append(curr.data)
            curr = curr.next
        return lst
    
    def __add__(self, obj):
        self.push_back(obj)
        return self
    
    def __mul__(self, lst):
        for i in lst:
            self.push_back(StackObj(i))
        return self
