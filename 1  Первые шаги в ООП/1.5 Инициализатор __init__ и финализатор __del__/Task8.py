# здесь пишите программу
class Cart:
    def __init__(self):
        self.goods = []

    def add(self, gd):
        self.goods.append(gd)
    
    def remove(self, indx):
        self.goods.pop(indx)

    def get_list(self):
        return [f'{i.name}: {i.price}' for i in self.goods]
    
class Table:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class TV:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Notebook:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Cup:
    def __init__(self, name, price):
        self.name = name
        self.price = price

cart = Cart()
tv1 = TV('Samsung', 70000)
tv2 = TV('Huawei', 50000)
nb1 = Notebook('Apple', 150000)
nb2 = Notebook('Lenovo', 80000)
cp = Cup('Просто кружка', 500)

cart.add(tv1)
cart.add(tv2)
cart.add(nb1)
cart.add(nb2)
cart.add(cp)
