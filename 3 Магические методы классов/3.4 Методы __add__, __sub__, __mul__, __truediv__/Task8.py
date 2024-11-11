class Item:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def __add__(self, it):
        return self.money + it.money
    
    def __radd__(self, it):
        return self.money + it
    
class Budget:
    def __init__(self):
        self.items = []

    def add_item(self, it):
        self.items.append(it)

    def remove_item(self, indx):
        self.items.pop(indx)

    def get_items(self):
        return self.items
