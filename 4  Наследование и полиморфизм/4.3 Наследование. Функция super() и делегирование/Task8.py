class SoftList(list):
    def __getitem__(self, key):
        if key < 0:
            if abs(key) > len(self):
                return False
            return super().__getitem__(key)
        else:
            if key >= len(self):
                return False
            return super().__getitem__(key)
    