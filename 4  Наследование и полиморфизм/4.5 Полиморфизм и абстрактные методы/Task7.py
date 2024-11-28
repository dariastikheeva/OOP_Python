from abc import ABC, abstractmethod

class StackInterface(ABC):
    @abstractmethod
    def push_back(self, obj):
        pass

    @abstractmethod
    def pop_back(self):
        pass

class StackObj:
    def __init__(self, data):
        self._data = data
        self._next = None


class Stack(StackInterface):
    def __init__(self):
        self._top = None
    
    def push_back(self, obj):
        if self._top == None:
            self._top = obj
        else:
            curr = self._top
            while curr._next != None:
                curr = curr._next
            curr._next = obj

    def pop_back(self):
        curr = self._top
        if curr:
            prev = None
            while curr._next:
                prev = curr
                curr = curr._next  
            if prev:
                prev._next = None
            else:
                self._top = None
        return curr

    def get_data(self):
        lst = []
        curr = self._top
        while curr:
            lst.append(curr._data)
            curr = curr._next
        return lst
    
    def __add__(self, obj):
        self.push_back(obj)
        return self
    
    def __mul__(self, lst):
        for i in lst:
            self.push_back(StackObj(i))
        return self
    