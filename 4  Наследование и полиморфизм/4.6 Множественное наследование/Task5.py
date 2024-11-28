class ShopGenericView:
    def __init__(self):
        super().__init__()

    def __repr__(self):
        return f'\n'.join([f'{item[0]}: {item[1]}' for item in self.__dict__.items()])


class ShopUserView:
    def __init__(self):
        super().__init__()

    def __str__(self):
        return f'\n'.join([f'{item[0]}: {item[1]}' for item in self.__dict__.items() if item[0] != "_id"])
    