class Box:
    def __init__(self, name, max_weight):
        self._name = name
        self._max_weight = max_weight
        self._things = []
        self._cur_weight = 0

    def add_thing(self, obj):
        if self._cur_weight < self._max_weight:
            tmp_weight = self._cur_weight + obj[1]
            if tmp_weight > self._max_weight:
                raise ValueError('превышен суммарный вес вещей')
            else:
                self._things.append(obj)
                self._cur_weight += obj[1]
    
class BoxDefender:
    def __init__(self, box):
        self._box = box

    def __enter__(self):
        self._tmp_box = Box(self._box._name, self._box._max_weight)
        self._tmp_box._cur_weight = self._box._cur_weight
        self._tmp_box._things = self._box._things[:]
        return self._tmp_box

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self._box._things = self._tmp_box._things[:]
            self._box._cur_weight = self._tmp_box._cur_weight
        return False
