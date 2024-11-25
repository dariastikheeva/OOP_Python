class Thing:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight
        
    def __hash__(self):
        return hash((self.name, self.price, self.weight))

    def __eq__(self, value):
        return hash(self) == hash(value)

class DictShop(dict):
    def __init__(self, *args):
        if args:
            if not isinstance(args[0], dict):
                raise TypeError('аргумент должен быть словарем')
            for thing in args[0]:
                if not isinstance(thing, Thing):
                    raise TypeError('ключами могут быть только объекты класса Thing')
        return super().__init__(*args)

    def __setitem__(self, key, value):
        if not isinstance(key, Thing):
            raise TypeError('ключами могут быть только объекты класса Thing')
        return super().__setitem__(key, value)
