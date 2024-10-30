import time

class Object:
    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        if key == 'date' and key in self.__dict__.keys():
            return
        else:
            object.__setattr__(self, key, value)

class Mechanical(Object):
    pass

class Aragon(Object):
    pass

class Calcium(Object):
    pass

class GeyserClassic:
    MAX_DATE_FILTER = 100
    filters = {1: None, 2: None, 3: None}

    def add_filter(self, slot_num, filter):
        validate_type = {1: isinstance(filter, Mechanical), 
                         2: isinstance(filter, Aragon),
                         3: isinstance(filter, Calcium)}
        
        if self.filters[slot_num] is None and validate_type[slot_num]:
            self.filters[slot_num] = filter

    def remove_filter(self, slot_num):
        self.filters[slot_num] = None

    def get_filters(self):
        return tuple(self.filters.values())
    
    def water_on(self):
        if all(self.filters.values()):
            if all(0 <= time.time() - v.date <= self.MAX_DATE_FILTER for v in self.filters.values()):
                return True
        return False
