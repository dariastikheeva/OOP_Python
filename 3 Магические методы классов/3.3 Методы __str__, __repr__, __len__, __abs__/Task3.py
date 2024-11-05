class Model:
    def __init__(self):
        self.fields = {}

    def query(self, **kwargs):
        for i in kwargs:
            self.fields.update(kwargs)
    def __str__(self):
        if not self.fields:
            return 'Model'
        s = 'Model:'
        for k, v in self.fields.items():
            s += f' {k} = {v},'
        return s.rstrip(',')
    