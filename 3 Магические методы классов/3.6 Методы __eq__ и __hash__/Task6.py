import sys

# здесь объявляйте классы
class ShopItem:
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    def __hash__(self):
        return hash((self.name.lower(), self.weight, self.price))
    
    def __eq__(self, value):
        return hash(self) == hash(value)

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))  # список lst_in в программе не менять!
shop_items = {}

for i in lst_in:
    i = i.split()
    i[-3] = i[-3].replace(':', '')
    item = ShopItem(' '.join(i[0:-2]), float(i[-2]), float(i[-1]))
    total = 1
    if item in shop_items:
        shop_items[item][1] += 1
    else:
        shop_items[item] = [item, total]
