class NewList:
    def __init__(self, *args):
        self.lst = args[0] if args else []
        self.lst_type = [(i, type(i)) for i in self.lst]

    def __sub__(self, other):
        return self.list_diff(self, other)

    def list_diff(self, lst1, other):
        other = other if isinstance(other, list) else other.lst
        other = [(i, type(i)) for i in other]
        indxs = []
        for i in other:
            if i in lst1.lst_type:
                for j in range(1, other.count(i) + 1):
                    indx = self.get_indx(i, lst1.lst_type, j)
                    indxs.append(indx)
        return NewList([lst1.lst[i] for i in range(len(lst1.lst)) if i not in indxs])

    @staticmethod
    def get_indx(value, lst, n_occur):
        indx = -1
        for _ in range(n_occur):
            indx = lst.index(value, indx + 1)
        return indx

    def __isub__(self, other):
        self = self.list_diff(self, other)
        return self
    
    def __rsub__(self, other):
        other = NewList(other) if isinstance(other, list) else other
        return self.list_diff(other, self)
    
    def get_list(self):
        return self.lst
