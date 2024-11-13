class Thing(object):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


class Bag(object):
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.things = []
        self.current_weight = 0

    def add_thing(self, thing):
        if self.current_weight + thing.weight <= self.max_weight:
            self.things.append(thing)
            self.current_weight += thing.weight
        else:
            raise ValueError('превышен суммарный вес предметов')

    def check_index(self, key):
        if key < 0 or key > len(self.things):
            raise IndexError('неверный индекс')

    def __getitem__(self, key):
        self.check_index(key)
        return self.things[key]

    def __setitem__(self, key, value):
        self.check_index(key)
        tmp_thing = self.things[key]
        if self.current_weight - tmp_thing.weight + value.weight <= self.max_weight:
            self.things[key] = value
            self.current_weight = self.current_weight - tmp_thing.weight + value.weight
        else:
            raise ValueError("превышен суммарный вес предметов")

    def __delitem__(self, key):
        self.check_index(key)
        tmp_thing = self.things[key]
        self.current_weight -= tmp_thing.weight
        self.things.pop(key)
