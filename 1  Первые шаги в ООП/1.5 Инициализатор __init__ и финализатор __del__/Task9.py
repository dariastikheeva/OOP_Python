import sys

# здесь объявляются все необходимые классы
class ListObject:
    def __init__(self, data):
        self.next_obj = None
        self.data = data

    def link(self, obj):
        self.next_obj = obj

# считывание списка из входного потока (эту строку не менять)
lst_in = list(map(str.strip, sys.stdin.readlines())) # список lst_in в программе не менять

# здесь создаются объекты классов и вызываются нужные методы
head_obj = ListObject(lst_in[0])
cur_object = head_obj
for i in lst_in[1:]:
    nxt_object = ListObject(i)
    cur_object.link(nxt_object)
    cur_object = nxt_object

