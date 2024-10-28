class Shop:
    def __init__(self, name):
        self.name = name
        self.goods = []

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        self.goods.remove(product)

class Product:
    id_cls = 1
    def __init__(self, name, weight, price):
        self.id = self.id_cls
        self.set_id()
        self.name = name
        self.weight = weight
        self.price = price

    @classmethod
    def set_id(cls):
        cls.id_cls += 1
        return cls.id_cls
    
    def __setattr__(self, key, value):
        if key == 'name':
            if not isinstance(value, str):
                raise TypeError("Неверный тип присваиваемых данных.")
        elif key == 'id':
            if not isinstance(value, int):
                raise TypeError("Неверный тип присваиваемых данных.")
        else:
            if not isinstance(value, (int, float)) or value < 0:
                raise TypeError("Неверный тип присваиваемых данных.")
        object.__setattr__(self, key, value)
    
    def __delattr__(self, item):
        if item == 'id':
            raise AttributeError(f"Атрибут {item} удалять запрещено.")
        object.__delattr__(self, item)
