class ListInteger(list):
    def __init__(self, *args):
        for i in args[0]:
            if not isinstance(i, int):
                raise TypeError('можно передавать только целочисленные значения')
        super().__init__(*args)

    def __setitem__(self, key, value):
        if not isinstance(value, int):
            raise TypeError('можно передавать только целочисленные значения')
        super().__setitem__(key, value)

    def append(self, value):
        if not isinstance(value, int):
            raise TypeError('можно передавать только целочисленные значения')
        super().append(value)
